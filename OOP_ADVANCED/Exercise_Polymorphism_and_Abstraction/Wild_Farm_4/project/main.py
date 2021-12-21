from project.animals.birds import Owl, Hen
from project.animals.mammals import Cat
from project.food import Meat, Vegetable, Fruit

cat = Cat("Pip", 10, 10)
print(cat)
meat = Meat(4)
print(cat.make_sound())
cat.feed(meat)
veg = Vegetable(1)
print(cat.feed(veg))
print(cat)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)