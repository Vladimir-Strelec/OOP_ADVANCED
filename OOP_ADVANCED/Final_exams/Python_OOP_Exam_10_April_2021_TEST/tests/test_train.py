from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 100)

    def test_class_parametrs(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_constructor(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_train_ful(self):
        self.train = Train("Test", 2)
        self.train.passengers = ["lol", "kill"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("LOH")
        self.assertEqual("Train is full", str(ex.exception))

    def test_train_name(self):
        self.train = Train("", 2)
        self.train.passengers = ["Test"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Test")
        self.assertEqual("Passenger Test Exists", str(ex.exception))

    def test_current_name(self):
        self.train.add("lol")
        self.assertEqual("lol", self.train.passengers[0])
        expected = "Added passenger lol"
        actual = self.train.PASSENGER_ADD.format("lol")
        self.assertEqual(expected, actual)

    def test_remove(self):
        self.train.add("lol")
        with self.assertRaises(ValueError) as ex:
            self.train.remove("kot")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_complied(self):
        self.train.add("lol")
        self.train.add("kol")
        self.train.remove("kol")
        self.assertEqual("lol", self.train.passengers[0])

    def test_remove_complied_messenger(self):
        self.train.add("lol")
        self.train.add("kol")
        self.assertEqual("Removed kol", self.train.remove("kol"))


if __name__ == "__main__":
    main()