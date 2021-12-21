from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.space_station import SpaceStation


space_station = SpaceStation()
a = SpaceStation()
print(a.add_astronaut("Biologist", "X"))
print(a.add_astronaut("Geodesist", "y"))
print(a.add_planet("Uran", "hernya"))
print(a.astronaut_repository.astronauts[0].oxygen)
print(a.astronaut_repository.astronauts[1].oxygen)
a.recharge_oxygen()
print(a.astronaut_repository.astronauts[0].oxygen)
print(a.astronaut_repository.astronauts[1].oxygen)
print(a.retire_astronaut("X"))

a.send_on_mission("Uran")

print(a.report())