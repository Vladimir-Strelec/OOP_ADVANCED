from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    __number_of_successful_missions = 0
    __number_of_not_successful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__create_astronaut(astronaut_type, name)
        if self.astronaut_repository.find_by_name(astronaut.name):
            return f"{astronaut.name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut.__class__.__name__}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        planet = self.__create_planet(name)
        planet.items = items.split(", ")
        if self.planet_repository.find_by_name(planet.name):
            return f"{planet.name} is already added."
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {astronaut.name} was retired!"

    def recharge_oxygen(self):
        for astr in self.astronaut_repository.astronauts:
            astr.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not self.planet_repository.find_by_name(planet.name):
            raise Exception("Invalid planet name!")
        astronauts = self._get_5_astronauts(self.astronaut_repository.astronauts)

        for current_astronaut in astronauts:
            participated = 0
            while planet.items and current_astronaut.oxygen > 0:
                current_astronaut.backpack.append(planet.items.pop())
                current_astronaut.breathe()

            else:
                self.__number_of_successful_missions += 1
                participated += 1
                return f"Planet: {planet_name} was explored. {participated} astronauts participated in collecting items."

        self.__number_of_not_successful_missions += 1
        return f"Mission is not completed."

    def report(self):
        result = f"{self.__number_of_successful_missions} successful missions!" + "\n"
        result += f"{self.__number_of_not_successful_missions} missions were not completed!" + "\n"
        result += f"Astronauts' info:" + "\n"

        for a in self.astronaut_repository.astronauts:
            result += str(a) + '\n'
        return result.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        if astronaut_type == "Geodesist":
            return Geodesist(name)
        if astronaut_type == "Meteorologist":
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")

    @staticmethod
    def __create_planet(name):
        return Planet(name)

    @staticmethod
    def _get_5_astronauts(astronauts):
        astronauts = sorted(astronauts, key=lambda x: x.oxygen, reverse=True)
        result = [a for a in astronauts if a.oxygen > 30]
        if len(result) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        return result[:5]