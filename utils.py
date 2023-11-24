import pygame
import pygame.freetype
from random import sample, randint, random
from pygame.mixer import Sound

from setting import *
from path import *

pygame.mixer.init()

pre_images = {'INFANTRY': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[0]]),
                                                 (tower_size[tower_type[0]][0] - 21, tower_size[tower_type[0]][1])),
              'ARCHER': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[1]]),
                                               (tower_size[tower_type[1]][0] - 21, tower_size[tower_type[1]][1])),
              'SHIELD': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[2]]),
                                               (tower_size[tower_type[2]][0] - 35, tower_size[tower_type[2]][1] - 22)),
              'FAIRY': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[3]]),
                                              (tower_size[tower_type[3]][0] - 15, tower_size[tower_type[3]][1])),
              'ARCHMAGE': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[4]]),
                                                 (tower_size[tower_type[5]][0] - 15, tower_size[tower_type[4]][1])),
              'MANIPULATOR': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[5]]),
                                                    (tower_size[tower_type[5]][0] - 15, tower_size[tower_type[5]][1])),
              'MINER': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[6]]),
                                              (tower_size[tower_type[6]][0] - 10, tower_size[tower_type[6]][1])),
              'SWORDSMAN': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[7]]),
                                                  (tower_size[tower_type[7]][0] - 40,
                                                   tower_size[tower_type[7]][1] - 25))}

bg_images = [pygame.transform.scale(pygame.image.load(main_pages[0]), (screen_width, screen_height)),
             pygame.transform.scale(pygame.image.load(main_pages[1]), (screen_width, screen_height)),
             pygame.transform.scale(pygame.image.load(main_pages[2]), (screen_width, screen_height)),
             pygame.transform.scale(pygame.image.load(main_pages[3]), (screen_width, screen_height)),
             pygame.transform.scale(pygame.image.load(main_pages[4]), (screen_width, screen_height))]

card_click = Sound(card_click)
card_click.set_volume(0.5)


class Text:
    def __init__(self, text, screen, path, foreground_color, center, size):
        self.text = text
        self.screen = screen
        self.font_path = path
        self.font = pygame.freetype.Font(self.font_path, size)
        self.foreground_color = foreground_color
        self.background_color = (0, 0, 0, 0)
        self.center = center
        self.size = size
        self.text_surface, _ = self.font.render(text, foreground_color, self.background_color)
        self.text_rect = self.text_surface.get_rect(center=center)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def change(self, new_text):
        self.text = new_text
        self.text_surface, _ = self.font.render(new_text, self.foreground_color, self.background_color)
        self.text_rect = self.text_surface.get_rect(center=self.center)


class Image:
    def __init__(self, image, screen, center, width, height):
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.width, self.height = width, height
        self.center = center
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.center[0] - self.width // 2, self.center[1] - self.height // 2))


