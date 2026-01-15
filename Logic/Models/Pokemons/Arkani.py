from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Fire import Fire
from Logic.Models.Elements.Water import Water
from Logic.Models.Pokemons.Pokemon import Pokemon


class Arkani(Pokemon):

    def __init__(self, id:int, trainer_name:str):
        super().__init__(
            id,
            trainer_name,
            Fire(),
            Water(),
            70,
            Punch(self)
        )