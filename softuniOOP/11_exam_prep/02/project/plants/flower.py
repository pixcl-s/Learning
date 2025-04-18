from project.plants.base_plant import BasePlant


class Flower(BasePlant):
    BLOOMING_SEASONS = ["Spring", "Summer", "Fall", "Winter"]

    def __init__(self, name: str, price: float, water_needed: int, blooming_season: str):
        super().__init__(name, price, water_needed)
        self.blooming_season = blooming_season

    def plant_details(self):
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml," \
               f" Blooming Season: {self.blooming_season}"

    @property
    def blooming_season(self):
        return self.__blooming_season

    @blooming_season.setter
    def blooming_season(self, value):
        if value not in self.BLOOMING_SEASONS:
            raise ValueError("Blooming season must be a valid one!")
        self.__blooming_season = value

