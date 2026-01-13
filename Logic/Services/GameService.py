import random

from typing import Type

from Logic.Models.Attacks.Attack import Attack
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

    def create_random_pokemon(self) -> Pokemon:
        pokemon_type:Type[Pokemon] = self.regristry_service.pokemon_types[random.Random().randint(0,len(self.regristry_service.pokemon_types)-1)]
        null_player:Trainer = self.db_service.load_trainer("null_player")
        pokemon:Pokemon = pokemon_type(null_player.Id)
        self.__pokemons.append(pokemon)
        return pokemon

    def choose_pokemon(self) -> Pokemon:
        print("Your pokemon are:")
        #for i in range(len(self.player.pokemons)):
        for i, pokemon in enumerate(self.player.pokemons):
            if not pokemon.is_down():
                print(f"{i+1}: {pokemon.display_str()}")
        while True:
            input_string:str = input(f"enter a number between 1 and {len(self.player.pokemons)}")
            try:
                input_number:int = int(input_string)
                if input_number < 1:
                    raise ValueError
                if input_number > len(self.player.pokemons) + 1:
                    raise ValueError
                pokemon:Pokemon = self.player.pokemons[input_number-1]
                print(f"you choose {pokemon.display_str()}")
                return pokemon
            except ValueError:
                print(f"\"{input_string}\" is not a valid input")

    def choose_random_attack(self, pokemon:Pokemon) -> Attack:
        available_attacks_count:int = 1
        if pokemon.has_attack2():
            available_attacks_count += 1
        if pokemon.has_attack3():
            available_attacks_count += 1
        if available_attacks_count == 1:
            return pokemon.Attack1
        rand = random.random() * available_attacks_count
        if rand < 1:
            return pokemon.Attack1
        if rand < 2:
            return pokemon.Attack2
        return pokemon.Attack3

    def choose_attack(self, pokemon:Pokemon) -> Attack:
        print("Available attacks are:")
        print(pokemon.Attack1.display_str())
        if pokemon.has_attack2():
            print(pokemon.Attack2.display_str())
        if pokemon.has_attack3():
            print(pokemon.Attack3.display_str())
        available_attacks_count:int = 1
        if pokemon.has_attack2():
            available_attacks_count += 1
        if pokemon.has_attack3():
            available_attacks_count += 1
        if available_attacks_count == 1:
            return pokemon.Attack1
        while True:
            attack:Attack | None = None
            input_string:str = input(f"enter a number between 1 and {available_attacks_count}")
            try:
                input_number:int = int(input_string)
                if input_number < 1:
                    raise ValueError
                if input_number > available_attacks_count:
                    raise ValueError
                if input_number == 1:
                    attack = pokemon.Attack1
                if input_number == 2:
                    attack = pokemon.Attack1
                if input_number == 3:
                    attack = pokemon.Attack1
                if attack is None:
                    raise ValueError
                print(f"you choose {attack.display_str()}")
            except ValueError:
                print(f"\"{input_string}\" is not a valid input")

    def figth_random_pokemon(self):
        enemy_pokemon:Pokemon = self.create_random_pokemon()
        own_pokemon:Pokemon = self.choose_pokemon()
        is_own_turn:bool = random.random() > 0.5
        damage_dealt:float = 0.0
        while True:
            if is_own_turn:
                self.choose_attack(own_pokemon).execute(enemy_pokemon)
                print(f"the enemy pokemon has {enemy_pokemon.Health} left")
            else:
                self.choose_random_attack(enemy_pokemon).execute(own_pokemon)
                print(f"your pokemon has {own_pokemon.Health} left")
            if own_pokemon.is_down():
                self.on_own_pokemon_down()
                break
            if enemy_pokemon.is_down():
                self.on_enemy_pokemon_down()
                break
            is_own_turn:bool = not is_own_turn

    def on_enemy_pokemon_down(self):
        print(f"your defeated the enemy pokemon")

    def on_own_pokemon_down(self):
        print(f"your were defeated by the enemy pokemon")

    def game_loop(self):
        #load a player if none is set
        if not self.player:
            player_name:str = ""
            while player_name == "null_player" or player_name == "":
                player_name = input("enter your player name")
            self.player = self.db_service.load_trainer(player_name)
        #give a starter pokemon to the player is he has none
        if len(self.player.pokemons) == 0:
            self.player.pokemons.append(self.regristry_service.starter_pokemon_type(self.player.Id))
            self.db_service.update_trainer(self.player)
        self.figth_random_pokemon()
