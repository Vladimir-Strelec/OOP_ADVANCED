from abc import ABC, abstractmethod


class Astronaut(ABC):
    _VALID_NAME_ASTRONAUT_ERROR_MESSAGE = "Astronaut name cannot be empty string or whitespace!"

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        result = f"Name: {self.name}\n"
        result += f"Oxygen: {self.oxygen}\n"
        if len(self.backpack) > 0:
            result += f"Backpack items: {', '.join([b for b in self.backpack])}"
        else:
            result += "Backpack items: none"
        return result

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            raise ValueError(cls._VALID_NAME_ASTRONAUT_ERROR_MESSAGE)

