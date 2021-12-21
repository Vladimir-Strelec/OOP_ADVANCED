from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission = 0
        self.failed_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__create_astronaut(astronaut_type, name)
        if self.astronaut_repository.find_by_name(name):
            return f"{astronaut.name} is already added."

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        remove_obj = self.astronaut_repository.find_by_name(name)
        if remove_obj is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(remove_obj)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for current_obj in self.astronaut_repository.astronauts:
            current_obj.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:

            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.find_astronaut_for_mission(5, 30)
        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        participated_astronauts = 0
        for astronaut in astronauts:
            if len(planet.items) == 0:
                break

            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if len(planet.items) == 0:
            self.successful_mission += 1
            return f"Planet: {planet.name} was explored. {participated_astronauts} astronauts participated in collecting items."
        self.failed_mission += 1
        return f"Mission is not completed."

    def report(self):
        result = f"{self.successful_mission} successful missions!" + "\n"
        result += f"{self.failed_mission} missions were not completed!" + "\n"
        result += f"Astronauts' info:" + "\n"

        for a in self.astronaut_repository.astronauts:
            result += str(a) + '\n'

        return result.strip()

    def __create_astronaut(self, astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception('Astronaut type is not valid!')



