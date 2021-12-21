from abc import ABC, abstractmethod


class Car(ABC):
    _MAX_SPEED = None
    _MIN_SPEED = None

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @classmethod
    def __validate_speed_limit(cls, value):
        if value < cls._MIN_SPEED or value > cls._MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {cls._MIN_SPEED} and {cls._MAX_SPEED}!")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError("Model {model} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value
