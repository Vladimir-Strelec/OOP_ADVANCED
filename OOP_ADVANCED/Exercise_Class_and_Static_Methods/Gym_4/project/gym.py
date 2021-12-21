

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if not Gym.__get_chek_id(self.customers, customer.id):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not Gym.__get_chek_id(self.trainers, trainer.id):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not Gym.__get_chek_id(self.equipment, equipment.id):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not Gym.__get_chek_id(self.plans, plan.id):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not Gym.__get_chek_id(self.subscriptions, subscription.id):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = []
        result.append(Gym.__get_chek_id(self.subscriptions, subscription_id))
        result.append(Gym.__get_chek_id(self.customers, subscription_id))
        result.append(Gym.__get_chek_id(self.trainers, subscription_id))
        result.append(Gym.__get_chek_id(self.equipment, subscription_id))
        result.append(Gym.__get_chek_id(self.plans, subscription_id))
        result_str = "\n".join([str(x) for x in result])
        return result_str

    @staticmethod
    def __get_chek_id(current_list, current_id):
        for obj in current_list:
            if obj.id == current_id:
                return obj

