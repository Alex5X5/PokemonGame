import time

from Logic.Services.Logger import Logger
from Logic.Services.DbService import DbService
from Logic.Services.DependencyInjector import DependencyInjector, ServiceCollection
from Logic.Services.GameService import GameService
from Logic.Services.PathService import PathService
from Logic.Services.RegsitryService import RegistryService


class PokemonApp:

    def __init__(self):

        self.injector: DependencyInjector = DependencyInjector()
        self.injector.register_service_singleton(Logger)
        self.injector.register_service_singleton(RegistryService)
        self.injector.register_service_singleton(PathService)
        self.injector.register_service_singleton(DbService)
        self.injector.register_service_singleton(GameService)
        services:ServiceCollection = self.injector.build_services()
        gs = services.get_service(GameService)
        while True:
            gs.game_loop()
            time.sleep(2.0)

        #main_view_model:MainViewModel = MainViewModel(self.game_service)
        #ViewLocator.register_page_type_singleton(main_view_model)

        #window:PokemonGameWindow = PokemonGameWindow()

        #window.mainloop()
