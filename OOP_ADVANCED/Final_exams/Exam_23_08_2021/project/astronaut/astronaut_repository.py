from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        obj = self.find_by_name(astronaut.name)
        if obj:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astr in self.astronauts:
            if astr.name == name:
                return astr
        return None
