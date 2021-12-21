from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer


class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id(ExercisePlan, ExercisePlan.id)

    @classmethod
    def from_hours(cls, trainer_id:int, equipment_id:int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @staticmethod
    def get_next_id(*args):
        if args:
            obj, x = args[:]
            x = obj.id
            obj.id += 1
            return x
        return ExercisePlan.id