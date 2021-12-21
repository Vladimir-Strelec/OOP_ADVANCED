from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__chek_valid_car(car_type, model, speed_limit)
        if car:
            if self.__chek_obj_in_list(self.cars, car.model):
                raise Exception("Car {model} is already created!")
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)
        if self.__chek_valid_driver(self.drivers, driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)
        if self.__chek_valid_driver(self.races, race_name):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__chek_valid_driver(self.drivers, driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__chek_valid_car_type(self.cars, car_type)
        if self.__chek_valid_driver(self.drivers, driver_name):
            driver = self.__get_driver(self.drivers, driver_name)
            if driver.car is None:
                driver.car = car
                self.cars.remove(car)
                return f"Driver {driver_name} chose the car {car.model}."
            old_model = driver.car.model
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__chek_valid_driver(self.races, race_name):
            raise Exception(f"Race {race_name} could not be found!")
        if not self.__chek_valid_driver(self.drivers, driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = self.__get_driver(self.drivers, driver_name)
        race = self.__get_driver(self.races, race_name)
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__chek_valid_driver(self.races, race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = self.__get_driver(self.races, race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda d: -d.car.speed_limit)[:3]
        output = ""
        for w in winners:
            output += f"Driver {w.name} wins the {race_name} race with a speed of {w.car.speed_limit}.\n"
        return output.strip()

    @staticmethod
    def __chek_valid_car(car_type, model, speed_limit):
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)
        if car_type == "SportsCar":
            return SportsCar(model, speed_limit)
        return None

    @staticmethod
    def __chek_obj_in_list(current_list, obj_param):
        for current_obj in current_list:
            if current_obj.model == obj_param:
                return True
        return False

    @staticmethod
    def __chek_valid_driver(current_list, obj_param):
        for current_obj in current_list:
            if current_obj.name == obj_param:
                return True
        return False

    @staticmethod
    def __chek_valid_car_type(list_cars, car_type):
        for car in list_cars:
            if car.__class__.__name__ == car_type:
                if car.is_taken is True:
                    raise Exception(f"Car {car_type} could not be found!")
            if car.__class__.__name__ == car_type:

                return car

    @staticmethod
    def __get_driver(drivers, driver_name):
        for driver in drivers:
            if driver.name == driver_name:
                return driver