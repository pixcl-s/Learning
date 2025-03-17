# You are provided with a code on which you have to apply the ISP (Interface Segregation Principle)
# by splitting the Worker class into two classes (Workable and Eatable),
# so the Robot class no longer needs to implement the eat method

from abc import ABC, abstractmethod
import time


class NonHumanWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class HumanWorker(NonHumanWorker):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(HumanWorker):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(HumanWorker):
    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(NonHumanWorker):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class Managing(ABC):
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, NonHumanWorker), f"`worker` must be of type {NonHumanWorker}"
        self.worker = worker


class WorkManager(Managing):
    def manage(self):
        self.worker.work()


class BreakManager(Managing):
    def lunch_break(self):
        self.worker.eat()


# test
work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
# output
# I'm normal worker. I'm working.
# Lunch break....(5 secs)
# I'm super worker. I work very hard!
# Lunch break....(3 secs)
# I'm a robot. I'm working....


# old

# from abc import ABCMeta, abstractmethod
# import time
#
# class AbstractWorker:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Worker(AbstractWorker):
#
#     def work(self):
#         print("I'm normal worker. I'm working.")
#
#     def eat(self):
#         print("Lunch break....(5 secs)")
#         time.sleep(5)
#
# class SuperWorker(AbstractWorker):
#
#     def work(self):
#         print("I'm super worker. I work very hard!")
#
#     def eat(self):
#         print("Lunch break....(3 secs)")
#         time.sleep(3)
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)
#
#         self.worker = worker
#
#     def manage(self):
#         self.worker.work()
#
#     def lunch_break(self):
#         self.worker.eat()
#
# class Robot(AbstractWorker):
#
#     def work(self):
#         print("I'm a robot. I'm working....")
#
#     def eat(self):
#         print("I don't need to eat....")

# test
# manager = Manager()
# manager.set_worker(Worker())
# manager.manage()
# manager.lunch_break()
# manager.set_worker(SuperWorker())
# manager.manage()
# manager.lunch_break()
# manager.set_worker(Robot())
# manager.manage()
# manager.lunch_break()
# output
# I'm normal worker. I'm working.
# Lunch break....(5 secs)
# I'm super worker. I work very hard!
# Lunch break....(3 secs)
# I'm a robot. I'm working....
# I don't need to eat....
