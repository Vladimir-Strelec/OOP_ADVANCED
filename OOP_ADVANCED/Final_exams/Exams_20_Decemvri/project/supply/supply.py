from abc import ABC, abstractmethod


class Supply(ABC):
    _VALUE_ERROR_NAME = "Name cannot be an empty string."
    _VALUE_ERROR_ENERGY = "Energy cannot be less than zero."

    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @classmethod
    def __get_valid_energy(cls, value):
        if value < 0:
            raise ValueError(cls._VALUE_ERROR_ENERGY)

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            raise ValueError(cls._VALUE_ERROR_NAME)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__get_valid_energy(value)
        self.__energy = value

