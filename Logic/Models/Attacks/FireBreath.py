from Logic.Models.Attacks.Attack import Attack, AttackEvent
from Logic.Models.Pokemons.Pokemon import Pokemon


class FireBreath(Attack):

    def __init__(self, executor:Pokemon):
        super().__init__(executor, 50)

    def on_attack(self, event: AttackEvent):
        super().on_attack(event)

    def on_post_attack(self, event: AttackEvent):
        super().on_post_attack()
