from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for obj in self.astronauts:
            if obj.name == name:
                return obj
        return None

    def find_astronaut_for_mission(self, count, min_oxigen):
        return sorted([x for x in self.astronauts if x.oxygen > min_oxigen], key=lambda x: x.oxygen, reverse=True)[0:count]
        