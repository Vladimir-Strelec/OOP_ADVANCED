from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = self.create_aquarium(aquarium_type, aquarium_name)
        if not aquarium:
            return f"Invalid aquarium type."
        self.aquariums.append(aquarium)
        return "Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = self.__create_decoration(decoration_type)
        if isinstance(type(decoration), str):
            return decoration
        self.add_decoration(decoration_type)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__get_valid_aquarium_by_aquariums(self.aquariums, aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if isinstance(aquarium, object) and isinstance(decoration, object):
            if not self.decorations_repository.remove(decoration):
                return f"There isn't a decoration of type {decoration_type}."
            aquarium.decorations.append(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.__get_valid_aquarium_by_aquariums(self.aquariums, aquarium_name)
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)
        if self.__check_valid_type_aquarium_and_fish(aquarium, fish_type):
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__get_valid_aquarium_by_aquariums(self.aquariums, aquarium_name)
        return f"Fish fed: {aquarium.feed()}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__get_valid_aquarium_by_aquariums(self.aquariums, aquarium_name)
        summa_comfort = aquarium.calculate_comfort()
        summa_fish = sum([f.price for f in aquarium.fish])
        return f"The value of Aquarium {aquarium_name} is {summa_comfort + summa_fish:.2f}."

    def report(self):
        result = ""
        for a in self.aquariums:
            result += str(a)
        return result

    @staticmethod
    def create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        if aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aquarium_name)
        return None

    @staticmethod
    def __create_decoration(decoration_type):
        if decoration_type == "Ornament":
            return Ornament()
        if decoration_type == "Plant":
            return Plant()
        return f"Invalid decoration type."

    @staticmethod
    def __get_valid_aquarium_by_aquariums(aquariums, aquarium_name):
        for a in aquariums:
            if a.name == aquarium_name:
                return a
        return None

    @staticmethod
    def __create_fish(fish_type, fish_name, fish_species, price):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, fish_species, price)
        if fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, fish_species, price)
        return f"There isn't a fish of type {fish_type}."

    @staticmethod
    def __check_valid_type_aquarium_and_fish(aquarium, fish_type):
        if aquarium.type == fish_type:
            return True
        return False