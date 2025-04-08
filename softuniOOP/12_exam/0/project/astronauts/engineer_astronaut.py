from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    SPECIALIZATION = "EngineerAstronaut"
    STAMINA = 80
    STAMINA_PER_TRAIN_SESSION = 5

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization=self.SPECIALIZATION, stamina=self.STAMINA)

    def train(self):
        stamina = self.stamina + self.STAMINA_PER_TRAIN_SESSION

        self.stamina = stamina if stamina <= self.MAX_STAMINA else 100
