
class Modifier:

    def modify_damage_entity(self, pokemon:'Pokemon', damage:float) -> float:
        return damage

    def modify_set_health(self, pokemon:'Pokemon', health:float) -> float:
        return health

    def modify_get_max_health(self, pokemon:'Pokemon', health:float) -> float:
        return health

    def modify_get_attack_power(self, pokemon:'Pokemon', damage:float) -> float:
        return damage




