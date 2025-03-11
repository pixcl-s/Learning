
class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for x in self.workers:
            if x.name == worker_name:
                self.workers.remove(x)
                return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_needed = 0
        for x in self.workers:
            money_needed += x.salary

        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum(animal.money_for_care for animal in self.animals)

        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        to_return = f"You have {len(self.animals)} animals"

        the_animals = {"lion": [], "tiger": [], "cheetah": []}

        for y in self.animals:
            the_animals[y.__class__.__name__.lower()].append(y)

        to_return += f"\n----- {len(the_animals['lion'])} Lions:"
        for z in the_animals["lion"]:
            to_return += f"\n{z}"

        to_return += f"\n----- {len(the_animals['tiger'])} Tigers:"
        for z in the_animals['tiger']:
            to_return += f"\n{z}"

        to_return += f"\n----- {len(the_animals['cheetah'])} Cheetahs:"
        for z in the_animals['cheetah']:
            to_return += f"\n{z}"

        return to_return

    def workers_status(self):
        to_return = f"You have {len(self.workers)} workers"

        the_workers = {"keeper": [], "caretaker": [], "vet": []}

        for y in self.workers:
            the_workers[y.__class__.__name__.lower()].append(y)

        to_return += f"\n----- {len(the_workers['keeper'])} Keepers:"
        for z in the_workers['keeper']:
            to_return += f"\n{z}"

        to_return += f"\n----- {len(the_workers['caretaker'])} Caretakers:"
        for z in the_workers['caretaker']:
            to_return += f"\n{z}"

        to_return += f"\n----- {len(the_workers['vet'])} Vets:"
        for z in the_workers['vet']:
            to_return += f"\n{z}"

        return to_return


# def animal_status(self):
#     return self.__status(self.animals, "Lion", "Tiger", "Cheetah")
#
# def worker_status(self):
#     return self.__status(self.workers, "Keeper", "Caretaker", "Cheetah")
#
# def __status(self, category: List[Union[Animal, Worker]], *args):
#     elements = {arg: [] for arg in args}
#     for element in category:
#         elements[element.__class__.__name__].append(repr(element))
#
#     result = [f"You have {len(category)} {str(category[0].__class__.__bases__[0].__name__).lower()}s"]
#     for key in args:
#         value = elements[key]
#         result.append(f"----- {len(value)} {key}s:")
#         result.extend(value)
#
#     return "\n".join(result)
