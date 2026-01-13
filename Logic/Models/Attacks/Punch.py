from typing import override

from Logic.Models.Attacks.Attack import Attack, AttackEvent

class Punch(Attack):

    def __init__(self, executor:'Pokemon'):
        super().__init__(executor, 10)

    @override
    def on_pre_attack(self, event: AttackEvent):
        super().on_pre_attack(event)

    @override
    def on_attack(self, event: AttackEvent):
        super().on_attack(event)

    @override
    def on_post_attack(self, event: AttackEvent):
        super().on_post_attack(event)
        print(f"{event.attacker.display_str()} throws a punch")