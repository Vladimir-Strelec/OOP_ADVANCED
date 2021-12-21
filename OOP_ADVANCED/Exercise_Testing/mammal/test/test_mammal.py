from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.current_animal = Mammal("Dora", "Tigre", "RRR!")

    def test_constructor(self):
        name = "Dora"
        mammal_type = "Tigre"
        sound = 'RRR!'
        mammal = Mammal(name, mammal_type, sound)
        self.current_animal._Mammal____kingdom = "animals"
        self.assertEqual("Dora", mammal.name)
        self.assertEqual("Tigre", mammal.type)
        self.assertEqual("RRR!", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.current_animal.name} makes {self.current_animal.sound}", self.current_animal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.current_animal.get_kingdom())

    def test_info(self):

        self.assertEqual(f"{self.current_animal.name} is of type {self.current_animal.type}", self.current_animal.info())


if __name__ == "__main__":
    main()