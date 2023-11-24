import pygame
import sys
from random import randint, sample, choice
from pygame.mixer import Sound

from setting import *
from path import *
from set_level import *
from surface import Surface
from inventory import CoinDisplay, Mortar, WriteFlag
from utils import ImageButton, Card, Map, Image, AdvancedButton, select_row
from tower import Infantry, Archer, Shield, Fairy, King, Archmage, Manipulator, Miner, Swordsman
from enemy import Viking, Barbarian, Ogre, Elementals, Masker, Elves, Phantom
from project import Flag, Campfire, Shell, Coin, SmallCoin, collide

pauseimg = pygame.transform.scale(pygame.image.load(pause_page), (screen_width, screen_height))
fightimg = pygame.transform.scale(pygame.image.load(fight), (screen_width, screen_height))

first_wave_mus = [Sound(first_wave_mus[0]), Sound(first_wave_mus[1]), Sound(first_wave_mus[2])]
final_wave_mus = [Sound(final_wave_mus[0]), Sound(final_wave_mus[1]), Sound(final_wave_mus[2])]
for sound in first_wave_mus + final_wave_mus:
    sound.set_volume(0.8)
fight_mus = Sound(fight_mus)
fight_mus.set_volume(0.1)
rest_mus = Sound(rest_mus)
rest_mus.set_volume(0.3)

pause_sound = Sound(pause_sound)
pause_sound.set_volume(0.3)
button_down_sound = Sound(button_down_sound)
button_down_sound.set_volume(0.5)
campfire_sound = Sound(campfire_sound)
campfire_sound.set_volume(0.2)
phantom_laugh = Sound(phantom_laugh)
phantom_laugh.set_volume(0.5)
buy_mortar_sound = Sound(buy_mortar_sound)
buy_mortar_sound.set_volume(0.5)
set_tower_sound = Sound(set_tower_sound)
set_tower_sound.set_volume(0.5)
king_die1 = Sound(king_die1)
king_die1.set_volume(0.5)
king_die2 = Sound(king_die2)
king_die2.set_volume(0.5)
king_die3 = Sound(king_die3)
king_die3.set_volume(0.5)
negative1_mus = Sound(negative1_mus)
negative1_mus.set_volume(0.5)
negative2_mus = Sound(negative2_mus)
negative2_mus.set_volume(0.5)

tower_dict = {
    MINER: Miner, INFANTRY: Infantry, ARCHER: Archer, MANIPULATOR: Manipulator, ARCHMAGE: Archmage, FAIRY: Fairy,
    SWORDSMAN: Swordsman, SHIELD: Shield
}
enemy_dict = {
    VIKING: Viking, BARBARIAN: Barbarian, OGRE: Ogre, ELEMENTALS: Elementals, MASKER: Masker, ELVES: Elves, PHANTOM:
        Phantom
}


