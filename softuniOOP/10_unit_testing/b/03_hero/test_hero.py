from unittest import TestCase

from hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.test_hero = Hero("Pesho", 10, 100, 10)
        self.test_enemy = Hero("Gosho", 10, 100, 10)

    def test_init(self):
        self.assertEqual("Pesho", self.test_hero.username)
        self.assertEqual(10, self.test_hero.level)
        self.assertEqual(100, self.test_hero.health)
        self.assertEqual(10, self.test_hero.damage)

    def test_battle_when_names_are_the_same(self):
        self.test_enemy.username = "Pesho"

        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_health_is_zero_or_less(self):
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.test_enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.test_hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.test_enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))


    def test_battle_when_enemy_health_is_zero_or_less(self):
        self.test_enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.test_enemy)

        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

        self.test_enemy.health = -1
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.test_enemy)

        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_battle_draw(self):
        result = self.test_hero.battle(self.test_enemy)

        self.assertEqual("Draw", result)

        self.assertEqual(0, self.test_hero.health)
        self.assertEqual(10, self.test_hero.level)
        self.assertEqual(10, self.test_hero.damage)

        self.assertEqual(0, self.test_enemy.health)
        self.assertEqual(10, self.test_enemy.level)
        self.assertEqual(10, self.test_enemy.damage)

    def test_battle_hero_win(self):
        self.test_enemy.level = 1

        result = self.test_hero.battle(self.test_enemy)

        self.assertEqual(11, self.test_hero.level)
        self.assertEqual(95, self.test_hero.health)
        self.assertEqual(15, self.test_hero.damage)

        self.assertEqual(1, self.test_enemy.level)
        self.assertEqual(0, self.test_enemy.health)
        self.assertEqual(10, self.test_enemy.damage)

        self.assertEqual("You win", result)

    def test_battle_enemy_win(self):
        self.test_hero.level = 1

        result = self.test_hero.battle(self.test_enemy)

        self.assertEqual(1, self.test_hero.level)
        self.assertEqual(0, self.test_hero.health)
        self.assertEqual(10, self.test_hero.damage)

        self.assertEqual(11, self.test_enemy.level)
        self.assertEqual(95, self.test_enemy.health)
        self.assertEqual(15, self.test_enemy.damage)

        self.assertEqual("You lose", result)

    def test_str(self):
        result = str(self.test_hero)

        self.assertEqual(f"Hero Pesho: 10 lvl\nHealth: 100\nDamage: 10\n", result)
