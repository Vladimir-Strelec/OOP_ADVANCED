from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.drink.tea import Tea
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

h = Bread("Seriy", 2)
print(h)
t = Tea('Cherniy', 1, "Lipton")
print(t)
i = OutsideTable(51, 3)
print(i.free_table_info())
i.reserve(2)
i.order_drink(t)
i.order_food(h)
print(i.get_bill())
b = Bakery("Hlebopekarnya")
print(b.add_food("Bread", "Seriy", 10.10))
print(b.add_drink("Water", "Bonakua", 10, "Super"))
b.add_table("InsideTable", 2, 2)
print(b.reserve_table(2))
print(b.order_food(2, "Hleb"))
