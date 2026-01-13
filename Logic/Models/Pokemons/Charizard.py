from Logic.Models.Attacks.FireBreath import FireBreath
from Logic.Models.Elements.Water import Water
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Elements.Fire import Fire


class Charizard(Pokemon):

    def __init__(self):
        super().__init__(
            Fire(),
            Water(),
            120,
            100,
            FireBreath(self)
        )