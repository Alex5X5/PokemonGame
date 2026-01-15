from abc import abstractmethod, ABC


class AttackEvent:

    def __init__(self, attacker:'Pokemon', victim:'Pokemon', attack:'Attack'):
        self.attacker:'Pokemon' = attacker
        self.victim:'Pokemon' = victim
        self.damage:float = attack.Power
        self.is_blocked:bool = False



class Attack(ABC):

    def __init__(
            self,
            executor:'Pokemon',
            power:float):
        self.__executor:'Pokemon' = executor
        self.__power:float = power

    @property
    def Power(self) -> float:
        return self.__power * (self.__executor.Level / 10 + 0.25)

    def display_str(self):
        return f"{self.__class__.__name__}"

    def execute(self, victim:'Pokemon') -> float:
        e:AttackEvent = AttackEvent(self.__executor, victim, self)
        self.on_pre_attack(e)
        if not e.is_blocked:
            self.on_attack(e)
            self.on_post_attack(e)
            return e.damage
        return 0.0

    @abstractmethod
    def on_pre_attack(self, event:AttackEvent):
        pass

    @abstractmethod
    def on_attack(self, event:AttackEvent):
        event.victim.Health = event.victim.Health - event.damage

    @abstractmethod
    def on_post_attack(self, event:AttackEvent):
        pass