from cat import Cat

from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.test_cat = Cat("Neko")

    def test_init(self):
        self.assertEqual("Neko", self.test_cat.name)
        self.assertEqual(False, self.test_cat.fed)
        self.assertEqual(False, self.test_cat.sleepy)
        self.assertEqual(0, self.test_cat.size)

    def test_eat_if_cat_already_ate(self):
        self.test_cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.test_cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_eat_if_cat_is_hungry(self):
        self.test_cat.eat()

        self.assertEqual("Neko", self.test_cat.name)
        self.assertEqual(True, self.test_cat.fed)
        self.assertEqual(True, self.test_cat.sleepy)
        self.assertEqual(1, self.test_cat.size)

    def test_sleep_if_cat_is_hungry(self):
        with self.assertRaises(Exception) as ex:
            self.test_cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep_if_cat_is_not_hungry(self):
        self.test_cat.fed = True
        self.test_cat.sleepy = True

        self.assertEqual(True, self.test_cat.fed)
        self.assertEqual(True, self.test_cat.sleepy)

        self.test_cat.sleep()
        self.assertEqual(True, self.test_cat.fed)
        self.assertEqual(False, self.test_cat.sleepy)


if __name__ == "__main__":
    main()
