from project.the_adding import IDStuff


class Trainer(IDStuff):
    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
