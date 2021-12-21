from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, km):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def drive(self, km):
        self.fuel_consumption += 0.9
        if self.fuel_consumption * km < self.fuel_quantity:
            self.fuel_quantity -= self.fuel_consumption * km
        return

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, km):
        self.fuel_consumption += 1.6
        if self.fuel_consumption * km < self.fuel_quantity:
            self.fuel_quantity -= self.fuel_consumption * km
        return

    def refuel(self, fuel):
        fuel = fuel * 0.95
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)