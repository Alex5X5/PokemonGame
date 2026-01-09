from abc import abstractmethod, ABC

from Logic.Models.Attacks import AttackEvent


class Attack(ABC):

    def __init__(
            self,
            executor:'Pokemon',
            power:float,
            is_unlocked:bool = False):
        self.__executor:'Pokemon' = executor
        self.__power:float = power
        self.__is_unlocked = is_unlocked

    @property
    def power(self) -> float:
        return self.__power * self.__executor.level / 2

    def execute(self, victim:'Pokemon'):
        e:AttackEvent = AttackEvent(self.__executor, victim)
        self.on_attack(e)

    @abstractmethod
    def on_attack(self, event:AttackEvent):
        pass

    @abstractmethod
    def on_post_attack(self, event:AttackEvent):
        if not event.is_blocked:
            event.victim.health = event.victim.health - event.attack.power


class AttackEvent:

    def __init__(self, attacker:'Pokemon', victim:'Pokemon'):
        self.attacker:'Pokemon' = attacker
        self.victim:'Pokemon' = victim
        self.is_blocked:bool = False