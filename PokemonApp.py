from GUI.PokemonGameWindow import PokemonGameWindow
from GUI.Services.ViewLocator import ViewLocator
from GUI.ViewModels.MainViewModel import MainViewModel
from Logic.Services.DbService import DbService
from Logic.Services.GameService import GameService
from Logic.Services.PathService import PathService
from Logic.Services.RegsitryService import RegistryService


class PokemonApp:

    def __init__(self):

        self.registry_service:RegistryService = RegistryService()
        self.path_service:PathService = PathService()
        self.database_service:DbService = DbService(self.path_service, self.registry_service)
        self.game_service:GameService = GameService(self.registry_service, self.database_service)
        self.game_service.game_loop()

        #main_view_model:MainViewModel = MainViewModel(self.game_service)
        #ViewLocator.register_page_type_singleton(main_view_model)

        #window:PokemonGameWindow = PokemonGameWindow()

        #window.mainloop()
