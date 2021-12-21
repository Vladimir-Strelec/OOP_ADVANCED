from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        obj = self.find_by_name(planet.name)
        if obj:
            self.planets.remove(obj)

    def find_by_name(self, name: str):
        for plnt in self.planets:
            if plnt.name == name:
                return plnt
        return None