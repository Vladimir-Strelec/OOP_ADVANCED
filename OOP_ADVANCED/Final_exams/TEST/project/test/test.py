from project.movie import Movie

from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
       self.movie = Movie("Test", 1998, 10)

    def test_init(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(1998, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_errors_init(self):
        with self.assertRaises(ValueError) as ex:
            self.movie = Movie("", 1998, 10)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_errors_years(self):
        with self.assertRaises(ValueError) as ex:
            self.movie = Movie("Test", 1886, 10)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor(self):
        self.movie.add_actor("vova")
        self.assertEqual(["vova"], self.movie.actors)

    def test_add_retern(self):
        self.movie.add_actor("vova")
        self.assertEqual(f"vova is already added in the list of actors!", self.movie.add_actor("vova"))

    def test_gt_1(self):
        other = Movie("Test2", 1998, 7)
        self.assertEqual(f'"{self.movie.name}" is better than "{other.name}"', self.movie.__gt__(other))

    def test_gt_2(self):
        other = Movie("Test2", 1998, 12)
        self.assertEqual(f'"{other.name}" is better than "{self.movie.name}"', self.movie.__gt__(other))

    def test_reper(self):
        self.movie.add_actor("vova")
        expected = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        actual = repr(self.movie)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()