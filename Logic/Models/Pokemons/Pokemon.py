import math
from typing import Any, Final

from Logic.Models.Attacks.Attack import *
from Logic.Models.Elements.Element import Element
from Logic.Models.Modifiers.Modifier import Modifier


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
        self.__element2:Element | None = element2
        self.__max_health:Final[float] = max_health
        self.__health:float = health
        self.__attack1:Attack = attack1
        self.__attack2:Attack | None = attack2
        self.__attack3:Attack | None = attack3
        self.__experience:float = experience
        self.modifiers:list[Modifier] = []

    def __str__(self):
        return f"<Logic.Models.Pokemons.Pokemon.Pokemon[Element1={self.Element1}, Element2={self.Element2}, Max Health={self.__max_health}, Health={self.__health}, Experience={self.__experience}]>"

    def display_str(self):
        return f"[{self.Level}]{self.__class__.__name__}"

    def set_from_dictionary(self, data:dict[str, Any]):
        from Logic.Services.DbService import DbService
        self.__experience = data.get(DbService.POKEMON_EXPERIENCE_KEY)

    @property
    def Max_Health(self) -> float:
        return math.floor(self.__max_health * self.Level) + self.Level + 10

    @property
    def Health(self) -> float: return self.__health

    @Health.setter
    def Health(self, value:float): self.__health = max(min(value, self.Max_Health), 0)

    @property
    def Element1(self) -> Element: return self.__element1

    @property
    def Element2(self) -> Element | None: return self.__element2

    @property
    def Experience(self) -> float: return self.__experience

    @Experience.setter
    def Experience(self, value:float): self.__experience = value

    @property
    def Attack1(self) -> Attack: return self.__attack1

    @property
    def Attack2(self) -> Attack | None: return self.__attack2

    @property
    def Attack3(self) -> Attack | None: return self.__attack3

    @property
    def Level(self) -> int:
        return int(math.floor(50 * (math.log((self.Experience * 99 + 10000) / 10000, 10))))

    def has_attack2(self) -> bool:
        return self.__attack2 is not None and self.Level > 10

    def has_attack3(self) -> bool:
        return self.__attack3 is not None and self.Level > 30

    def is_down(self) -> bool:
        return self.Health == 0.0

    def execute_attack_1(self, target:'Pokemon'):
        self.__attack1.execute(target)

    def execute_attack_2(self, target:'Pokemon'):
        self.__attack2.execute(target)

    def execute_attack_3(self, target:'Pokemon'):
        self.__attack3.execute(target)

