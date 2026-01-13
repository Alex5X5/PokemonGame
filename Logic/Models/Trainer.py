from typing import Any

from Logic.Models.Pokemons.Pokemon import Pokemon


class Trainer:

    def __init__(self, id_:int, name:str):
        self.__id:int = id_
        self.__name:str = name
        self.__owned_pokemons:list[Pokemon] = []

    def __str__(self):
        return f"Logic.Models.Trainer.Trainer[Id={self.Id}, Name={self.Name}, Pokemons=[{','.join([str(p) for p in self.__owned_pokemons])}]]"

    @property
    def Id(self) -> int:
        return self.__id

    @property
    def Name(self) -> str:
        return self.__name

    @property
    def Reputiation(self) -> float:
        return round(1000 - 400000 / (sum([p.Level for p in self.__owned_pokemons]) + 400), 1)

    @property
    def pokemons(self) -> list[Pokemon] | None:
        return self.__owned_pokemons

    @classmethod
    def from_dictionary(cls, data:dict[str, Any]) -> 'Trainer':
        new_trainer = cls.__new__(cls)
        new_trainer.__init__(data['Id'], data['Name'])
        return new_trainer

