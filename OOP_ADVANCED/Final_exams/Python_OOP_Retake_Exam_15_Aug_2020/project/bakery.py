from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    _VALID_FOOD = ["Bread", "Cake"]
    _VALID_DRINK = ["Tea", "Water"]

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            ValueError("Name cannot be empty string or white space!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food = self.__create_food(food_type, name, price)
        return self.__chek_food_in_menu(self.food_menu, food, food_type)

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        drink = self.__create_drink(drink_type, name, portion, brand)
        return self.__chek_drink_in_menu(self.drinks_menu, drink, drink_type)

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.__get_current_table(table_type, table_number, capacity)
        return self.__check_ob_in_list(self.tables_repository, table)

    def reserve_table(self, number_of_people: int):
        return self.__get_free_table(self.tables_repository, number_of_people)

    def __get_table_by_number(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        return table[0] if table else None

    def order_food(self, table_number: int, *args):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        product_in_args = [pr for pr in args]
        food_names = [n.name for n in self.food_menu]
        product_in_menu = [pr for pr in product_in_args if pr in food_names]
        product_not_in_menu = [pr for pr in product_in_menu if pr not in food_names]
        product = [self.get_food_by_name(p) for p in product_in_menu]
        [table.order_food(b) for b in product]

        ordered_foods_str = "\n".join([repr(i) for i in product])
        missed_foods_str = "\n".join([i for i in product_not_in_menu])
        return f'''Table {table_number} ordered:
{ordered_foods_str}
{self.name} does not have in the menu:
{missed_foods_str}'''


    def order_drink (self, table_number: int, drinks_name1: str, drink_name2: str):
        pass

    def leave_table (self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass

    @staticmethod
    def __create_food(food_type, name, price):
        if food_type == Bakery._VALID_FOOD[0]:
            return Bread(name, price)
        elif food_type == Bakery._VALID_FOOD[1]:
            return Cake(name, price)
        return None

    @staticmethod
    def __create_drink(drink_type, name, portion, brand):
        if drink_type == Bakery._VALID_DRINK[0]:
            return Tea(name, portion, brand)
        elif drink_type == Bakery._VALID_DRINK[1]:
            return Water(name, portion, brand)
        return None

    def __check_ob_in_list(self, tables_repository, table):
        for t in tables_repository:
            if t.table_number == table.table_number:
                raise Exception(f"Table {table.number} is already in the bakery!")
        self.tables_repository.append(table)
        return f"Added table number {table.table_number} in the bakery"

    @staticmethod
    def __get_current_table(table_type, table_number, capacity):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)
        return None

    @staticmethod
    def __get_free_table(table_repository, number_of_people):
        for t in table_repository:
            if not t.is_reserved and t.capacity <= number_of_people:
                t.reserve(number_of_people)
                return f"Table {t.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def __chek_drink_in_menu(self, drinks_menu, drink, drink_type):
        for d in drinks_menu:
            if d.name == drink.name:
                raise Exception(f"{drink_type} {drink.name} is already in the menu!")
        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.__class__.__name__}) to the drink menu"

    def __chek_food_in_menu(self, food_menu, food, food_type):
        for f in food_menu:
            if f.name == food.name:
                raise Exception(f"{food_type} {f.name} is already in the menu!")
        self.food_menu.append(food)
        return f"Added {food.name} ({food.__class__.__name__}) to the food menu"

    def get_food_by_name(self, p):
        food = [f for f in self.food_menu if f.name == p]
        return food[0] if food else None