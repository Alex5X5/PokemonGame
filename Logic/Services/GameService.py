import random
import time

from typing import Type, Any

from Logic.Models.Attacks.Attack import Attack
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Trainer import Trainer
from Logic.Services.DbService import DbService
from Logic.Services.DependencyInjector import DpiEntryPoint
from Logic.Services.RegsitryService import RegistryService


class PokemonDefeatedEvent:

    def __init__(self, winner:'Pokemon', looser:'Pokemon', winner_damaged:float, looser_damaged:float):
        self.winner:'Pokemon' = winner
        self.looser:'Pokemon' = looser
        self.winner_damaged:float = winner_damaged
        self.looser_damaged:float = looser_damaged

    def did_win(self, pokemon:'Pokemon'):
        return self.winner == pokemon

    def did_lose(self, pokemon:'Pokemon'):
        return self.looser == pokemon


class GameService:

    @DpiEntryPoint
    def __init__(self, registry_service:RegistryService, database_service:DbService):
        self.regristry_service:RegistryService = registry_service
        self.db_service = database_service
        self.player:Trainer | None = None
        self.__pokemons = []

    def create_random_pokemon(self) -> Pokemon:
        pokemon_type:Type[Pokemon] = self.regristry_service.pokemon_types[random.Random().randint(0,len(self.regristry_service.pokemon_types)-1)]
        null_player:Trainer = self.db_service.load_trainer("null_player")
        pokemon:Any[Pokemon] = pokemon_type(0, null_player.Name)
        self.db_service.insert_pokemon(pokemon, null_player)
        self.__pokemons.append(pokemon)
        return pokemon

    def give_start_pokemon(self):
        self.player.Pokemons.append(self.regristry_service.starter_pokemon_type(0, self.player.Name))
        self.player.Pokemons[0].Experience = 30
        self.db_service.update_trainer(self.player)

    def choose_pokemon(self) -> Pokemon:
        print("Your pokemon are:")
        for i, pokemon in enumerate(self.player.Pokemons):
            if not pokemon.is_down():
                print(f"{i+1}: {pokemon.display_str()}")
        while True:
            input_string:str = input(f"enter a number between 1 and {len(self.player.Pokemons)}")
            try:
                input_number:int = int(input_string)
                if input_number < 1:
                    raise ValueError
                if input_number > len(self.player.Pokemons) + 1:
                    raise ValueError
                pokemon:Pokemon = self.player.Pokemons[input_number - 1]
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
        print(f"a {enemy_pokemon.display_str()} jumps out of the bushes")
        time.sleep(3.0)
        own_pokemon:Pokemon = self.choose_pokemon()
        is_own_turn:bool = random.random() > 0.5
        damage_dealt_to_enemy:float = 0.0
        damage_dealt_to_self:float = 0.0
        time.sleep(3.0)
        while True:
            if is_own_turn:
                damage_dealt_to_enemy += self.choose_attack(own_pokemon).execute(enemy_pokemon)
                print(f"the enemy pokemon has {enemy_pokemon.Health} left")
                time.sleep(3)
            else:
                damage_dealt_to_self += self.choose_attack(own_pokemon).execute(enemy_pokemon)
                self.choose_random_attack(enemy_pokemon).execute(own_pokemon)
                print(f"your pokemon has {own_pokemon.Health} left")
                time.sleep(3)
            if own_pokemon.is_down():
                time.sleep(3)
                event:PokemonDefeatedEvent = PokemonDefeatedEvent(enemy_pokemon, own_pokemon, damage_dealt_to_enemy, damage_dealt_to_self)
                self.on_own_pokemon_down(event)
                break
            if enemy_pokemon.is_down():
                time.sleep(3)
                event:PokemonDefeatedEvent = PokemonDefeatedEvent(own_pokemon, enemy_pokemon, damage_dealt_to_self, damage_dealt_to_enemy)
                self.on_enemy_pokemon_down(event)
                break
            is_own_turn:bool = not is_own_turn

    def on_enemy_pokemon_down(self, event:PokemonDefeatedEvent):
        print(f"your {event.winner.display_str()} defeated the enemy {event.looser.display_str()}\n\n")
        event.winner.Experience += event.looser_damaged
        time.sleep(5)
        print(f"will the enemy pokemon trust you ?")
        time.sleep(5)
        if random.randint(1, 100) < self.player.Reputiation:
            self.on_pokemon_trusts_player(event)
        else:
            print(f"the pokemon desides that you are not worthy enough and hobbles away")
        self.db_service.update_trainer(self.player)

    def on_own_pokemon_down(self, event:PokemonDefeatedEvent):
        print(f"your {event.looser.display_str()} was defeated by the enemy {event.winner.display_str()}\n\n")


    def on_pokemon_trusts_player(self, event:PokemonDefeatedEvent):
        print(f"the pokemon desided that this was an honorable loss and wants to join you")
        time.sleep(1)
        print(f"do you want to train the {event.looser.display_str()}?")
        while True:
            input_str:str = input(f"enter y for yes or n for no")
            if input_str == "y":
                self.on_pokemon_trusts_player(event)
                return
            elif input_str == "n":
                self.on_pokemon_trusts_player(event)
                return

    def on_player_accepts_pokemon(self, event:PokemonDefeatedEvent):
        pass

    def on_player_rejects_pokemon(self, event:PokemonDefeatedEvent):
        pass

    def game_loop(self):
        #load a player if none is set
        if not self.player:
            player_name:str = ""
            while player_name == "null_player" or player_name == "":
                player_name = input("enter your player name")
            self.player = self.db_service.load_trainer(player_name)
        if len(self.player.Pokemons) == 0:
            self.give_start_pokemon()
        for pokemon in self.player.Pokemons:
            pokemon.Health = pokemon.Max_Health
        self.figth_random_pokemon()
