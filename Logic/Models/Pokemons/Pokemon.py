from copy import copy
import math
from typing import Any

from Logic.Models.Attacks.Attack import *
from Logic.Models.Elements.Element import Element
from Logic.Models.Modifiers import Modifier

class Pokemon:

    def __init__(
            self,
            element1:Element,
            element2:Element | None,
            max_health:float,
            health:float,
            attack1:Attack,
            attack2:Attack | None = None,
            attack3:Attack | None = None,
            experience=0.0):
        self.__element1:Element = element1
        self.__element2:Element or None = element2
        self.__max_health:float = max_health
        self.__health:float = health
        self.attack1:Attack = attack1
        self.attack2:Attack | None = attack2
        self.attack3:Attack | None = attack3
        self.__experience:float = experience
        self.modifiers:list[Modifier] = []

    @classmethod
    def from_dictionary(cls, data:dict[str, Any]):
        new_logger = cls.__new__(cls)
        return new_logger

    @property
    def element1(self):
        return self.__element1

    @property
    def element2(self):
        return self.__element2

    @property
    def experience(self) -> float:
        return self.__experience

    @experience.setter
    def __set_eperience(self, value):
        self.__experience = value

    @property
    def level(self) -> int:
        return int(math.floor(50*(math.log((self.experience*99+10000)/10000, 10))))

    @property
    def max_health(self) -> float:
        return math.floor(self.__max_health * self.level) + self.level + 10

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    def set_health(self, value:float):
        self.__health = value

    @experience.setter
    def set_experience(self, value:float):
        self.__experience = value

    def execute_attack_1(self, target:'Pokemon'):
        pass

    def execute_attack_2(self, target:'Pokemon'):
        pass

    def execute_attack_3(self, target:'Pokemon'):
        pass
