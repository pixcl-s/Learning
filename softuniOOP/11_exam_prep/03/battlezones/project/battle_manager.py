from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}

        if zone_type not in VALID_ZONES:
            raise Exception("Invalid zone type!")

        existing_zone = next((x for x in self.zones if x.code == zone_code), None)
        if existing_zone:
            raise Exception("Zone already exists!")

        self.zones.append(VALID_ZONES[zone_type](zone_code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        VALID_SHIPS = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

        if ship_type not in VALID_SHIPS:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(VALID_SHIPS[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume:
            if ship.health > 0:
                if ship.is_available:
                    if ship.FRIENDLY_ZONE == zone.__class__.__name__:
                        ship.is_attacking = True
                    else:
                        ship.is_attacking = False

                    zone.ships.append(ship)
                    ship.is_available = False
                    zone.volume -= 1

                    return f"Ship {ship.name} successfully participated in zone {zone.code}."
                return f"Ship {ship.name} is not available and could not participate!"
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        return f"Zone {zone.code} does not allow more participants!"

    def remove_battleship(self, ship_name: str):
        existing_ship = next((x for x in self.ships if x.name == ship_name), None)
        if existing_ship:
            if existing_ship.is_available:
                self.ships.remove(existing_ship)
                return f"Successfully removed ship {existing_ship.name}."
            return "The ship participates in zone battles! Removal is impossible!"
        return "No ship with this name!"

    def start_battle(self, zone: BaseZone):
        ship_status = self._ship_sorting(zone)
        if ship_status["True"] and ship_status["False"]:
            attacker = max([x for x in ship_status["True"]], key= lambda ship: ship.hit_strength)
            defender = max([x for x in ship_status["False"]], key= lambda ship: ship.health)
            attacker.attack()
            defender.take_damage(attacker)

            if defender.health == 0:
                zone.ships.remove(defender)
                self.ships.remove(defender)
                return f"{defender.name} lost the battle and was sunk."

            if attacker.ammunition == 0:
                zone.ships.remove(attacker)
                self.ships.remove(attacker)
                return f"{attacker.name} ran out of ammunition and leaves."

            return "Both ships survived the battle."

        return "Not enough participants. The battle is canceled."

    def get_statistics(self):
        available_ships = [x for x in self.ships if x.is_available]
        to_return = f"Available Battleships: {len(available_ships)}\n"
        if available_ships:
            to_return += "#" + ", ".join(x.name for x in available_ships) + "#\n"

        to_return += f"***Zones Statistics:***\n" \
                     f"Total Zones: {len(self.zones)}\n"

        to_return += "\n".join([x.zone_info() for x in self.zones])

        return to_return

    @staticmethod
    def _ship_sorting(zone):
        ships = {"True": [], "False": []}
        for x in zone.ships:
            ships[str(x.is_attacking)].append(x)
        return ships
