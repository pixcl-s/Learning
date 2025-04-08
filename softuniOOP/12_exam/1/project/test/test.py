from unittest import TestCase

from project.star_system import StarSystem


class TestStarSystem(TestCase):
    def setUp(self):
        self.star_system_test_without_habitable_zone = StarSystem(name="planets", star_type="Red giant", system_type="Single", num_planets=5)

    def test_init(self):
        self.assertEqual("planets", self.star_system_test_without_habitable_zone.name)
        self.assertEqual("Red giant", self.star_system_test_without_habitable_zone.star_type)
        self.assertEqual("Single", self.star_system_test_without_habitable_zone.system_type)
        self.assertEqual(5, self.star_system_test_without_habitable_zone.num_planets)
        self.assertEqual(None, self.star_system_test_without_habitable_zone.habitable_zone_range)

        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)

        self.assertEqual((1, 3), self.star_system_test_without_habitable_zone.habitable_zone_range)

    def test_is_habitable_True(self):
        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)
        result = self.star_system_test_without_habitable_zone.is_habitable
        self.assertTrue(result)

    def test_is_habitable_False_habitable_zone_range_is_none_planets_greater_than_zero(self):
        result = self.star_system_test_without_habitable_zone.is_habitable
        self.assertFalse(result)

    def test_is_habitable_False_habitable_zone_range_is_none_planets_equal_to_zero(self):
        self.star_system_test_without_habitable_zone.num_planets = 0
        result = self.star_system_test_without_habitable_zone.is_habitable
        self.assertFalse(result)

    def test_is_habitable_False_habitable_zone_range_is_not_none_planets_equal_to_zero(self):
        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)
        self.star_system_test_without_habitable_zone.num_planets = 0
        result = self.star_system_test_without_habitable_zone.is_habitable
        self.assertFalse(result)

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.name = ""

        self.assertEqual("Name must be a non-empty string.", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.name = "\n\n\n\n"

        self.assertEqual("Name must be a non-empty string.", str(ve.exception))

    def test_star_type_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.star_type = "a"

        self.assertEqual("Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].", str(ve.exception))

    def test_system_type_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.system_type = "a"

        self.assertEqual("System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].", str(ve.exception))

    def test_num_planets_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.num_planets = -1

        self.assertEqual("Number of planets must be a non-negative integer.", str(ve.exception))

    def test_habitable_zone_range_setter_error_tuple_of_1_number(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.habitable_zone_range = (1,)

        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ve.exception))

    def test_habitable_zone_range_setter_error_tuple_of_3_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 2, 3)

        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ve.exception))

    def test_habitable_zone_range_setter_error_tuple_1st_number_is_equal_or_larger(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.habitable_zone_range = (3, 3)

        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.star_system_test_without_habitable_zone.habitable_zone_range = (3, 1)

        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ve.exception))

    def test_gt_error_one_planet_unhabitable(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5, habitable_zone_range=(1, 3))
        with self.assertRaises(ValueError) as ve:
            test = self.star_system_test_without_habitable_zone < test_second

        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(ve.exception))

        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)
        test_second.num_planets = 0
        with self.assertRaises(ValueError) as ve:
            test = self.star_system_test_without_habitable_zone < test_second

        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(ve.exception))

    def test_gt_error_both_planets_unhabitable(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5)

        with self.assertRaises(ValueError) as ve:
            test = self.star_system_test_without_habitable_zone > test_second

        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(ve.exception))

    def test_gt_True(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5, habitable_zone_range=(1, 5))
        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)

        result = test_second > self.star_system_test_without_habitable_zone

        self.assertTrue(result)

    def test_gt_False(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5, habitable_zone_range=(1, 5))
        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)

        result = self.star_system_test_without_habitable_zone > test_second

        self.assertFalse(result)

    def test_compare_star_systems_error(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5,
                                 habitable_zone_range=(1, 5))

        result = test_second.compare_star_systems(self.star_system_test_without_habitable_zone, test_second)

        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", result)

    def test_compare_star_systems_system_one_bigger(self):
        test_second = StarSystem(name="system", star_type="Red giant", system_type="Single", num_planets=5,
                                 habitable_zone_range=(1, 5))
        self.star_system_test_without_habitable_zone.habitable_zone_range = (1, 3)

        result = test_second.compare_star_systems(test_second, self.star_system_test_without_habitable_zone)

        self.assertEqual("system has a wider habitable zone than planets.", result)

        result = test_second.compare_star_systems(self.star_system_test_without_habitable_zone, test_second)

        self.assertEqual("system has a wider or equal habitable zone compared to planets.", result)
