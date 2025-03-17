# You are building a simple payment processing system for an e-commerce application.
# The current system (the provided code) has a single Order class that handles multiple responsibilities:
# managing order items, calculating the total price, and processing payments for different payment methods
# like Credit Card and PayPal. This design does not adhere to key architecture principles, specifically
# the Single Responsibility Principle (SRP), the Open/Closed Principle (OCP), and the Dependency Inversion Principle (DIP).
# Your Tasks:
#   · Create a PaymentMethod Interface (Abstract Base Class):
#       o Define an interface or abstract base class for processing payments.
#       o This class should have a method that all concrete payment method classes must implement.
#           § The method should define the contract for payment processing.
#   · Create a PaymentProcessor class:
#       o Define a class that accepts a PaymentMethod object.
#       o Implement a method that processes payments using the provided PaymentMethod object for a given Order.
#   · Implement concrete payment classes:
#       o CreditCardPayment class that handles credit card payment processing.
#       o PayPalPayment class that handles PayPal payment processing.
#           § Each class should implement the PaymentMethod interface.
#   · Refactor the Order class:
#       o Remove any payment processing logic from the Order class.
#       o Modify the Order class to use the PaymentProcessor class to process payments.
#       o Ensure that the Order class depends on the PaymentMethod interface rather than specific payment classes,
#           adhering to the Dependency Inversion Principle (DIP) by depending on an abstraction.
# By the end of this task, your system should be designed to easily accommodate new payment methods by implementing
# new classes that follow the PaymentMethod interface.
# The Order class should not need modification when new payment methods are introduced, ensuring adherence to both
# the Open/Closed Principle (OCP) and Dependency Inversion Principle (DIP).

from abc import ABC, abstractmethod
from typing import List, Tuple


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f'Processing credit card payment for ${amount}')


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f'Processing paypal payment for ${amount}')


class PaymentProcessor:
    def __init__(self, pay_process: PaymentMethod):
        self.pay_process = pay_process

    def process_payment(self, the_order: "Order"):
        total_amount = the_order.calculate_total()
        self.pay_process.pay(total_amount)


class Order:
    def __init__(self, items: List[Tuple[str, int, float]]):
        self.items = items

    def calculate_total(self) -> float:
        return sum(quantity * price for _, quantity, price in self.items)


# test
order_obj = Order([('Apple', 2, 1.0), ('Banana', 5, 0.5)])
credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)
# output
# Processing credit card payment for $4.5


# old

# from typing import List, Tuple
# class Order:
#     def __init__(self, items: List[Tuple[str, int, float]]):
#         """
#         Initialize an Order with a list of items.
#
#         Args:
#         items (List[Tuple[str, int, float]]): A list where each tuple represents an item in the order.
#             Each tuple contains:
#                 - item_name (str): The name of the item.
#                 - quantity (int): The number of units of the item.
#                 - price_per_unit (float): The price of a single unit of the item.
#
#         Example:
#         items = [
#             ("apple", 2, 0.5),  # 2 apples, each costing $0.5
#             ("banana", 5, 0.3), # 5 bananas, each costing $0.3
#         ]
#         """
#         self.items = items
#
#     def calculate_total(self) -> float:
#         """
#         Calculate the total price of all items in the order.
#
#         Returns:
#         float: The total price of the order.
#         """
#         return sum(quantity * price for _, quantity, price in self.items)
#
#     def process_payment(self, payment_type: str) -> None:
#         """
#         Process the payment based on the payment type.
#
#         Args:
#         payment_type (str): The type of payment (e.g., 'credit_card', 'paypal').
#         """
#         total_amount = self.calculate_total()
#
#         if payment_type == 'credit_card':
#             print(f'Processing credit card payment for ${total_amount}')
#         elif payment_type == 'paypal':
#             print(f'Processing PayPal payment for ${total_amount}')
#         else:
#             print('Unsupported payment type.')

# test
# order_obj = Order([('Apple', 2, 1.0), ('Banana', 5, 0.5)])
# order_obj.process_payment('credit_card')
# output
# Processing credit card payment for $4.5
