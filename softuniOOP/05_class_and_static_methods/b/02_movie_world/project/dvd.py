import calendar


class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int) -> "DVD":
        month, year = date.split(".")[1:]
        month = calendar.month_name[int(month)]

        return cls(name, _id, int(year), month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

