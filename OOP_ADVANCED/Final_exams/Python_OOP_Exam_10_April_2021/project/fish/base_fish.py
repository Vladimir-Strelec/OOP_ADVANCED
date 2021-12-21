from abc import ABC, abstractmethod


class BaseFish(ABC):
    _TYPE = None
    _VALID_NAME_ERROR_MESSAGE = "Fish name cannot be an empty string."
    _VALID_SPECIES_ERROR_MESSAGE = "Fish species cannot be an empty string."
    _VALID_PRICE_ERROR_MESSAGE = "Price cannot be equal to or below zero."

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    def eat(self):
        self.size += 5

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            raise ValueError(cls._VALID_NAME_ERROR_MESSAGE)

    @classmethod
    def __get_valid_species(cls, value):
        if value.strip() == "":
            raise ValueError(cls._VALID_SPECIES_ERROR_MESSAGE)

    @classmethod
    def __get_valid_price(cls, value):
        if value <= 0:
            raise ValueError(cls._VALID_PRICE_ERROR_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__get_valid_species(value)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__get_valid_price(value)
        self.__price = value
