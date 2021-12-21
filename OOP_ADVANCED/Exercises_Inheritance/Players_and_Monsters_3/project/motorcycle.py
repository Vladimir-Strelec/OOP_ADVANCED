from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int):
        super(Motorcycle, self).__init__(fuel, horse_power)
