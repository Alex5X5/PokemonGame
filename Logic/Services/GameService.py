import random

from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Trainer import Trainer
from Logic.Services.DbService import DbService
from Logic.Services.RegsitryService import RegistryService


class GameService:

    def __init__(self, registry_service:RegistryService, database_service:DbService):
        self.regristry_service:RegistryService = registry_service
        self.db_service = database_service
        self.player:Trainer | None = None
        self.__pokemons = []

    def create_random_pokemon(self, owner:Trainer) -> Pokemon:
        type:type = self.regristry_service.pokemon_types[random.Random().randint(0,len(self.regristry_service.pokemon_types)-1)]
        print(type)
        pokemon:Pokemon = type(Trainer)
        print(pokemon)
        self.__pokemons.append(pokemon)

    def figth_random_pokemon(self):
        enemy:Pokemon = self.create_random_pokemon(self.player)
        print(f"selected pokemon type {enemy.__class__}")

    def game_loop(self):
        if not self.player:
            player_name:str = input("enter your player name")
            self.player = self.db_service.load_trainer(player_name)
            print(self.player)
        if len(self.player.pokemons) == 0:
            self.player.pokemons.append(self.regristry_service.starter_pokemon_type(self.player))
            self.db_service.insert_or_update_trainer(self.player)

        self.figth_random_pokemon()
