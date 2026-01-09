import tkinter

from GUI.Views.ViewBase import ViewBase


class MainView(ViewBase):

    def __init__(self, parent:tkinter.Widget):
        super().__init__(parent)
        self.config(background='green')

    def initialize_component(self):
        pass
