from Logic.Models.Attacks.FireBreath import FireBreath
from Logic.Models.Attacks.Punch import Punch

from Logic.Models.Pokemons.Endivie import Endivie
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Pokemons.Arkani import Arkani
from Logic.Models.Pokemons.Charizard import Charizard
from Logic.Models.Pokemons.Gengar import Gengar
from Logic.Models.Pokemons.Umbreon import Umbreon


class RegistryService:

    def __init__(self):
        self.__registered_pokemon_types:list[type[Pokemon]] = []
        self.__registered_attack_types:list[type] = []
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

    @property
    def starter_pokemon_type(self):
        return Endivie

    @property
    def attack_types(self) -> list[type]:
        return self.__registered_attack_types

    @property
    def pokemon_types(self) -> list[type]:
        return self.__registered_pokemon_types
