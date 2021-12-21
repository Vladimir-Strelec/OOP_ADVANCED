from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist

# b = Biologist("lol")
# r = AstronautRepository()
# r.add(b)
# r.remove(b)
# print(r.astronauts)
from project.space_station import SpaceStation

s = SpaceStation()

s.add_astronaut("Biologist", "Vova")
s.add_astronaut("Geodesist", "Anton")
s.add_astronaut("Biologist", "Volk")
s.add_astronaut("Biologist", "V")
s.add_astronaut("Biologist", "olk")
s.add_astronaut("Biologist", "lk")
s.add_planet("Vinera", "Granit, shibenka, galka")
s.send_on_mission("Vinera")
print(s.report())