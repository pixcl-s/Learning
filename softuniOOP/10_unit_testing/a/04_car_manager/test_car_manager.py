
from car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.test_car = Car("Peugeot", "307", 8, 60)

    def test_init(self):
        self.assertEqual("Peugeot", self.test_car.make)
        self.assertEqual("307", self.test_car.model)
        self.assertEqual(8, self.test_car.fuel_consumption)
        self.assertEqual(60, self.test_car.fuel_capacity)
        self.assertEqual(0, self.test_car.fuel_amount)

    def test_make_getter_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("", "307", 8, 60)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test = Car(None, "307", 8, 60)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_getter_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", "", 8, 60)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", None, 8, 60)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_getter_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", "307", 0, 60)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", "307", -1, 60)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_getter_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", "307", 8, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test = Car("Peugeot", "307", 8, -1)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_getter_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_invalid_numbers(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.test_car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_valid_number(self):
        self.test_car.refuel(10)

        self.assertEqual(10, self.test_car.fuel_amount)

        self.test_car.refuel(70)

        self.assertEqual(60, self.test_car.fuel_amount)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.test_car.fuel_amount = 60
        self.test_car.drive(100)

        self.assertEqual(52, self.test_car.fuel_amount)


if __name__ == "__main__":
    main()
