# Class Customer
# Upon initialization, each customer will receive the following parameters: name: str, address: str, email: str.
# Each customer should also have a personal id (autoincremented, starting from 1). To do the incrementation, you should create a class attribute id equal to 1, 
# which will keep the value of the id for the upcoming customer. For example, if there are no customers, the class id should be equal to 1. When there is one customer - the class id should be equal to 2.
# Create a method called get_next_id, which returns the id that will be given to the next customer.
# Implement the __repr__ method so it returns the info about the customer in the following format: "Customer <{id}> {name}; Address: {address}; Email: {email}"
# Class Equipment
# Upon initialization, the class will receive the following parameters: name: str. Each equipment should also have an id (autoincremented, starting from 1).
# To do the incrementation, you should create a class attribute id equal to 1, which will keep the value of the id for the following equipment's id.
# Create a method called get_next_id, which returns the id that will be given to the following equipment.
# Implement the __repr__ method so it returns the info about the equipment in the following format: "Equipment <{id}> {name}"
# Create a static method called get_next_id, which returns the id that will be given to the following equipment.
# Class ExercisePlan
# Upon initialization, the class will receive the following parameters: trainer_id: int, equipment_id: int, duration: int (in minutes).
# Each plan should also have an id (autoincremented, starting from 1). To do the incrementation, you should create a class attribute id equal to 1, 
# which will keep the value of the id for the next plan's id. Create the following methods:
#   · from_hours(trainer_id:int, equipment_id:int, hours:int) - creates new instance using the provided information
#   · get_next_id() - static method that returns the id that will be given to the next plan
#   · __repr__() - returns the information about the plan in the following format: "Plan <{id}> with duration {duration} minutes"
# Class Subscription
# Upon initialization, the class will receive the following parameters: date: str, customer_id: int, trainer_id: int, exercise_id: int. The class should also have an id (autoincremented starting from 1). 
# To do the incrementation, you should create a class attribute id equal to 1, which will keep the value of the id for the next subscription's id.
# Implement the __repr__ method so it returns the info about the subscription in the following format: "Subscription <{id}> on {date}"
# Create a static method called get_next_id which returns the id that will be given to the next subscription
# Class Trainer
# Upon initialization, the class will receive the following parameters: name: str. The class should also have an id (autoincremented starting from 1). To do the incrementation, 
# you should create a class attribute id equal to 1, which will keep the value of the id for the next trainer's id.
# Implement the __repr__ method so it returns the info about the trainer in the following format: "Trainer <{id}> {name}"
# Create a static method called get_next_id, which returns the id that will be given to the next trainer.
# Class Gym
# Upon initialization, the class will not receive any parameters. However, it should have the following attributes: customers (empty list of customer objects), trainers (empty list of trainer objects), 
# equipment (empty list of equipment objects), plans (empty list of plan objects), subscriptions (empty list of subscription objects)
# Create the following methods:
#   · add_customer(customer: Customer) - add the customer to the customer list if the customer is not already in it
#   · add_trainer(trainer: Trainer) - add the trainer to the trainers' list, if the trainer is not already in it
#   · add_equipment(equipment: Equipment) - add the equipment to the equipment list, if the equipment is not already in it
#   · add_plan(plan: ExercisePlan) - add the plan to the plans' list, if the plan is not already in it
#   · add_subscription(subscription: Subscription) - add the subscription in the subscriptions list if the subscription is not already in it
#   · subscription_info(subscription_id: int) - get the subscription, the customer, the trainer, the equipment, and the plan. Then return their string representations each on a new line.

# test
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)
gym = Gym()
gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)
print(Customer.get_next_id())
print(gym.subscription_info(1))

