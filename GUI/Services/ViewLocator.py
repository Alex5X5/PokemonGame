import importlib
from types import ModuleType
from typing import Type


class ViewLocator:

    __view_models:dict[Type, any or None] = {}

    @staticmethod
    def get_registered_service(cls:Type) -> any or None:
        try:
            return ViewLocator.__view_models[cls]
        except KeyError:
            return None

    @staticmethod
    def register_page_type_singleton(view_model):
        view_module_string: str = str(view_model.__class__.__module__).replace('ViewModel', 'View')
        view_class_string: str = str(view_model.__class__.__name__).replace('ViewModel', 'View')
        print(f"module name of view is {view_module_string}")
        print(f"class name of view is {view_class_string}")
        try:
            module:ModuleType = importlib.import_module(view_module_string, view_class_string)
            dynamic_class:Type = getattr(module, view_class_string)
            if dynamic_class:
                ViewLocator.__view_models[dynamic_class] = view_model
        except ModuleNotFoundError:
            print(f"view type {view_model.__class__.__name__} has no view type")

    @staticmethod
    def register_service_singleton(service:any):
        ViewLocator.__view_models[service.__class] = service
