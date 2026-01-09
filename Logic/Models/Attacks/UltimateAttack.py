from Logic.Models.Attacks.Attack import Attack


class UltimateAttack(Attack):

    def __init__(self, damag_per_attack:float):
        super().__init__(damag_per_attack)