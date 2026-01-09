import os, sys
import pathlib
from shutil import copyfile

class PathService:

    def __init__(self):
        self.real_path_string: str = os.path.dirname(os.path.realpath(__file__))
        self.root_path_string: str = str(pathlib.Path.cwd()) + '\\'
        self.bundled_app_files_path_string: str = os.path.join(sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + '\\'
        self.app_files_path_string: str = self.root_path_string + 'pokemon-game-files\\'
        self.assets_path_string: str = self.bundled_app_files_path_string + 'Assets\\'
        print('root path:' + self.root_path_string)
        print('bundled app files path:' + self.bundled_app_files_path_string)
        print('app files path:' + self.app_files_path_string)
        print('assets path:' + self.assets_path_string)

    def gen_app_files(self):
        """
            creates a directory for the app files and initializes a fallback database as well as the local config file
        """
        if not pathlib.Path(self.app_files_path_string + r'pokemon_database.sqlite3').is_file():
            copyfile(
                self.bundled_app_files_path_string + r'sec_data_info\DD-invBeispielDatenbank.sqlite3',
                self.app_files_path_string + r'pokemon_database.sqlite3'
            )

    def assets_path(self, relative_asset_path: str) -> str:
        """
            generates a string with the path of the assets folder together with the relative path

            :param str relative_asset_path: the path relative to the assets folder

            :return: a string representing the path
        """
        return os.path.join(self.assets_path_string, relative_asset_path)


s = PathService()
print(s.assets_path('test.png'))
