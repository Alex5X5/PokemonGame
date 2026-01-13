from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Fire import Fire
from Logic.Models.Elements.Water import Water
from Logic.Models.Pokemons.Pokemon import Pokemon


class Arkani(Pokemon):

    def __init__(self, id:int):
        super().__init__(
            id,
            Fire(),
            Water(),
            70,
            70,
            Punch(self)
        )