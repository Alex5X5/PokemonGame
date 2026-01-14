from Logic.Models.Attacks.FireBreath import FireBreath
from Logic.Models.Elements.Water import Water
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Elements.Fire import Fire


class Charizard(Pokemon):

    def __init__(self, id:int, trainer_name:str):
        super().__init__(
            id,
            trainer_name,
            Fire(),
            Water(),
            120,
            120,
            FireBreath(self)
        )