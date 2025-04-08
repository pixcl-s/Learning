from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    BASE_AMMUNITION = 80
    FRIENDLY_ZONE = "PirateZone"

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=self.BASE_AMMUNITION)

    def attack(self):
        self.ammunition -= 10
