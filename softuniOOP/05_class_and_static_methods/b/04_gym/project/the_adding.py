

class IDStuff:
    id = 0

    @classmethod
    def get_next_id(cls):
        cls.id += 1
        return cls.id