class Level(Surface):
    def __init__(self, window, num):
        super().__init__(window)
        self.name = str(num)
        self.comment = None

        self.background = fightimg
        self.image = [Image(coin_box, self.window, coin_box_pos, coin_box_size[0], coin_box_size[1])]
        self.b_back = AdvancedButton(back_button2, window, (screen_center[0] - 150, screen_center[1]), 100, 100,
                                     back_button2c, button_down_sound)
        self.b_continue = AdvancedButton(continue_button, window, (screen_center[0] + 150, screen_center[1]), 100, 100,
                                         continue_buttonc, pause_sound)
        self.b_replay = AdvancedButton(replay_button, window, (screen_center[0], screen_center[1]), 100, 100,
                                       replay_buttonc, button_down_sound)
        self.b_pause = ImageButton(pause_button, self.window, (100, 35), 160, 45, pause_sound)
        self.coin_box = CoinDisplay(self.window, self.name)

        self.tower = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.ornament = pygame.sprite.Group()
        self.my_projectile = pygame.sprite.Group()
        self.other_projectile = pygame.sprite.Group()
        self.kings = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.score = 0

        self.flag = WriteFlag(self.window)
        self.tool = None
        self.cards = []
        for i in range(len(level_towers[self.name])):
            self.cards.append(Card(card_images[level_towers[self.name][i]], self.window,
                                   level_towers[self.name][i], i + 1))

        self.choose = None

        self.map = Map()
        self.waves = level_wave_dict[self.name]
        self.next_wave = 0
        self.last_wave_time = pygame.time.get_ticks()
        self.pause_tick = 0
        self.last_wave_enemy_num = 0
        self.row_enemies_num = {}
        for enemy in enemy_type:
            self.row_enemies_num[enemy] = [1, 1, 1, 1]

        self.pause = False
        self.init_king()

        self.event_mus = [True, True, True, True]
        self.event_channel = pygame.mixer.Channel(0)
        self.fight_channel = pygame.mixer.Channel(1)
        self.rest_channel = pygame.mixer.Channel(2)
        self.envir_channel = pygame.mixer.Channel(3)
        self.fire_channel = pygame.mixer.Channel(4)
        self.fire_channel.play(campfire_sound, -1)

    def draw_surface(self):
        super().draw_surface()
        if self.pause:
            self.b_back.draw()
            self.b_continue.draw()
            self.b_replay.draw()
        else:
            self.b_pause.draw()
            for image in self.image:
                image.draw()
            self.coin_box.display()
            self.flag.draw_box()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            mouse_pos = pygame.mouse.get_pos()

            if not self.pause:
                self.load_music()
                self.load_ornament()
                self.load_projectile()
                self.load_tower()
                self.load_king()
                self.load_enemy()
                self.deal_wave()
                self.load_coin()
                self.show(mouse_pos)
                self.check_game()
                self.load_card()
            self.event_loop()

            pygame.display.flip()
            clock.tick(fps)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if not self.pause:
                    self.set_tower(pos)
                    self.clic_coin(pos)
                    self.load_tool(pos)

                    if self.b_pause.button_down(pos):
                        self.pause = True
                        self.pause_tick = pygame.time.get_ticks()
                        self.fight_channel.pause()
                        self.event_channel.pause()
                        self.rest_channel.play(rest_mus, -1)
                        self.background = pauseimg

                else:
                    self.b_continue.button_down(pos)
                    self.b_back.button_down(pos)
                    self.b_replay.button_down(pos)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = event.pos
                if self.b_continue.button_up(pos):
                    self.pause = False
                    self.fight_channel.unpause()
                    self.event_channel.unpause()
                    self.rest_channel.stop()
                    self.background = fightimg
                    for tower in self.tower:
                        if tower.name == 'MINER':
                            tower.last_time += pygame.time.get_ticks() - self.pause_tick
                    for coin in self.coin:
                        coin.start_time += pygame.time.get_ticks() - self.pause_tick

                elif self.b_back.button_up(pos):
                    self.comment = 'back'
                    self.running = False
                    self.stop_all_music()

                elif self.b_replay.button_up(pos):
                    self.comment = 'replay'
                    self.running = False
                    self.stop_all_music()

    def load_music(self):
        if self.next_wave == len(self.waves) // 2:
            if not self.fight_channel.get_busy():
                self.fight_channel.play(fight_mus, -1)
        if not self.event_channel.get_busy():
            if self.next_wave == 1 and self.event_mus[0]:
                self.event_channel.play(first_wave_mus[randint(0, len(first_wave_mus) - 1)])
                self.event_mus[0] = False
            elif not self.waves[self.next_wave] and self.event_mus[1]:
                self.event_channel.play(final_wave_mus[randint(0, len(final_wave_mus) - 1)])
                self.event_mus[1] = False
            elif len(self.kings) <= 2 and self.event_mus[2]:
                self.event_channel.play(negative1_mus)
                self.event_mus[2] = False
            elif len(self.kings) <= 1 and self.event_mus[3]:
                self.event_channel.play(negative2_mus)
                self.event_mus[3] = False

    def stop_all_music(self):
        self.event_channel.stop()
        self.rest_channel.stop()
        self.fight_channel.stop()
        self.fire_channel.stop()
        self.envir_channel.stop()

    def load_card(self):
        for card in self.cards:
            if -cost_value[card.species] <= self.coin_box.value:
                card.can_buy = True
            else:
                card.can_buy = False
            card.draw()

    def load_tower(self):
        for tower in self.tower:
            if not tower.live:
                if tower.state != "dying":
                    tower.y = 0
                    tower.state = "dying"
                    self.map.get_cell(tower.rect.center).is_empty = True

                    if tower.name == 'INFANTRY':
                        for i in range(tower.return_coin // 5):
                            coin = Coin(tower.rect_x + randint(-50, 50), tower.rect_y + randint(-50, 50))
                            self.coin.add(coin)
                        for i in range(tower.return_coin % 5):
                            coin = SmallCoin(tower.rect_x + randint(-50, 50), tower.rect_y + randint(-50, 50))
                            self.coin.add(coin)
        self.tower.update(enemies=self.enemy, projectiles=self.my_projectile, towers=self.tower, coins=self.coin)
        self.tower.draw(self.window)

    def load_enemy(self):
        for enemy in self.enemy:
            if not enemy.live:
                if enemy.name == 'PHANTOM':
                    if enemy.action != 'dying':
                        enemy.action = 'dying'
                        enemy.y = 0
                        ran_n = randint(0, 100) / 100
                        if ran_n <= enemy.p_drop:
                            ran_n = randint(0, 100) / 100
                            if ran_n <= 0.5:
                                coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                self.coin.add(coin)
                            elif 0.5 < ran_n <= 0.8:
                                for i in range(2):
                                    coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                    self.coin.add(coin)
                            elif 0.8 < ran_n <= 1:
                                for i in range(3):
                                    coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                    self.coin.add(coin)

                else:
                    if enemy.state != "dying":
                        enemy.y = 0
                        enemy.state = "dying"
                        ran_n = randint(0, 100) / 100
                        if ran_n <= enemy.p_drop:
                            ran_n = randint(0, 100) / 100
                            if ran_n <= 0.5:
                                coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                self.coin.add(coin)
                            elif 0.5 < ran_n <= 0.8:
                                for i in range(2):
                                    coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                    self.coin.add(coin)
                            elif 0.8 < ran_n <= 1:
                                for i in range(3):
                                    coin = Coin(enemy.rect_x + randint(-50, 50), enemy.rect_y + randint(-50, 50))
                                    self.coin.add(coin)
        self.enemy.update(self.tower, self.other_projectile)
        self.enemy.draw(self.window)

    def load_projectile(self):
        self.other_projectile.update(self.tower)
        self.other_projectile.draw(self.window)
        filtered_sprites = [sprite for sprite in self.enemy if sprite.state != "falling"]
        self.my_projectile.update(enemy_group=filtered_sprites, tower_group=self.tower)
        self.my_projectile.draw(self.window)

    def load_tool(self, pos):
        if self.flag.box.button_down(pos):
            if self.tool == 'FLAG':
                self.flag.chosen = False
                self.tool = None
            else:
                if self.tool and self.name == '8':
                    self.mortar.chosen = False
                self.flag.chosen = True
                self.tool = 'FLAG'
        elif self.tool == 'FLAG':
            for tower in self.tower:
                if tower.rect.collidepoint(pos):
                    if tower.name == 'INFANTRY':
                        for i in range(tower.return_coin // 5):
                            coin = Coin(tower.rect_x + randint(-50, 50), tower.rect_y + randint(-50, 50))
                            self.coin.add(coin)
                        for i in range(tower.return_coin % 5):
                            coin = SmallCoin(tower.rect_x + randint(-50, 50), tower.rect_y + randint(-50, 50))
                            self.coin.add(coin)
                    if tower.name != 'KING':
                        tower.kill()
                        self.map.get_cell(tower.rect.center).is_empty = True
                        self.flag.chosen = False
                        self.tool = None

    def load_ornament(self):
        if not len(self.ornament):
            for i in range(6):
                flag = Flag(i)
                self.ornament.add(flag)
            for i in range(2):
                campfire = Campfire(i)
                self.ornament.add(campfire)

        self.ornament.update()
        self.ornament.draw(self.window)

    def load_coin(self):
        self.coin.update(self.coin_box)
        self.coin.draw(self.window)

    def clic_coin(self, pos):
        self.coin.update(self.coin_box, pos)

    def set_tower(self, pos):
        for card in self.cards:
            if card.button_down(pos):
                self.tool = None
                if self.choose == card:
                    self.choose.chosen = False
                    self.choose = None
                else:
                    self.choose = card
                    other_cards = [card for card in self.cards if card != self.choose]
                    for other_card in other_cards:
                        other_card.chosen = False
                    self.choose.chosen = True

        if self.choose and map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
            if self.choose.cd_ready:
                species = tower_dict[self.choose.species]()
                if self.coin_box.value + species.cost >= 0:
                    cell = self.map.get_cell(pos)
                    if cell.is_empty:
                        set_tower_sound.play()
                        if species.name == 'MINER':
                            species.last_time = pygame.time.get_ticks() - 17000
                        species.set((cell.center[0] + randint(-5, 5), cell.center[1] + randint(-5, 5)))
                        self.tower.add(species)
                        self.coin_box.change(species.cost)
                        cell.is_empty = False
                        self.choose.cd_ready = False
                        self.choose.start_time = pygame.time.get_ticks()
                        self.choose.chosen = False
                        self.choose = None

    def show(self, pos):
        if self.tool:
            if self.choose:
                self.choose.chosen = False
            self.choose = None
            if self.tool == 'FLAG':
                self.flag.select(pos)

        elif self.choose:
            self.tool = None
            if map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
                cell = self.map.get_cell(pos)
                if cell.is_empty:
                    rect = self.choose.pre_image.get_rect()
                    rect.center = cell.center
                    self.window.blit(self.choose.pre_image, rect)

    def init_king(self):
        if not len(self.kings):
            king_num = sample(range(0, 3), 3)
            for i in range(3):
                king = King(king_num[i])
                king.set((110, rows[i]))
                self.kings.add(king)
            king = King(randint(0, 2))
            king.set((110, rows[3]))
            self.kings.add(king)

    def load_king(self):
        self.kings.update()
        self.kings.draw(self.window)
        for king in self.kings:
            if king.live:
                enemy = collide(king, self.enemy, 0.3)
                if enemy:
                    if king.lives:
                        if enemy.name == 'PHANTOM' and len(king.lives) >= 2:
                            phantom_laugh.play()
                            for i in range(2):
                                live = choice(king.lives.sprites())
                                live.kill()
                                enemy.kill()
                        else:
                            live = choice(king.lives.sprites())
                            live.kill()
                            enemy.kill()
                if not king.lives:
                    king.live = False
            else:
                if king.state != "dying":
                    if king.num == 0:
                        king_die1.play()
                    elif king.num == 1:
                        king_die2.play()
                    elif king.num == 2:
                        king_die3.play()
                    king.y = 0
                    king.state = "dying"
            king.lives.update()
            king.lives.draw(self.window)

    def check_game(self):
        if len(self.kings) <= 0:
            self.comment = 'loss'
            self.running = False
            self.stop_all_music()
        for enemy in self.enemy:
            if enemy.rect_x <= 0:
                self.comment = 'loss'
                self.running = False
                self.stop_all_music()
        if not self.waves[self.next_wave]:
            if not len(self.enemy):
                self.comment = 'win'
                self.running = False
                for king in self.kings:
                    self.score += len(king.lives)
                self.stop_all_music()

    def wave(self):
        wave = self.waves[self.next_wave]
        for i in range(len(wave[0])):
            for k in range(wave[1][i]):
                enemy = wave[0][i]
                row_num = select_row(self.row_enemies_num[enemy])
                row = rows[row_num]
                self.row_enemies_num[enemy][row_num] += 1
                if enemy == ELVES:
                    enemy = enemy_dict[enemy]()
                    enemy.set((randint(720, 1080), randint(-30, 30)))
                else:
                    enemy = enemy_dict[enemy]()
                    enemy.set((screen_width + randint(50, 150), row + randint(-3, 3)))
                self.enemy.add(enemy)

    def deal_wave(self):
        current_time = pygame.time.get_ticks()
        if self.waves[self.next_wave]:
            if self.next_wave != 0 and not len(self.enemy):
                if current_time - self.last_wave_time >= 800 * self.waves[self.next_wave][2]:
                    self.wave()
                    self.next_wave += 1
                    self.last_wave_time = current_time
            elif self.next_wave != 0 and len(self.enemy) >= self.last_wave_enemy_num // 2:
                if current_time - self.last_wave_time >= 1200 * self.waves[self.next_wave][2]:
                    self.wave()
                    self.next_wave += 1
                    self.last_wave_time = current_time
            elif self.next_wave != 0 and len(self.enemy) < self.last_wave_enemy_num // 2:
                if current_time - self.last_wave_time >= 1000 * self.waves[self.next_wave][2]:
                    self.wave()
                    self.next_wave += 1
                    self.last_wave_time = current_time
            elif self.next_wave == 0:
                if current_time - self.last_wave_time >= 1000 * self.waves[self.next_wave][2]:
                    self.wave()
                    self.next_wave += 1
                    self.last_wave_time = current_time
            self.last_wave_enemy_num = 0
            if self.waves[self.next_wave]:
                for i in self.waves[self.next_wave][1]:
                    self.last_wave_enemy_num += i


class Level8(Level):
    def __init__(self, window):
        super().__init__(window, 8)
        self.mortar = Mortar(self.window)

    def draw_surface(self):
        super().draw_surface()
        if self.pause:
            self.b_back.draw()
            self.b_continue.draw()
            self.b_replay.draw()
        else:
            self.b_pause.draw()
            for image in self.image:
                image.draw()
            self.coin_box.display()
            self.flag.draw_box()
            self.mortar.draw_box()

    def load_tool(self, pos):
        super().load_tool(pos)
        if self.mortar.box.button_down(pos):
            if not self.mortar.bought and self.coin_box.value + self.mortar.cost >= 0:
                buy_mortar_sound.play()
                self.mortar.bought = True
                self.coin_box.change(self.mortar.cost)
                self.mortar.start_time = pygame.time.get_ticks()
            elif self.mortar.bought and self.mortar.ready:
                if self.tool == 'MORTAR':
                    self.mortar.chosen = False
                    self.tool = None
                else:
                    if self.tool:
                        self.flag.chosen = False
                    self.mortar.chosen = True
                    self.tool = 'MORTAR'
        elif self.tool == 'MORTAR':
            shell = Shell(pos[0], self.mortar.damage, pos[1])
            self.my_projectile.add(shell)
            self.mortar.start_time = pygame.time.get_ticks()
            self.mortar.ready = False
            self.mortar.chosen = False
            self.tool = None

    def show(self, pos):
        if self.tool:
            if self.choose:
                self.choose.chosen = False
            self.choose = None
            if self.tool == 'MORTAR':
                if self.mortar.bought:
                    self.mortar.aim(pos)
            elif self.tool == 'FLAG':
                self.flag.select(pos)

        elif self.choose:
            self.tool = None
            if map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
                cell = self.map.get_cell(pos)
                if cell.is_empty:
                    rect = self.choose.pre_image.get_rect()
                    rect.center = cell.center
                    self.window.blit(self.choose.pre_image, rect)
