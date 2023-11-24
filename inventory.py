import pygame
import math
from pygame.mixer import Sound

from setting import *
from path import *
from utils import Text, ImageButton, Image

crosshair_image = pygame.transform.scale(pygame.image.load(crosshair_image), (crosshair_size[0], crosshair_size[1]))
flag_image = pygame.transform.scale(pygame.image.load(write_flag), (write_flag_size[0], write_flag_size[1]))
live_img = pygame.transform.scale(pygame.image.load(live_img), (heart_size[0], heart_size[1]))


class CoinDisplay:
    def __init__(self, window, level):
        self.window = window
        self.value = init_coin[level]
        self.text = Text(str(self.value), self.window, ALGER, (0, 255, 0),
                         (coin_box_pos[0] + 20, coin_box_pos[1]), 30)

    def display(self):
        self.text.draw()

    def change(self, increment):
        self.value += increment
        self.text.change(str(self.value))


class Mortar:
    def __init__(self, window):
        self.window = window
        self.box = ImageButton(mortar_card, self.window, mortar_box_pos, box_size[0], box_size[0])
        self.pos = mortar_box_pos
        self.mortar_image = Image(mortar_image, self.window, mortar_box_pos, box_size[0] - 10, box_size[0] - 10)
        self.mortar = Image(mortar_image, self.window, mortar_pos, character_size[0] * 2, character_size[0] * 2)
        self.crosshair = crosshair_image
        self.crosshair_rect = self.crosshair.get_rect()
        self.crosshair_rect.center = 0, 0
        self.shell_image = Image(shell_image, self.window, mortar_box_pos, box_size[0] - 50, box_size[0] - 5)
        self.cd = cd_value['SHELL']
        self.cost = cost_value['MORTAR']
        self.damage = damage_value['MORTAR']
        self.FIRE = Text('FIRE', self.window, AGENCYB, (255, 0, 0), (self.pos[0], self.pos[1] + 50), 25)
        self.BUY = Text(f'${-self.cost}', self.window, AGENCYB, (255, 255, 0), (self.pos[0], self.pos[1] + 50), 25)
        self.countdown = self.cd
        self.start_time = 0
        self.current_time = 0
        self.ready = True
        self.bought = False
        self.chosen = False

    def draw_box(self):
        self.box.draw()
        if self.bought:
            if self.countdown <= 0:
                self.ready = True
                self.countdown = self.cd
            if not self.ready:
                self.current_time = pygame.time.get_ticks()
                self.countdown = self.cd - int((self.current_time - self.start_time) / 1000)
                if self.countdown < 0:
                    self.countdown = 0
                elif self.countdown > self.cd:
                    self.countdown = self.cd
                x = self.countdown / self.cd
                color = (255, int(255 * x), int(255 * x))
                t = Text(f'{self.countdown}', self.window, AGENCYB, color, (self.pos[0], self.pos[1] + 50), 30)
                t.draw()
            else:
                self.FIRE.draw()
            if not self.chosen:
                self.shell_image.draw()
            self.mortar.draw()

        else:
            self.BUY.draw()
            self.mortar_image.draw()

    def aim(self, pos):
        self.crosshair_rect.center = pos
        self.window.blit(self.crosshair, self.crosshair_rect)


class WriteFlag:
    def __init__(self, window):
        self.window = window
        self.box = ImageButton(mortar_card, self.window, flag_pos, box_size[0], box_size[0])
        self.pos = flag_pos
        self.flag_image = Image(write_flag, self.window, flag_pos, box_size[0] - 10, box_size[0] - 10)
        self.flag = flag_image
        self.flag_rect = self.flag.get_rect()
        self.flag_rect.center = 0, 0
        self.chosen = False

    def draw_box(self):
        self.box.draw()
        if not self.chosen:
            self.flag_image.draw()

    def select(self, pos):
        self.flag_rect.center = pos
        self.window.blit(self.flag, self.flag_rect)


class Live(pygame.sprite.Sprite):
    def __init__(self, center, num):
        super().__init__()
        self.num = num
        self.center = center
        self.r = 40
        self.t = 0
        self.angle = pygame.time.get_ticks() // 10
        self.image = live_img
        self.origin_img = self.image
        self.rect_x = self.center[0]
        self.rect_y = self.center[1]
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def update(self):
        self.angle = pygame.time.get_ticks() // 10
        self.rect_x = self.center[0] + self.r * math.cos(math.radians(self.angle + 120 * self.num))
        self.rect_y = self.center[1] + self.r * math.sin(math.radians(self.angle + 120 * self.num))
        self.t += 1
        x = heart_size[0] * math.sin(0.05 * self.t) * 0.1
        self.image = pygame.transform.scale(self.origin_img, (heart_size[0] + x, heart_size[1] + x))
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
