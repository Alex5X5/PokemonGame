from GUI.Views.Components.PokemonSprite import PokemonSprite
from Logic.Models.Elements.Fire import Fire
from Logic.Models.Elements.Flying import Flying


class CharizardPokemonSprite(PokemonSprite):

    def __init__(self):
        super().__init__(
            Fire(),
            Flying(),
            100,
            100,


        )
