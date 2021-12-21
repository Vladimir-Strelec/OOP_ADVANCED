from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.fish.freshwater_fish import FreshwaterFish

o = Ornament()
rep = DecorationRepository()
rep.add(o)
# print(rep.remove(o))
print(rep.find_by_type('Ornament'))
f = FreshwaterFish("Karas", "FreshwaterFish", 10)
k = FreshwaterFish("Karp", "FreshwaterFish", 13)
aq = FreshwaterAquarium("AQUA-BIG")
# print(aq.add_fish(f))
# print(aq.add_fish(k))
aq.add_decoration(o)
print(aq)
c = Controller()
c.add_aquarium("FreshwaterAquarium", "AQUA-BIG")
c.decorations_repository.add(o)
print(c.insert_decoration("AQUA-BIG", "Ornament"))
print(c.add_fish("AQUA-BIG", 'FreshwaterFish', 'Alina', "Karp", 10))
print(c.feed_fish("AQUA-BIG"))
print(c.calculate_value("AQUA-BIG"))
print(c.report())