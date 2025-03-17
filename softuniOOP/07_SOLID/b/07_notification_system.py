# You are developing a notification system that supports different types of notifications: Email, SMS, and Push notifications.
# The initial design has a single NotificationSender class that enforces a common interface for all notification types.
# This design violates the Interface Segregation Principle (ISP), the Open/Closed Principle (OCP), the Liskov Substitution Principle (LSP),
# and the Single Responsibility Principle (SRP).
# Some Violation Examples:
#   · EmailSender and SMSSender are required to implement the send() method, which is appropriate for them.
#   · PushSender implements send() but the functionality is currently under maintenance, so it should handle this scenario gracefully.
#   · The NotificationService class directly depends on specific notification types,
#       which violates the Open/Closed Principle (OCP) by requiring modifications to support new notification types.
# Your Tasks:
#   · Refactor the NotificationSender Class:
#       o Create a base interface, NotificationSender, that defines the common method send().
#       o Ensure that NotificationSender does not include methods that are not applicable to all notification types.
#   · Implement Concrete Notification Classes:
#       o EmailSender: Implements NotificationSender and provides functionality for sending email notifications.
#       o SMSSender: Implements NotificationSender and provides functionality for sending SMS notifications.
#       o PushSender: Implements NotificationSender and provides functionality for push notifications when the service is normally working.
#       o Handle scenarios where any service can be under maintenance. Return feedback that the service is currently unavailable.
#   · Refactor the NotificationService Class:
#       o Modify NotificationService to depend on the NotificationSender abstraction rather than specific notification implementations.
#       o Ensure that NotificationService can handle new types of notifications by accepting any object that implements NotificationSender.
#   · Handle Maintenance Status Appropriately:
#       o If a notification type is under maintenance, provide an appropriate message.

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(NotificationSender):
    def send(self, message: str):
        return print(f"Sending email with message: {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        return print(f"Sending SMS with message: {message}")


class PushSender(NotificationSender):
    def send(self, message: str):
        return print(f"Sending Push Notification with message: {message}")


class NotificationService:
    def __init__(self, sender_type: NotificationSender):
        self.sender = sender_type

    def notify(self, message: str):
        if self.sender.is_under_maintenance:
            return print("This service is currently under maintenance.")
        self.sender.send(message)


# test
email_sender = EmailSender()
sms_sender = SMSSender()
push_sender = PushSender()
push_sender.is_under_maintenance = True
"""
The status change represents manual toggling done by an admin or a developer when they know a system component
is under maintenance. In more complex systems, this would be automated or pulled from an external source.
"""
email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)
push_service = NotificationService(push_sender)
email_service.notify('Hello via email!')
sms_service.notify('Hello via SMS!')
push_service.notify('Hello via Push!')
# output
# Sending email with message: Hello via email!
# Sending SMS with message: Hello via SMS!
# This service is currently under maintenance.


# old

# from abc import ABC, abstractmethod
#
#
# class UnderMaintenanceException(Exception):
#     pass
#
#
# class NotificationSender(ABC):
#     def __init__(self):
#         self.is_under_maintenance = False
#
#     @abstractmethod
#     def send(self, message: str):
#         pass
#
#
# class EmailSender(NotificationSender):
#     def send(self, message: str):
#         print(f"Sending email with message: {message}")
#
#
# class SMSSender(NotificationSender):
#     def send(self, message: str):
#         print(f"Sending SMS with message: {message}")
#
#
# class PushSender(NotificationSender):
#     def send(self, message: str):
#         self.is_under_maintenance = True
#         raise UnderMaintenanceException('The Push Sender is under maintenance.')
#
#
# class NotificationService:
#     def __init__(self, sender_type: str):
#         if sender_type == "email":
#             self.sender = EmailSender()
#         elif sender_type == "sms":
#             self.sender = SMSSender()
#         elif sender_type == "push":
#             self.sender = PushSender()
#
#     def notify(self, message: str):
#         self.sender.send(message)
# test
# try:
#     email_service = NotificationService("email")
#     email_service.notify("Hello via email!")
#     sms_service = NotificationService("sms")
#     sms_service.notify("Hello via SMS!")
#     push_service = NotificationService("push")
#     push_service.notify("Hello via Push!")
# except UnderMaintenanceException as ex:
#     print(ex)
# output
# Sending email with message: Hello via email!
# Sending SMS with message: Hello via SMS!
# The Push Sender is under maintenance.
