import tkinter
from abc import abstractmethod, ABC

from GUI.Services.ViewLocator import ViewLocator
from GUI.ViewModels.ViewModelBase import ViewModelBase


class ViewBase(tkinter.Frame, ABC):

    def __init__(self, parent:tkinter.Widget):
        super().__init__(parent)
        self.data_context:ViewModelBase | None = ViewLocator.get_registered_service(self.__class__)
        print(self.data_context)

    @abstractmethod
    def initialize_component(self):
        pass