# 86/100
# output
# 2
# Subscription <1> on 14.05.2020
# Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
# Trainer <1> Peter
# Equipment <1> Treadmill
# Plan <1> with duration 20 minutes
#
# from project.customer import Customer
# from project.equipment import Equipment
# from project.exercise_plan import ExercisePlan
# from project.gym import Gym
# from project.subscription import Subscription
# from project.trainer import Trainer
#
# # import unittest
# #
# #
# class TestGym(unittest.TestCase):
#     def test_customer_init(self):
#         Customer.id = 1
#         c = Customer("Pesho", "addr.", "pesho@gmail.com")
#         self.assertEqual(c.id, 1)
#         self.assertEqual(c.name, "Pesho")
#         self.assertEqual(c.address, "addr.")
#         self.assertEqual(c.email, "pesho@gmail.com")
#
#     def test_customer_repr(self):
#         Customer.id = 1
#         c = Customer("Pesho", "addr.", "pesho@gmail.com")
#         self.assertEqual(str(c), "Customer <1> Pesho; Address: addr.; Email: pesho@gmail.com")
#
#     def test_equipment_init(self):
#         Equipment.id = 1
#         e = Equipment("Pesho")
#         self.assertEqual(e.id, 1)
#         self.assertEqual(e.name, "Pesho")
#
#     def test_equipment_repr(self):
#         Equipment.id = 1
#         e = Equipment("Pesho")
#         self.assertEqual(str(e), "Equipment <1> Pesho")
#
#     def test_trainer_init(self):
#         Trainer.id = 1
#         t = Trainer("Pesho")
#         self.assertEqual(t.id, 1)
#         self.assertEqual(t.name, "Pesho")
#
#     def test_trainer_repr(self):
#         Trainer.id = 1
#         t = Trainer("Pesho")
#         self.assertEqual(str(t), "Trainer <1> Pesho")
#
#     def test_subscription_init(self):
#         Subscription.id = 1
#         s = Subscription("20.02.2020", 1, 1, 1)
#         self.assertEqual(s.id, 1)
#         self.assertEqual(s.date, "20.02.2020")
#         self.assertEqual(s.customer_id, 1)
#         self.assertEqual(s.trainer_id, 1)
#         self.assertEqual(s.exercise_id, 1)
#
#     def test_plan_init(self):
#         ExercisePlan.id = 1
#         p = ExercisePlan(1, 1, 10)
#         self.assertEqual(p.id, 1)
#         self.assertEqual(p.trainer_id, 1)
#         self.assertEqual(p.equipment_id, 1)
#         self.assertEqual(p.duration, 10)
#
#     def test_plan_from_hours(self):
#         ExercisePlan.id = 1
#         p = ExercisePlan.from_hours(1, 1, 16)
#         self.assertEqual(p.id, 1)
#         self.assertEqual(p.trainer_id, 1)
#         self.assertEqual(p.equipment_id, 1)
#         self.assertEqual(p.duration, 960)
#
#     def test_plan_repr(self):
#         ExercisePlan.id = 1
#         p = ExercisePlan(1, 1, 15)
#         self.assertEqual(str(p), "Plan <1> with duration 15 minutes")
#
#     def test_gym_init(self):
#         g = Gym()
#         self.assertEqual(g.customers, [])
#         self.assertEqual(g.trainers, [])
#         self.assertEqual(g.equipment, [])
#         self.assertEqual(g.plans, [])
#         self.assertEqual(g.subscriptions, [])
#
#     def test_gym_add_customer(self):
#         Gym.id = 1
#         g = Gym()
#         c = Customer("Pesho", "addr.", "pesho@gmail.com")
#         g.add_customer(c)
#         g.add_customer(c)
#         self.assertEqual(g.customers, [c])
#
#     def test_gym_add_trainer(self):
#         g = Gym()
#         t = Trainer("Pesho")
#         g.add_trainer(t)
#         g.add_trainer(t)
#         self.assertEqual(g.trainers, [t])
#
#     def test_gym_add_equipment(self):
#         g = Gym()
#         e = Equipment("Pesho")
#         g.add_equipment(e)
#         g.add_equipment(e)
#         self.assertEqual(g.equipment, [e])
#
#     def test_gym_add_plan(self):
#         g = Gym()
#         p = ExercisePlan(1, 1, 10)
#         g.add_plan(p)
#         g.add_plan(p)
#         self.assertEqual(g.plans, [p])
#
#     def test_gym_add_subscription(self):
#         g = Gym()
#         s = Subscription("10.02.2020", 1, 1, 1)
#         g.add_subscription(s)
#         g.add_subscription(s)
#         self.assertEqual(g.subscriptions, [s])
#
#     def test_gym_subscription_info(self):
#         Gym.id = 1
#         Subscription.id = 1
#         ExercisePlan.id = 1
#         Equipment.id = 1
#         Trainer.id = 1
#         Customer.id = 1
#         g = Gym()
#         s = Subscription("10.02.2020", 1, 1, 1)
#         p = ExercisePlan(1, 1, 10)
#         e = Equipment("Pesho")
#         t = Trainer("Pesho")
#         c = Customer("Pesho", "addr.", "pesho@gmail.com")
#         g.add_subscription(s)
#         g.add_customer(c)
#         g.add_equipment(e)
#         g.add_plan(p)
#         g.add_trainer(t)
#         self.assertEqual(g.subscription_info(1).strip(),
#                          "Subscription <1> on 10.02.2020\nCustomer <1> Pesho; Address: addr.; Email: pesho@gmail.com\nTrainer <1> Pesho\nEquipment <1> Pesho\nPlan <1> with duration 10 minutes")
#
#     def test_customer_static_method(self):
#         Customer.id = 1
#         self.assertEqual(Customer.get_next_id(), 1)
#
#     def test_equipment_static_method(self):
#         Equipment.id = 1
#         self.assertEqual(Equipment.get_next_id(), 1)
#
#     def test_trainer_static_method(self):
#         Trainer.id = 1
#         self.assertEqual(Trainer.get_next_id(), 1)
#
#     def test_subscription_static_method(self):
#         Subscription.id = 1
#         self.assertEqual(Subscription.get_next_id(), 1)
#
#     def test_plan_static_method(self):
#         ExercisePlan.id = 1
#         self.assertEqual(ExercisePlan.get_next_id(), 1)
#
#
# if __name__ == "__main__":
#     unittest.main()
