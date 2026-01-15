from Logic.Models.Attacks.Punch import Punch
from Logic.Models.Elements.Ghost import Ghost
from Logic.Models.Elements.Poison import Poison
from Logic.Models.Pokemons.Pokemon import Pokemon


class Umbreon(Pokemon):

    def __init__(self, id:int, trainer_name:str):
        super().__init__(
            id,
            trainer_name,
            Ghost(),
            Poison(),
            80,
            Punch(self)
        )
