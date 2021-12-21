from project.car.car import Car


class MuscleCar(Car):
    _MAX_SPEED = 450
    _MIN_SPEED = 250

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)


