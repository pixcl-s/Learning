# Create an instance of the Space Agency Manager
from project.space_agency import SpaceAgency

manager = SpaceAgency()
# Add astronauts (engineers & scientists)
print(manager.add_astronaut("EngineerAstronaut", "02345", 780_000.0))
print(manager.add_astronaut("EngineerAstronaut", "1234", 500_000.0))
print(manager.add_astronaut("EngineerAstronaut", "789123", 800_000.0))
print(manager.add_astronaut("EngineerAstronaut", "45678999", 702_000.0))
print(manager.add_astronaut("ScientistAstronaut", "321654", 401_000.0))
print(manager.add_astronaut("ScientistAstronaut", "6543211", 490_000.0))
print(manager.add_astronaut("ScientistAstronaut", "334654", 600_000.0))
print(manager.add_astronaut("ScientistAstronaut", "034654", 395_000.0))
print()
# Add stations
print(manager.add_station("MaintenanceStation", "Lunar-Base"))
print(manager.add_station("ResearchStation", "ISS-3"))
print(manager.add_station("ResearchStation", "Mars-Habitat"))
print()
# Assign astronauts to stations
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
print(manager.assign_astronaut("Lunar-Base", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
print()
# Conduct training sessions
print(manager.train_astronauts(manager.stations[0], 0))
print(manager.train_astronauts(manager.stations[0], 1))
print(manager.train_astronauts(manager.stations[0], 2))
print(manager.train_astronauts(manager.stations[0], 3))
print(manager.train_astronauts(manager.stations[0], 3))
print(manager.train_astronauts(manager.stations[1], 0))
print(manager.train_astronauts(manager.stations[2], 1))
print()
# Retire an astronaut
print(manager.retire_astronaut(manager.stations[2], "334654"))
print(manager.retire_astronaut(manager.stations[0], "02345"))
print(manager.stations[0].astronauts[0].id_number, manager.stations[0].astronauts[0].stamina)
print(manager.retire_astronaut(manager.stations[0], "111111"))
print(manager.retire_astronaut(manager.stations[1], "45678999"))
print()
# Perform an agency-wide update
print(manager.agency_update(500_000.0))
print()
# Check astronaut salaries after the update
print(manager.stations[0].astronauts[0].salary)
print(manager.stations[0].astronauts[1].salary)
print(manager.stations[0].astronauts[2].salary)
print()
print(manager.stations[1].astronauts[0].salary)
print(manager.stations[1].astronauts[1].salary)
print(manager.stations[1].astronauts[2].salary)
print()
print(manager.astronauts[0].salary)

# output
# 02345 is successfully hired as EngineerAstronaut.
# 1234 is successfully hired as EngineerAstronaut.
# 789123 is successfully hired as EngineerAstronaut.
# 45678999 is successfully hired as EngineerAstronaut.
# 321654 is successfully hired as ScientistAstronaut.
# 6543211 is successfully hired as ScientistAstronaut.
# 334654 is successfully hired as ScientistAstronaut.
# 034654 is successfully hired as ScientistAstronaut.
#
# Lunar-Base is successfully added as a MaintenanceStation.
# ISS-3 is successfully added as a ResearchStation.
# Mars-Habitat is successfully added as a ResearchStation.
#
# 02345 was assigned to Lunar-Base.
# 1234 was assigned to Lunar-Base.
# 321654 was assigned to Lunar-Base.
# 6543211 was assigned to ISS-3.
# 334654 was assigned to ISS-3.
# 789123 was assigned to ISS-3.
# 45678999 was assigned to ISS-3.
#
# Lunar-Base astronauts have 230 total stamina after 0 training session/s.
# Lunar-Base astronauts have 243 total stamina after 1 training session/s.
# Lunar-Base astronauts have 269 total stamina after 2 training session/s.
# Lunar-Base astronauts have 288 total stamina after 3 training session/s.
# Lunar-Base astronauts have 297 total stamina after 3 training session/s.
# ISS-3 astronauts have 300 total stamina after 0 training session/s.
# Mars-Habitat astronauts have 0 total stamina after 1 training session/s.
#
# The retirement process was canceled.
# The retirement process was canceled.
# 02345 100
# The retirement process was canceled.
# Retired astronaut 45678999.
#
# *Space Agency Up-to-Date Report*
# Total number of available astronauts: 1
# **Stations count: 3; Total available capacity: 7**
# Station name: ISS-3; Astronauts: 334654 #6543211 #789123; Total salaries: 1895000.00
# Station name: Lunar-Base; Astronauts: 02345 #1234 #321654; Total salaries: 1684000.00
# Station name: Mars-Habitat; Astronauts: N/A; Total salaries: 0.00
#
# 780000.0
# 503000.0
# 401000.0
#
# 495000.0
# 600000.0
# 800000.0
#
# 395000.0
