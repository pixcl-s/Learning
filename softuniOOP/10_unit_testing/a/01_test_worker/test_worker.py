from worker import Worker

from unittest import TestCase, main


class TestWorker(TestCase):
    def setUp(self):
        self.test_worker = Worker("Pesho", 5000, 100)

    def test_init(self):
        self.assertEqual("Pesho", self.test_worker.name)
        self.assertEqual(5000, self.test_worker.salary)
        self.assertEqual(100, self.test_worker.energy)
        self.assertEqual(0, self.test_worker.money)

    def test_work_without_energy(self):
        self.test_worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.test_worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

        self.test_worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.test_worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_energy(self):
        self.test_worker.work()

        self.assertEqual("Pesho", self.test_worker.name)
        self.assertEqual(5000, self.test_worker.salary)
        self.assertEqual(99, self.test_worker.energy)
        self.assertEqual(5000, self.test_worker.money)

    def test_rest(self):
        self.test_worker.rest()

        self.assertEqual("Pesho", self.test_worker.name)
        self.assertEqual(5000, self.test_worker.salary)
        self.assertEqual(101, self.test_worker.energy)
        self.assertEqual(0, self.test_worker.money)

    def test_get_info(self):

        self.assertEqual("Pesho has saved 0 money.", self.test_worker.get_info())


if __name__ == "__main__":
    main()
