from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super(CrossMotorcycle, self).__init__(fuel, horse_power)