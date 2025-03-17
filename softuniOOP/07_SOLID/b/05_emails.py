# You are provided with code containing class IEmail and class Email.
# The code does not follow the principle of single responsibility (the Email class has 2 responsibilities).
# Create a new class - IContent, and a class that inherits it called MyContent to split the responsibilities.

from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, contents):
        self.content = contents

    @abstractmethod
    def format(self):
        pass


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, contents):
        pass


class MyContent(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, contents):
        self.__content = contents.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# test
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
# output
# Sender: I'm qmal
# Receiver: I'm james
# Content:
# <MyML>Hello, there!</MyML>


# old

# from abc import ABCMeta, abstractmethod
#
# class IEmail(object):
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def set_sender(self, sender):
#         pass
#
#     @abstractmethod
#     def set_receiver(self, receiver):
#         pass
#
#     @abstractmethod
#     def set_content(self, content):
#         pass
#
# class Email(IEmail):
#     def __init__(self, protocol, content_type):
#         self.protocol = protocol
#         self.content_type = content_type
#         self.__sender = None
#         self.__receiver = None
#         self.__content = None
#
#     def set_sender(self, sender):
#         if self.protocol == 'IM':
#             self.__sender = ''.join(["I'm ", sender])
#         else:
#             self.__sender = sender
#
#     def set_receiver(self, receiver):
#         if self.protocol == 'IM':
#             self.__receiver = ''.join(["I'm ", receiver])
#         else:
#             self.__receiver = receiver
#
#     def set_content(self, content):
#         if self.content_type == 'MyML':
#             self.__content = '\n'.join(['<myML>', content, '</myML>'])
#         else:
#             self.__content = content
#
#     def __repr__(self):
#         template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
#         return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)
# test
# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)
# output
# Sender: I'm qmal
# Receiver: I'm james
# Content:
# <myML>
# Hello, there!
# </myML>