# define button class
class Button:
    # initialize class
    def __init__(self, pos, width, height, sound=None):
        self.point1 = (pos[0] - width // 2, pos[1] - height // 2)
        self.point2 = (pos[0] + width // 2, pos[1] + height // 2)
        self.pos = pos
        self.width = width
        self.height = height
        self.sound = sound
        self.ready = True

    # to check whether mouse click button
    def button_down(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1] and self.ready:
            if self.sound:
                self.sound.play()
            return True

    def remove(self):
        self.ready = False


class TextButton(Button):
    def __init__(self, text, background, path, text_color, button_color, pos, width, height, sound=None):
        super().__init__(pos, width, height, sound)
        self.background = background
        self.button_color = button_color
        self.rect = pygame.Rect(self.point1[0], self.point1[1], self.point2[0] - self.point1[0],
                                self.point2[1] - self.point1[1])
        self.text = Text(text, background, path, text_color, pos, int(height * 0.75))

    def draw(self):
        self.ready = True
        pygame.draw.rect(self.background, self.button_color, self.rect)
        pygame.draw.rect(self.background, (0, 0, 0), self.rect, 3)
        self.text.draw()


class ImageButton(Button):
    def __init__(self, image, background, pos, width, height, sound=None):
        super().__init__(pos, width, height, sound)
        self.background = background
        self.img = pygame.transform.scale(pygame.image.load(image), (width, height))

    def draw(self):
        self.ready = True
        self.background.blit(self.img, self.point1)


class MoveButton(ImageButton):
    def __init__(self, image, background, pos, width, height, sound=None):
        super().__init__(image, background, pos, width, height, sound)
        self.new_center = pos[0], pos[1] + 32
        self.origin_center = pos
        self.pos = pos
        self.speed = 5

    def move(self):
        if self.pos[1] < self.new_center[1]:
            self.pos = list(self.pos)
            self.pos[1] += self.speed
            self.pos = tuple(self.pos)
            self.point1 = (self.pos[0] - self.width // 2, self.pos[1] - self.height // 2)
            self.point2 = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2)

    def back(self):
        if self.pos[1] > self.origin_center[1]:
            self.pos = list(self.pos)
            self.pos[1] -= self.speed
            self.pos = tuple(self.pos)
            self.point1 = (self.pos[0] - self.width // 2, self.pos[1] - self.height // 2)
            self.point2 = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2)


class AdvancedButton(ImageButton):
    def __init__(self, image, background, pos, width, height, otherimage, upsound=None, downsound=None):
        super().__init__(image, background, pos, width, height)
        self.background = background
        self.downsound = downsound
        self.upsound = upsound
        self.img = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.otherimg = pygame.transform.scale(pygame.image.load(otherimage), (width, height))
        self.click = False
        self.inside = False

    def button_down(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1] and self.ready:
            if self.downsound:
                self.downsound.play()
            self.click = True
            self.inside = True
        else:
            self.click = False

    def button_up(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1]:
            if self.click and self.inside:
                if self.upsound:
                    self.upsound.play()
                    self.inside = False
                return True
        else:
            self.inside = False

    def draw(self):
        self.ready = True
        if self.click and self.inside:
            self.background.blit(self.otherimg, self.point1)
        else:
            self.background.blit(self.img, self.point1)


# define card class
class Card(MoveButton):
    def __init__(self, image, background, species, slot, width=card_size[0], height=card_size[1]):
        self.pos = (140 + slot * 133, 95)
        super().__init__(image, background, self.pos, width, height, sound=card_click)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.pos

        self.slot = slot
        self.species = species
        self.name = Text(self.species, self.background, AGENCYB, (192, 192, 192),
                         (self.pos[0], self.pos[1] - 56), 20)
        self.cost = Text(str(-cost_value[f'{species}']), self.background, AGENCYB, (0, 0, 0),
                         (self.pos[0], self.pos[1] + 63), 20)
        self.pre_image = pre_images[species]

        self.cd, self.cd_ready = cd_value[self.species] * 1000, cd_init[self.species]
        self.cd_edge = pygame.Rect((self.pos[0] - self.width // 2, self.pos[1] + 75, self.width, 30))
        self.cd_blank = pygame.Rect((self.pos[0] - self.width // 2, self.pos[1] + 75, self.width, 30))
        self.cd_process = pygame.Rect((self.pos[0] - self.width // 2, self.pos[1] + 75, self.width, 30))
        self.process_fraction = 0
        self.READY = Text('READY', self.background, AGENCYB, (255, 255, 0), (self.pos[0], self.pos[1] + 90), 30)
        self.start_time = pygame.time.get_ticks()

        self.chosen = False
        self.can_buy = False
        self.DISABLE = Text('DISABLE', self.background, AGENCYB, (255, 0, 0), (self.pos[0], self.pos[1] + 90), 30)

    def draw(self):
        super().draw()
        self.cost.text_rect.center = (self.pos[0], self.pos[1] + 63)
        self.name.text_rect.center = (self.pos[0], self.pos[1] - 56)
        self.cost.draw()
        self.name.draw()
        self.update()

    def update(self):
        if self.chosen:
            self.move()
        else:
            self.back()
        if self.process_fraction >= 1:
            self.cd_ready = True
            self.process_fraction = 0
        if not self.cd_ready:
            current_time = pygame.time.get_ticks()
            self.process_fraction = (current_time - self.start_time) / self.cd
            self.cd_process = pygame.Rect(
                (self.pos[0] - self.width // 2, self.pos[1] + 75, self.width * self.process_fraction, 30))
            self.cd_blank.topleft = self.pos[0] - self.width // 2, self.pos[1] + 75
            pygame.draw.rect(self.background, (255, 255, 255), self.cd_blank)
            if self.process_fraction < 0:
                self.process_fraction = 0
            elif self.process_fraction > 1:
                self.process_fraction = 1
            pygame.draw.rect(self.background,
                             (255, int(255 * (1 - self.process_fraction)),
                              int(255 * (1 - self.process_fraction))),
                             self.cd_process)
            self.cd_edge.topleft = self.pos[0] - self.width // 2, self.pos[1] + 75
            pygame.draw.rect(self.background, (0, 0, 0), self.cd_edge, 5)
        else:
            if self.pos[1] == self.origin_center[1]:
                if self.can_buy:
                    self.img.set_alpha(255)
                    self.READY.draw()
                else:
                    self.img.set_alpha(100)
                    self.DISABLE.draw()
        if self.can_buy and self.cd_ready:
            self.img.set_alpha(255)
        else:
            self.img.set_alpha(175)


class Map:
    def __init__(self):
        self.num_row = num_row
        self.num_column = num_column
        self.row = []
        self.data = []
        for row in range(1, self.num_row + 1):
            for column in range(1, self.num_column + 1):
                self.row.append(Cell(row, column))
            self.data.append(self.row)
            self.row = []

    def get_cell(self, pos):
        for row in self.data:
            for cel in row:
                if cel.in_range(pos):
                    return cel


class Cell:
    def __init__(self, row, col):
        self.range_x = (map_point1[0] + cell_size[0] * (col - 1), map_point1[0] + cell_size[0] * col)
        self.range_y = (map_point1[1] + cell_size[1] * (row - 1), map_point1[1] + cell_size[1] * row)
        self.center = ((self.range_x[0] + self.range_x[1]) / 2, (self.range_y[0] + self.range_y[1]) / 2)
        self.is_empty = True

    def in_range(self, pos):
        if self.range_x[0] <= pos[0] < self.range_x[1] and self.range_y[0] <= pos[1] < self.range_y[1]:
            return True
        else:
            return False


class Tip:
    def __init__(self, window):
        self.window = window
        self.tips = tips
        self.order = sample(range(0, len(self.tips)), len(self.tips))
        self.order_num = 0
        self.text = self.tips[self.order[self.order_num]]
        self.font_path = gabriola
        self.font = pygame.freetype.Font(self.font_path, tip_size)
        self.foreground_color = (255, 255, 255)
        self.background_color = (0, 0, 0, 0)
        self.pos = tip_pos
        self.text_surface, _ = self.font.render(self.text, self.foreground_color, self.background_color)
        self.start_time = pygame.time.get_ticks()
        self.wait_time = 15
        self.alpha_num = 255
        self.p_blink = 0.1
        self.p_disappear = 0.03
        self.alpha_increase = False
        self.blink = False

    def draw(self):
        if self.text == "Don't think you can hide in the back and escape notice..." \
                         or self.text == "Mortar? I don't know what that is...":
            self.blink = True
        else:
            self.blink = False

        pos = self.pos
        if self.blink:
            random_num = random()
            if random_num < self.p_blink:
                pos = self.pos[0] + randint(-10, 10), self.pos[1] + randint(-10, 10)
            random_num = random()
            if random_num < self.p_disappear:
                pos = 2000, 2000

        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.wait_time * 1000:
            if self.alpha_increase:
                self.alpha_num += 2
            else:
                self.alpha_num -= 2
            if self.alpha_num <= 0:
                self.order_num += 1
                if self.order_num == len(self.order):
                    self.order_num = 0
                self.text = self.tips[self.order[self.order_num]]
                self.text_surface, _ = self.font.render(self.text, self.foreground_color, self.background_color)
                self.alpha_increase = True
            if self.alpha_num >= 255:
                self.start_time = pygame.time.get_ticks()
                self.alpha_increase = False
            self.text_surface.set_alpha(self.alpha_num)

        self.window.blit(self.text_surface, pos)


class Background:
    def __init__(self, window):
        self.window = window
        self.backgrounds = bg_images
        self.order = sample(range(0, len(self.backgrounds)), len(self.backgrounds))
        self.order_num = 0
        self.background = self.backgrounds[self.order[self.order_num]]
        self.start_time = pygame.time.get_ticks()
        self.wait_time = 10
        self.alpha_num = 255
        self.alpha_increase = False

    def draw(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.start_time >= self.wait_time * 1000:
            if self.alpha_increase:
                self.alpha_num += 1
            else:
                self.alpha_num -= 1
            if self.alpha_num <= 0:
                self.order_num += 1
                if self.order_num == len(self.order):
                    self.order_num = 0
                self.background = self.backgrounds[self.order[self.order_num]]
                self.alpha_increase = True
            if self.alpha_num >= 255:
                self.start_time = pygame.time.get_ticks()
                self.alpha_increase = False
            self.background.set_alpha(self.alpha_num)

        self.window.blit(self.background, (0, 0))


def select_row(data):
    for i in range(len(data)):
        if data[i] <= max([item for index, item in enumerate(data) if index != i]) - 2:
            return i
    return randint(0, 3)
