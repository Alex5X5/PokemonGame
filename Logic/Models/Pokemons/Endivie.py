from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Plant import Plant
from Logic.Models.Pokemons.Pokemon import Pokemon


class Endivie(Pokemon):

    def __init__(self, id:int):
        super().__init__(
            id,
            Plant(),
            None,
            30,
            30,
            Punch(self)
        )
