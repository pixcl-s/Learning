from vehicle import Vehicle
from unittest import TestCase


class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(50.5, 90.1)

    def test_init(self):
        self.assertEqual(50.5, self.test_vehicle.fuel)
        self.assertEqual(50.5, self.test_vehicle.capacity)
        self.assertEqual(90.1, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_type(self):
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.test_vehicle.drive(9)
        self.assertEqual(39.25, self.test_vehicle.fuel)

        self.test_vehicle.fuel = 50.5

        self.test_vehicle.drive(40.4)
        self.assertEqual(0, self.test_vehicle.fuel)

    def test_refuel_too_much_fuel(self):
        self.test_vehicle.fuel = 30

        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(30)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_enough_fuel(self):
        self.test_vehicle.fuel = 30

        self.test_vehicle.refuel(19.5)

        self.assertEqual(49.5, self.test_vehicle.fuel)

        self.test_vehicle.refuel(1)

        self.assertEqual(50.5, self.test_vehicle.fuel)

    def test_str(self):
        result = str(self.test_vehicle)

        self.assertEqual("The vehicle has 90.1 horse power with 50.5 fuel left and 1.25 fuel consumption", result)
