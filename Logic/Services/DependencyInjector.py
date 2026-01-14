from enum import Enum, auto
from functools import wraps, update_wrapper

from typing import Any, Type, Callable, Iterator
from inspect import Parameter, signature


class DpiEntryPoint:

    def __init__(self, func):
        self.func = func
        self.owner_class = None

    def __set_name__(self, owner, method_name):
        self.owner_class = owner
        entry_point_names = DependencyInjector.entry_points.get(self.owner_class, [])
        entry_point_names.append(method_name)
        DependencyInjector.entry_points.update({self.owner_class: entry_point_names})
        #print(f"marking function {method_name} of class {self.owner_class.__name__} as a valid dpi entry point")

    def __get__(self, instance, owner):
        if instance is None:
            return self.func
        def wrapper(*args, **kwargs):
            return self.func(instance, *args, **kwargs)
        update_wrapper(wrapper, self.func)
        return wrapper


class ImplementationPolicy(Enum):
    Singleton = auto


class ServiceCollection:

    def __init__(self):
        self.__services_to_build:list[tuple[Type, Type, ImplementationPolicy]] = []
        self.__services:dict[Type, Any] = {}
        self.__did_build_services:bool = False

    @property
    def Services_to_build(self) -> list[tuple[Type, Type, ImplementationPolicy]]:
        return self.__services_to_build

    @property
    def Services(self) -> dict[Type, Any]:
        if not self.__did_build_services:
            raise RuntimeError('can not get services before building')
        return self.__services

    def enable_did_build_services(self) -> None:
        self.__did_build_services = True

    def get_service(self, T:Type) -> Any | None:
        print(f"services:\n{'\n'.join(s.__name__ for s in self.__services)}")
        return self.__services.get(T)


class DependencyInjector:

    entry_points:dict[type, list[str]] = {}

    def __init__(self):
        self.__service_collection:ServiceCollection = ServiceCollection()

    def build_services(self) -> ServiceCollection:
        print(f"started buiding services")
        self.__service_collection.enable_did_build_services()
        for cls_T, reg_T, policy in self.__service_collection.Services_to_build:
            print(f"building service {cls_T.__name__}")
            entry_points:list[Callable]
            try:
                entry_points = [getattr(cls_T, p) for p in DependencyInjector.entry_points[cls_T]]
            except KeyError:
                raise RuntimeError(f"""the type {cls_T.__name__} has no methods marked with 'DpiEntryPoint'""")
            entry_points = sorted(entry_points, key = lambda p: len(signature(p).parameters))
            for entry_point in entry_points:
                all_params_available:bool = True
                prams_to_use:list[Any] = []
                for param_name, param in signature(entry_point).parameters.items():
                    print(f"param annotation:{param.annotation}")
                    if param_name == 'self':
                        continue
                    val = self.__service_collection.get_service(param.annotation)
                    if val is None:
                        all_params_available = False
                        print(f"missing parameter of type:{val}")
                        break
                    else:
                        prams_to_use.append(val)
                print(f"all params available:{all_params_available}")
                if all_params_available:
                    print(f"creating instance")
                    instance = object.__new__(object)
                    instance = cls_T.__new__(cls_T, instance)
                    entry_point(instance, *prams_to_use)
                    print(f"instance:{instance}")
                    self.__service_collection.Services.update({reg_T:instance})
                    break
        return self.__service_collection

    def register_service_singleton_for_type(self, cls_T:Type, reg_T:Type):
        self.__service_collection.Services_to_build.append((reg_T, cls_T, ImplementationPolicy.Singleton))

    def register_service_singleton(self, cls_T:Type):
        self.register_service_singleton_for_type(cls_T, cls_T)

    def register_service_singleton_instance(self, cls_T:Type, instance):
        self.__service_collection.Services[cls_T] = instance

    def register_service_transient(self):
        pass