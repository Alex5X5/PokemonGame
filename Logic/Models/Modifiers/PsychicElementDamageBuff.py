from typing_extensions import override

from Logic.Models.Modifiers.Modifier import Modifier


class PsychicElementBuff(Modifier):

    def __init__(self):
        super().__init__()

    @override
    def modify_damage_enemy(self, pokemon:'Pokemon', damage:float) -> float:
        return damage