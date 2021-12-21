from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")
        self.members = {}

    def test_constructor(self):
        self.assertEqual("Test", self.team.name)
        self.assertEqual({}, self.team.members)
        with self.assertRaises(ValueError) as ex:
            self.team = Team("123")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_number(self):
        self.team.add_member(Vova=26)
        self.assertEqual({"Vova": 26}, self.team.members)
        self.assertEqual(f"Successfully added: ", self.team.add_member(Vova=26))

    def test_remove(self):
        self.team.add_member(Vova=26)
        name = "Vova"
        name2 = "Alina"
        self.assertEqual(f"Member {name} removed", self.team.remove_member(name))
        self.assertEqual(f"Member with name {name2} does not exist", self.team.remove_member(name2))

    def test_gt(self):
        self.team.add_member(Vova=26)
        self.team.add_member(Vov=20)
        self.team.add_member(Vo=20)
        other = Team("Drigoy")
        other.add_member(Tolik=10)
        self.assertEqual(True, self.team.__gt__(other))
        other.add_member(Toliki=10)
        other.add_member(Tol=10)
        self.assertEqual(False, self.team.__gt__(other))

    def test_add(self):
        self.team.add_member(Vova=26)
        self.assertEqual(1, self.team.members.__len__())

    def test_add_other(self):
        other = Team('Other')
        new_team_name = f"{self.team.name}{other.name}"
        new_team = Team(new_team_name)
        new_team.add_member(**self.members)
        new_team.add_member(**other.members)
        expected = self.team.name + other.name
        actual = new_team.name
        self.assertEqual(expected, actual)
        new_team.add_member(**self.members)
        new_team.add_member(**other.members)

        self.assertEqual({}, new_team.members)

    def test_str(self):
        self.team.add_member(Vova=26)
        result = """Team name: Test
Member: Vova - 26-years old"""
        actual = str(self.team)
        self.assertEqual(result, actual)


if __name__ == "__main__":
    main()