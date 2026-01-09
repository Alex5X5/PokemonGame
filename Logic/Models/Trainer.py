from typing import Any

from Logic.Models.Pokemons.Pokemon import Pokemon


class Trainer:

    def __init__(self, id_:int, name:str):
        self.__id:int = id_
        self.__name:str = name
        self.__owned_pokemons:list[Pokemon] = []

    @property
    def id(self)->int:
        return self.__id

    @property
    def name(self)->int:
        return self.__name

    @property
    def pokemons(self) -> list[Pokemon] | None:
        return self.__owned_pokemons

    @classmethod
    def from_dictionary(cls, data:dict[str, Any]):
        new_trainer = cls.__new__(cls)
        print(data)
        new_trainer.__init__(data['Id'], data['Name'])

        return new_trainer
