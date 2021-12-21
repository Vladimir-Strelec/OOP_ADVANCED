from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    _MIN_TABLE_NUMBER = None
    _MAX_TABLE_NUMBER = None
    _INVALID_TABLE_NUMBER_MESSAGE = None

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @classmethod
    def __get_valid_table_number(cls, value):
        if cls._MIN_TABLE_NUMBER and value < cls._MIN_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        if cls._MAX_TABLE_NUMBER and value > cls._MAX_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        pass

    @classmethod
    def __get_valid_capacity(cls, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

    @property
    @abstractmethod
    def table_type(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__get_valid_table_number(value)
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__get_valid_capacity(value)
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result_drink = sum([i.price for i in self.drink_orders])
        result_food = sum([i.price for i in self.food_orders])
        return result_food + result_drink
        #TODO: Neponyatno kak vischtivat obshiy schet

    def clear(self):
        if self.is_reserved:
            self.food_orders.clear()
            self.drink_orders.clear()
            self.number_of_people = 0
            self.is_reserved = False

    def free_table_info(self):
        if self.is_reserved:
            return None
        return f"""Table: {self.table_number}
Type: {self.table_type}
Capacity: {self.capacity}
"""



