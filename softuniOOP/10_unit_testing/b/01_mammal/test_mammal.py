from mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.test_mammal = Mammal("Pesho", "cat", "meow")

    def test_init(self):
        self.assertEqual("Pesho", self.test_mammal.name)
        self.assertEqual("cat", self.test_mammal.type)
        self.assertEqual("meow", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.test_mammal.make_sound()

        self.assertEqual("Pesho makes meow", result)

    def test_get_kingdom(self):
        result = self.test_mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info(self):
        result = self.test_mammal.info()

        self.assertEqual("Pesho is of type cat", result)


if __name__ == "__main__":
    main()
