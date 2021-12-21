class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_Cat_size_is_increased_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_Cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_Cat_cannot_eat_if_already_fed_raises_an_error(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_Cat_cannot_fall_asleep_if_not_fed_raises_an_error(self):
        self.assertEqual(False, self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_Cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()