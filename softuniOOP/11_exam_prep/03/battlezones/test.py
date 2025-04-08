
# Initialize the BattleManager
from project.battle_manager import BattleManager

battle_manager = BattleManager()
# Add zones
print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()
# Add battleships
print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
print()
# Retrieve battleships and zones
royal_zone = battle_manager.zones[0]
pirate_zone = battle_manager.zones[1]
royal_one = battle_manager.ships[0]
royal_two = battle_manager.ships[1]
pirate_one = battle_manager.ships[2]
pirate_two = battle_manager.ships[3]
# Add ships to zones
print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
print(battle_manager.add_ship_to_zone(pirate_zone, pirate_two))
print()
# Remove a battleship
print(battle_manager.remove_battleship("RoyalTwo"))
print(battle_manager.remove_battleship("Nonexistent"))
print()
# Start battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()
# Start battle in PirateZone
print(battle_manager.start_battle(pirate_zone))
print()
# Start another battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()
# Retrieve updated statistics
print(battle_manager.get_statistics())
print()
# Remove a battleship
print(battle_manager.remove_battleship("RoyalThree"))

# output
# A zone of type RoyalZone was successfully added.
# A zone of type PirateZone was successfully added.
#
# A new RoyalBattleship was successfully added.
# A new RoyalBattleship was successfully added.
# A new PirateBattleship was successfully added.
# A new PirateBattleship was successfully added.
# A new RoyalBattleship was successfully added.
# A new PirateBattleship was successfully added.
#
# Ship RoyalOne successfully participated in zone 001.
# Ship PirateOne successfully participated in zone 001.
# Ship RoyalTwo successfully participated in zone 002.
# Ship PirateTwo successfully participated in zone 002.
#
# The ship participates in zone battles! Removal is impossible!
# No ship with this name!
#
# PirateOne lost the battle and was sunk.
#
# Both ships survived the battle.
#
# Not enough participants. The battle is canceled.
#
# Available Battleships: 2
# #RoyalThree, PirateThree#
# ***Zones Statistics:***
# Total Zones: 2
# @Royal Zone Statistics@
# Code: 001; Volume: 8
# Battleships currently in the Royal Zone: 1, 0 out of them are Pirate Battleships.
# #RoyalOne#
# @Pirate Zone Statistics@
# Code: 002; Volume: 6
# Battleships currently in the Pirate Zone: 2, 1 out of them are Royal Battleships.
# #PirateTwo, RoyalTwo#
#
# Successfully removed ship RoyalThree.
