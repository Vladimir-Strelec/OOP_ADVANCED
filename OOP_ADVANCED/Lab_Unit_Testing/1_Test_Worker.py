


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_worker_is_initialized_correctly(self):
        #Asert
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_worker_is_incremented_method_called(self):
        self.assertEqual(10, self.worker.energy)
        #Act
        self.worker.rest()
        #Assert
        self.assertEqual(11, self.worker.energy)

    def test_person_works_with_negative_energy_raises(self):
        # Arrange
        self.worker = Worker("Test", 100, 0)
        #Act
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        #Assertion
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        self.assertEqual(0, self.worker.money)
        #Act
        self.worker.work()
        # Assertion
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_increased_after_work(self):
        #Act
        self.worker.work()
        #Assertion
        self.assertEqual(9, self.worker.energy)

    def test_get_info_method_returns_proper_string_correct_values(self):
        #Act
        #actual_result = self.worker.get_info()
        #expected_result = "Test has saved 0 money."
        #Assertion
        self.assertEqual(f"{self.worker.name} has saved {self.worker.money} money.", self.worker.get_info())


if __name__ == '__main__':
    unittest.main()