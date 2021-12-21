from abc import ABC, abstractmethod


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            ValueError("Name cannot be empty string or white space!")

    @classmethod
    def __get_valid_portion(cls, value):
        if value <= 0:
            ValueError("Price cannot be less than or equal to zero!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__get_valid_portion(value)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
