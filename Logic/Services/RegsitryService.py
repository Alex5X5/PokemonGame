from typing import Type

from Logic.Models.Attacks.Attack import Attack
from Logic.Models.Attacks.FireBreath import FireBreath
from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Element import Element

from Logic.Models.Pokemons.Endivie import Endivie
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Pokemons.Arkani import Arkani
from Logic.Models.Pokemons.Charizard import Charizard
from Logic.Models.Pokemons.Gengar import Gengar
from Logic.Models.Pokemons.Umbreon import Umbreon
from Logic.Services.DependencyInjector import DpiEntryPoint


class RegistryService:

    @DpiEntryPoint
    def __init__(self):
        self.__registered_pokemon_types:list[Type[Pokemon]] = []
        self.__registered_attack_types:list[Type[Attack]] = []
        self.__registered_element_types:list[Type[Element]] = []
        self.__register_pokemons()
        self.__register_attacks()

    def __register_pokemons(self):
        self.__registered_pokemon_types.append(Arkani)
        self.__registered_pokemon_types.append(Charizard)
        self.__registered_pokemon_types.append(Gengar)
        self.__registered_pokemon_types.append(Umbreon)
        self.__registered_pokemon_types.append(Endivie)

    def __register_attacks(self):
        self.__registered_attack_types.append(Punch)
        self.__registered_attack_types.append(FireBreath)

    def __register_elements(self):
        self.__registered_attack_types.append(Punch)
        self.__registered_attack_types.append(FireBreath)

    @property
    def starter_pokemon_type(self):
        return Endivie

    @property
    def attack_types(self) -> list[Type]:
        return self.__registered_attack_types

    @property
    def pokemon_types(self) -> list[Type[Pokemon]]:
        return self.__registered_pokemon_types

    @property
    def element_types(self) -> list[Type[Pokemon]]:
        return self.__registered_pokemon_types

    def find_pokemon_type(self, type_name:str) -> Type[Pokemon] | None:
        for t in self.__registered_pokemon_types:
            if t.__name__ == type_name:
                return t
        return None

    def find_attack_type(self, type_name:str) -> Type[Attack] | None:
        for t in self.__registered_attack_types:
            if t.__name__ == type_name:
                return t
        return None

    def find_element_type(self, type_name:str) -> Type[Element] | None:
        for t in self.__registered_element_types:
            if t.__name__ == type_name:
                return t
        return None
