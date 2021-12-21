from project.car.car import Car


class SportsCar(Car):
    _MAX_SPEED = 600
    _MIN_SPEED = 400

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)


