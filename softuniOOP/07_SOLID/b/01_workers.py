# You are provided with a code on which you have to apply the DIP (Dependency Inversion Principle)
# so that when adding new worker classes, the Manager class will work properly.

from abc import ABC, abstractmethod


class TheWorkers(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(TheWorkers):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(TheWorkers):
    @staticmethod
    def work():
        print("I work very hard!!!")


class OverworkedWorker(TheWorkers):
    @staticmethod
    def work():
        print("Work is da poop. Too hard, make me tired. Life sad.\nBut then, burger. Birger worth it.")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, workers: TheWorkers):
        assert isinstance(workers, TheWorkers), f'`worker` must be of type {TheWorkers}'
        self.worker = workers

    def manage(self):
        if self.worker is not None:
            self.worker.work()


# test
worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
# output
# I'm working!!
# I work very hard!!!

lazy_w = OverworkedWorker()
manager.set_worker(lazy_w)
manager.manage()


# old

# class Worker:
#
#     def work(self):
#         print("I'm working!!")
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)
#
#         self.worker = worker
#
#     def manage(self):
#         if self.worker is not None:
#             self.worker.work()
#
# class SuperWorker:
#
#     def work(self):
#         print("I work very hard!!!")
#
# # test
# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
# super_worker = SuperWorker()
# try:
#     manager.set_worker(super_worker)
# except AssertionError:
#     print("manager fails to support super_worker....")
# output
# I'm working!!
# manager fails to support super_worker....
