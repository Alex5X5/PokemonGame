from Logic.Models.Attacks.Attack import Attack, AttackEvent

class FireBreath(Attack):

    def __init__(self, executor:'Pokemon'):
        super().__init__(executor, 50)

    def on_pre_attack(self, event: AttackEvent):
        super().on_pre_attack(event)

    def on_post_attack(self, event: AttackEvent):
        super().on_post_attack(event)
        print(f"{event.attacker.display_str()} spits fire")
