import tkinter

from GUI.Views.MainView import MainView


class PokemonGameWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("PokemonSprite.py Game")

        # Fensterbreite und -höhe definieren
        window_width = 1700
        window_height = 1000

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        #self.resizable(False, False)  # Ermögliche Größenanpassung des Fensters

        self.main_view = MainView(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_view.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
