from list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.test_lists = IntegerList(1, 2, 3, 4)

    def test_init_with_integers_only(self):
        self.assertEqual([1, 2, 3, 4], self.test_lists._IntegerList__data)

    def test_init_with_integers_and_strings(self):
        self.test_list = IntegerList(1, "2", 3, "4")

        self.assertEqual([1, 3], self.test_list._IntegerList__data)

    def test_init_with_strings_only(self):
        self.test_list = IntegerList("1", "2", "3", "4")

        self.assertEqual([], self.test_list._IntegerList__data)

    def test_get_data(self):
        result = self.test_lists.get_data()

        self.assertEqual([1, 2, 3, 4], result)

    def test_add_non_integer_element(self):
        with self.assertRaises(ValueError) as ve:
            self.test_lists.add("8")

        self.assertEqual("Element is not Integer", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_lists.add(8.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_element(self):
        result = self.test_lists.add(8)

        self.assertEqual([1, 2, 3, 4, 8], self.test_lists._IntegerList__data)
        self.assertEqual([1, 2, 3, 4, 8], result)

    def test_remove_index_when_index_not_in_range(self):
        with self.assertRaises(IndexError) as ie:
            self.test_lists.remove_index(20)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_when_index_in_range(self):
        result = self.test_lists.remove_index(0)

        self.assertEqual([2, 3, 4], self.test_lists._IntegerList__data)
        self.assertEqual(1, result)

    def test_get_when_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.test_lists.get(20)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_index_in_range(self):
        result = self.test_lists.get(0)

        self.assertEqual(1, result)

    def test_insert_when_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.test_lists.insert(20, 8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_when_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.test_lists.insert(1, "8")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct_index_and_element(self):
        self.test_lists.insert(1, 8)

        self.assertEqual([1, 8, 2, 3, 4], self.test_lists._IntegerList__data)

    def test_get_biggest(self):
        result = self.test_lists.get_biggest()

        self.assertEqual(4, result)

    def test_get_index(self):
        result = self.test_lists.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
