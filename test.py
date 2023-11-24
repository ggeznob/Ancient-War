import unittest
from random import randint
import time
import pygame

from setting import *
from main import Game
from level import Level
from user import LevelData, save, load
from surface import MainPage, LevelMenu, WinPage
from tower import Infantry, Archer, Shield, Archmage, Miner
from enemy import Viking, Barbarian, Ogre, Elementals, Masker
from project import Coin


class TestAncientWarLevel(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = Game()
        self.level = Level(self.game.window, 1)

    def tearDown(self):
        self.level = Level(self.game.window, 1)

    def test_gold_production(self):
        self.level.coin.add(Coin(0, 0))
        miner = Miner()
        miner.mine_time = 2
        self.level.tower.add(miner)
        self.assertEqual(len(self.level.coin), 1)
        self.level.clic_coin((0, 0))

        start_time = time.time()
        while time.time() - start_time < 3:
            self.level.load_coin()
        self.assertEqual(len(self.level.coin), 0)
        self.assertEqual(self.level.coin_box.value, 100)

        start_time = time.time()
        while time.time() - start_time < 3:
            self.level.load_tower()
        self.assertGreaterEqual(len(self.level.coin), 1)

    def test_king(self):
        self.level.init_king()
        self.assertEqual(len(self.level.kings), 4)

        for i in range(1, 4):
            for king in self.level.kings:
                enemy = Viking()
                enemy.set(king.rect.center)
                self.level.enemy.add(enemy)
                self.level.load_king()
                self.assertEqual(len(king.lives), 3 - i)

        start_time = time.time()
        while time.time() - start_time < 5:
            self.level.load_king()
        self.assertEqual(len(self.level.kings), 0)

    def test_attack(self):
        having_projectile_group = [Archer(), Archmage()]
        non_projectile_group = [Infantry(), Shield(), Viking(), Barbarian(), Ogre(), Masker()]

        for character in having_projectile_group:
            character.set(screen_center)
            character.attack(self.level.other_projectile)
            aim = Infantry()
            aim.set((screen_center[0] + 50, screen_center[1]))
            self.level.tower.add(aim)
            start_time = time.time()
            while time.time() - start_time < 1:
                self.level.load_projectile()
            self.assertEqual(aim.HP, aim.full_HP + character.damage)

        for character in non_projectile_group:
            character.set(screen_center)
            aim = Infantry()
            aim.set(screen_center)
            if character.name == "MASKER":
                character.state = "walking"
            character.attack(aim)
            self.assertEqual(aim.HP, aim.full_HP + character.damage)

    def test_move(self):
        test_group = [Viking(), Barbarian(), Ogre(), Masker(), Elementals()]
        for character in test_group:
            character.state = "walking"
            character.set((screen_width, screen_center[1]))
            self.level.enemy.add(character)
            walk_num = 1
            for i in range(5):
                self.level.load_enemy()
                walk_num += 1
            self.assertGreaterEqual(character.rect_x, screen_width - character.move_speed * walk_num - 5)
            self.assertLessEqual(character.rect_x, screen_width - character.move_speed * walk_num + 5)

    def test_tower_deployment(self):
        self.assertTrue(self.level.cards[0].cd_ready)
        self.level.set_tower(self.level.cards[0].pos)
        self.level.set_tower(screen_center)
        self.assertFalse(self.level.cards[0].cd_ready)
        self.level.cards[0].process_fraction = 1
        self.level.cards[0].update()
        self.assertTrue(self.level.cards[0].cd_ready)

    def test_successful_use_tool(self):
        self.assertFalse(self.level.flag.chosen)
        self.level.load_tool(self.level.flag.pos)
        self.assertTrue(self.level.flag.chosen)
        tower = Infantry()
        tower.set(screen_center)
        self.level.tower.add(tower)
        self.level.load_tool(screen_center)
        self.assertEqual(len(self.level.tower), 0)
        self.assertFalse(self.level.flag.chosen)

    def test_victory_condition(self):
        self.level.waves = [None]
        self.level.game_loop()
        self.assertEqual(self.level.comment, "win")
        self.assertFalse(self.level.running)

    def test_defeat_condition(self):
        self.level.kings.empty()
        self.level.game_loop()
        self.assertEqual(self.level.comment, "loss")
        self.assertFalse(self.level.running)


class TestGameFunctionality(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.game = Game()

    def tearDown(self):
        pygame.quit()

    def test_main_page(self):
        click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': self.game.stage.b_start.pos})
        pygame.event.post(click_event)
        self.game.stage.game_loop()
        self.assertEqual(self.game.stage.comment, 'levelmenu')
        self.assertFalse(self.game.stage.running)

        self.game.stage = MainPage(self.game.window)
        click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': self.game.stage.b_quit.pos})
        pygame.event.post(click_event)
        self.game.stage.game_loop()
        self.assertEqual(self.game.stage.comment, 'quit')
        self.assertFalse(self.game.stage.running)

    def test_load_save_data(self):
        origin_data = load()
        analog_data = {'level_access': [False] * 8, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
        for i in range(8):
            if randint(0, 1):
                analog_data['level_access'][i] = True
            else:
                analog_data['level_access'][i] = False
        for i in range(1, 9):
            analog_data[str(i)] = randint(0, 12)

        save(analog_data)
        self.game.stage = LevelMenu(self.game.window)
        test_data = self.game.stage.level_data.data
        for i in range(1, 9):
            self.assertEqual(test_data['level_access'][i - 1], analog_data['level_access'][i - 1])
            self.assertEqual(test_data[str(i)], analog_data[str(i)])

        analog_data['level_access'][1] = False
        analog_data['1'] = 0
        save(analog_data)
        LevelData().init()
        self.game.stage = WinPage(self.game.window, '1', 12)
        self.game.stage = LevelMenu(self.game.window)
        test_data = self.game.stage.level_data.data
        self.assertTrue(test_data['level_access'][1])
        self.assertEqual(test_data['1'], 12)

        save(origin_data)


if __name__ == '__main__':
    unittest.main()
