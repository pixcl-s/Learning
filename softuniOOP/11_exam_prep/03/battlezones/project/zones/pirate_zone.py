from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_SHIPS = 8

    def __init__(self, code: str):
        super().__init__(code, volume=self.INITIAL_SHIPS)

    def zone_info(self):
        to_return = f"@Pirate Zone Statistics@\n" \
                    f"Code: {self.code}; Volume: {self.volume}\n" \
                    f"Battleships currently in the Pirate Zone: {len(self.ships)}, " \
                    f"{len([x for x in self.ships if self.__class__.__name__ != x.FRIENDLY_ZONE])} out of them are Royal Battleships."

        if self.ships:
            the_ships = self.get_ships()
            to_return += "\n#" + ", ".join(x.name for x in the_ships) + "#"

        return to_return
