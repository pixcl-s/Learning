from typing import List, Union
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plan: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def adding(the_list: List, the_element: Union[Customer, Trainer, Equipment, ExercisePlan, Subscription]) -> None:
        if the_element not in the_list:
            the_list.append(the_element)

    @staticmethod
    def the_one(the_list, the_id):
        the_one = next((x for x in the_list if x.id == the_id), None)
        return the_one

    def add_customer(self, customer: Customer):
        self.adding(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.adding(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.adding(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.adding(self.plan, plan)

    def add_subscription(self, subscription: Subscription):
        self.adding(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        the_stuff = [self.subscriptions, self.customers, self.trainers, self.equipment, self.plan]
        to_return = ""

        for x in the_stuff:
            to_return += f"{self.the_one(x, subscription_id)}" + "\n"

        return to_return
