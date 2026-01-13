from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Ghost import Ghost
from Logic.Models.Elements.Poison import Poison
from Logic.Models.Pokemons.Pokemon import Pokemon


class Gengar(Pokemon):

    def __init__(self):
        super().__init__(
            Ghost(),
            Poison(),
            110,
            110,
            Punch(self)
        )
