from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSOR = {"AMD Ryzen 9 5950X": 900,
                           "Intel Core i9-11900H": 1050,
                           "Apple M1 Pro": 1200}
    MAX_RAM = 64

    def __str__(self):
        return "laptop"
