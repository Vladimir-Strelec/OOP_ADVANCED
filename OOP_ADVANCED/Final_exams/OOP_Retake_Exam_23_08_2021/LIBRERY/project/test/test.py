from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Biblioteka")

    def test_chek_raise_valid_string(self):
        with self.assertRaises(ValueError) as ex:
            self.library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_initialization(self):
        self.assertEqual("Biblioteka", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_add_book(self):
        self.library.add_book("Strugackih", "Anigilyaciya")
        expected = "Anigilyaciya"
        actual = ''.join(self.library.books_by_authors["Strugackih"])

        self.assertEqual(expected, actual)
        self.library.add_book("Strugackih", "Anigilyaciya")
        expected = 1
        actual = len(self.library.books_by_authors)
        self.assertEqual(expected, actual)

    def test_chek_name_in_reader(self):
        self.library.add_reader("Arendadatel")
        expected = []
        actual = self.library.readers["Arendadatel"]
        self.assertEqual(expected, actual)

        expected = f"{'Arendadatel'} is already registered in the {self.library.name} library."
        actual = self.library.add_reader("Arendadatel")
        self.assertEqual(expected, actual)

    def test_chek_rent_book_reader_name(self):
        expected = f"{'Vladimir'} is not registered in the {self.library.name} Library."
        actual = self.library.rent_book("Vladimir", "Strugackih", "Anigilyaciya")
        self.assertEqual(expected, actual)

    def test_chek_rent_book_book_author(self):
        expected = f"{self.library.name} Library does not have any {'Strug'}'s books."
        self.library.add_reader("Arendadatel")
        actual = self.library.rent_book("Arendadatel", "Strug", "Anigilyaciya")
        self.assertEqual(expected, actual)

    def test_chek_rent_book_title(self):
        self.library.add_reader("Vladimir")
        self.library.add_book("Strugackih", "Piknik")
        self.library.rent_book("Vladimir", "Strugackih", "Anigilyaciya")
        expected = f"""{self.library.name} Library does not have {"Strugackih"}'s "{"Anigilyaciya"}"."""
        actual = self.library.rent_book("Vladimir", "Strugackih", "Anigilyaciya")
        self.assertEqual(expected, actual)

    def test_chek_rent_result(self):
        self.library.add_reader("Vladimir")
        self.library.add_book("Strugackih", "Piknik")
        self.library.rent_book("Vladimir", "Strugackih", "Piknik")

        self.assertEqual("Vladimir", ''.join(self.library.readers.keys()))
        self.assertEqual([{"Strugackih": "Piknik"}], self.library.readers["Vladimir"])

        self.library.add_book("Strugackih", "Piknik")
        actual = self.library.books_by_authors["Strugackih"].index("Piknik")
        self.assertEqual(0, actual)
        self.library.rent_book("Vladimir", "Strugackih", "Piknik")
        self.assertEqual([], self.library.books_by_authors['Strugackih'])


if __name__ == "__main__":
    main()