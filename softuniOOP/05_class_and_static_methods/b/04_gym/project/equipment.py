from project.the_adding import IDStuff


class Equipment(IDStuff):
    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
