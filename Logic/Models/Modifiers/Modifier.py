
class Modifier:

    def __init__(self):
        pass

    def on_pre_attack_deal(self, pokemon: 'Pokemon', damage: float) -> float:
        return damage

    def on_attack_deal(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def on_post_attack_deal(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def on_pre_attack_take(self, pokemon: 'Pokemon', damage: float) -> float:
        return damage

    def on_attack_take(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def on_post_attack_take(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def modify_damage_enemy(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def modify_damage_self(self, pokemon:'Pokemon', health:float) -> float:
        return health

    def modify_get_max_health(self, pokemon:'Pokemon', health:float) -> float:
        return health

    def modify_get_attack_power(self, pokemon:'Pokemon', damage:float) -> float:
        return damage




