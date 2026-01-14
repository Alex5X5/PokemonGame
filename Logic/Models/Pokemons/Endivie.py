from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Plant import Plant
from Logic.Models.Pokemons.Pokemon import Pokemon


class Endivie(Pokemon):

    def __init__(self, id:int, trainer_name:str):
        super().__init__(
            id,
            trainer_name,
            Plant(),
            None,
            30,
            30,
            Punch(self)
        )
