from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            ValueError("Name cannot be empty string or white space!")

    @classmethod
    def __get_valid_portion(cls, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

    @classmethod
    def __get_valid_brand(cls, value):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty string or white space!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__get_valid_portion(value)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__get_valid_brand(value)
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
