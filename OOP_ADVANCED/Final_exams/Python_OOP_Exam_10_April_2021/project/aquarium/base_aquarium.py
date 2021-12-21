from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    _TYPE = None
    _VALID_NAME_AQUARIUM_ERROR = "Aquarium name cannot be an empty string."

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @classmethod
    def __get_valid_type(cls, value):
        if cls._TYPE and not cls._TYPE == "FreshwaterFish" or cls._TYPE == "SaltwaterFish":
            return f"There isn't a fish of type {value}."
        pass

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            raise ValueError(cls._VALID_NAME_AQUARIUM_ERROR)

    def calculate_comfort(self):
        sum_comfort = [c.comfort*c.price for c in self.decorations]
        return sum(sum_comfort)

    def add_fish(self, fish):
        if self.capacity <= 0:
            return f"Not enough capacity."
        if self.__check_valid_fish(fish):
            self.fish.append(fish)
            self.capacity -= 1
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        for f in self.fish:
            if f.name == fish.name and self.__check_valid_fish(fish):
                self.fish.remove(f)
                self.capacity += 1

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        count = 0
        for f in self.fish:
            f.eat()
            count += 1
        return count

    def __str__(self):
        fish_list_name = self.__get_fish_name_or_none(self.fish)
        return f"""{self.name}:
Fish: {fish_list_name}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}
"""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @staticmethod
    def __check_valid_fish(fish):
        if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
            return True

    @staticmethod
    def __get_fish_name_or_none(fish):
        result = ""
        if any(fish):
            result += " ".join([n.name for n in fish])
        else:
            result += "none"
        return result

    @property
    @abstractmethod
    def type(self):
        pass