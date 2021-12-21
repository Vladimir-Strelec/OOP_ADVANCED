from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero(username='Name', level=10, health=5.5, damage=6.6)

    def test_constructor(self):
        self.assertEqual("Name", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(5.5, self.hero.health)
        self.assertEqual(6.6, self.hero.damage)

    def test_method_battle_return_raise_with_request_name(self):
        enemy_hero = Hero('Name', 11, 10, 7.7)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_method_battle_return_raise_with_request_health_hero(self):
        for health in [0, -25]:
            enemy_hero = Hero(username='Enemy_hero', level=11, health=100, damage=7.7)
            self.hero = Hero(username='Name', level=11, health=health, damage=7.7)
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(enemy_hero)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_method_battle_return_raise_with_request_health_enemy_hero(self):
        for health in [0, -25]:
            enemy_hero = Hero(username='Enemy_hero', level=11, health=health, damage=7.7)
            self.hero = Hero(username='Name', level=11, health=10, damage=7.7)
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(enemy_hero)
            self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    # def test_player_damage(self):
    #     damage = self.hero.level * self.hero.damage
    #     self.assertEqual(66.0, damage)
    #
    # def test_enemy_hero_damage(self):
    #     enemy_hero = Hero(username='Enemy_hero', level=10, health=10.7, damage=7.7)
    #     damage = enemy_hero.damage * enemy_hero.level
    #     self.assertEqual(77.0, damage)

    def test_health_zero_hero_and_enemy_hero(self):
        enemy_hero = Hero(username='Enemy_hero', level=10, health=10.0, damage=7.7)
        self.hero = Hero(username='Name', level=10, health=5.5, damage=6.6)

        expected_health_enemy = enemy_hero.health - self.hero.damage * self.hero.level
        expected_health_hero = self.hero.health - enemy_hero.damage * enemy_hero.level

        self.assertEqual("Draw", self.hero.battle(enemy_hero))
        self.assertEqual(expected_health_enemy, enemy_hero.health)
        self.assertEqual(expected_health_hero, self.hero.health)

    def test_health_zero_only_enemy_hero(self):
        enemy_hero = Hero(username='Enemy_hero', level=1, health=10.0, damage=1.7)
        self.hero = Hero(username='Name', level=10, health=5.5, damage=6.6)
        self.assertEqual("You win", self.hero.battle(enemy_hero))

        self.assertEqual(11, self.hero.level)

        self.assertEqual(8.8, self.hero.health)

        self.assertEqual(11.6, self.hero.damage)

    def test_health_zero_only_hero(self):
        enemy_hero = Hero(username='Enemy_hero', level=10, health=5.5, damage=6.6)
        self.hero = Hero(username='Name', level=1, health=10.0, damage=1.7)
        self.assertEqual("You lose", self.hero.battle(enemy_hero))

        self.assertEqual(11, enemy_hero.level)

        self.assertEqual(8.8, enemy_hero.health)

        self.assertEqual(11.6, enemy_hero.damage)

    def test_string(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()