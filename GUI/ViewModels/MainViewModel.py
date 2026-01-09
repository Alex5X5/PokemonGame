from GUI.ViewModels.ViewModelBase import ViewModelBase
from Logic.Services import GameService
from concurrent import futures


class MainViewModel(ViewModelBase):

    def __init__(self, game_service:GameService):
        super().__init__()

        self.thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)


        self.game_service = game_service
