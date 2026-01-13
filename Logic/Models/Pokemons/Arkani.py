from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Fire import Fire
from Logic.Models.Elements.Water import Water
from Logic.Models.Pokemons.Pokemon import Pokemon


class Arkani(Pokemon):

    def __init__(self):
        super().__init__(
            Fire(),
            Water(),
            120,
            100,
            Punch(self)
        )