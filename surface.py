import pygame
import sys
from pygame.mixer import Sound

from utils import ImageButton, Tip, Background, Image, AdvancedButton
from project import Star
from setting import *
from path import *
from set_level import *
from user import LevelData

pygame.mixer.init()
level_menu_bg = pygame.transform.scale(pygame.image.load(level_menu), (screen_width, screen_height))
loss_bg = pygame.transform.scale(pygame.image.load(loss_page), (screen_width, screen_height))
win_bg = pygame.transform.scale(pygame.image.load(win_page), (screen_width, screen_height))
you_loss = pygame.transform.scale(pygame.image.load(you_loss), (675, 90))

gold_star = pygame.transform.scale(pygame.image.load(gold_star), (40, 40))

button_down_sound = Sound(button_down_sound)
button_down_sound.set_volume(0.2)
win_mus = Sound(win_mus)
win_mus.set_volume(0.5)
loss_mus = Sound(loss_mus)
loss_mus.set_volume(0.5)


class Surface:
    def __init__(self, window):
        self.window = window
        self.running = True
        self.background = None

    def draw_surface(self):
        self.window.blit(self.background, (0, 0))

    def remove(self):
        self.window.fill((0, 0, 0))
        pygame.mixer.music.stop()


class MainPage(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.backgrounds = Background(self.window)
        self.text1 = ImageButton(title, window, (screen_center[0], 150), 500, 200)
        self.b_start = ImageButton(start_button, window, (screen_center[0], 385), 230, 80, button_down_sound)
        self.b_quit = ImageButton(exit_button, window, (screen_center[0], 515), 230, 75, button_down_sound)
        self.stage_num = 0
        self.tip = Tip(self.window)
        self.name = 'mainpage'
        self.comment = None
        pygame.mixer.music.load(mus_menu)
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)

    def draw_surface(self):
        self.backgrounds.draw()
        self.b_quit.draw()
        self.b_start.draw()
        self.text1.draw()
        self.tip.draw()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if self.b_quit.button_down(pos):
                        self.comment = 'quit'
                        self.running = False
                    elif self.b_start.button_down(pos):
                        self.comment = 'levelmenu'
                        self.running = False
            pygame.display.flip()
            clock.tick(fps)


class LevelMenu(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.background = level_menu_bg
        self.centers = [(screen_center[0] - 400, screen_center[1] - 100),
                        (screen_center[0] - 200, screen_center[1] - 100),
                        (screen_center[0], screen_center[1] - 100),
                        (screen_center[0] + 200, screen_center[1] - 100),
                        (screen_center[0] + 400, screen_center[1] - 100),
                        (screen_center[0] - 200, screen_center[1] + 60),
                        (screen_center[0], screen_center[1] + 60),
                        (screen_center[0] + 200, screen_center[1] + 60)]

        self.b_levels = []
        for i in range(level_num):
            self.b_levels.append(ImageButton(level_buttons[i + 1], self.window, self.centers[i], 100, 100,
                                             button_down_sound))

        self.b_back = ImageButton(back_button1, self.window, (screen_center[0] - 150, 600), 154, 70,
                                  button_down_sound)
        self.b_ok = ImageButton(ok_button, self.window, (screen_center[0] + 150, 600), 154, 70,
                                button_down_sound)
        self.locks = []
        for i in range(level_num):
            self.locks.append(Image(lock, self.window, self.centers[i], 50, 50))
        self.level_data = LevelData()
        self.name = 'levelmenu'
        self.comment = None

    def draw_surface(self):
        super().draw_surface()
        for b_level in self.b_levels:
            b_level.draw()
        self.b_back.draw()
        for i in range(len(self.locks)):
            if not self.level_data.data['level_access'][i]:
                self.locks[i].draw()
        for i in range(level_num):
            if 4 <= self.level_data.data[str(i + 1)] <= 6:
                gold_star_rect = gold_star.get_rect()
                gold_star_rect.center = self.centers[0][0] - 40, self.centers[0][1] + 80
                self.window.blit(gold_star, gold_star_rect)
            elif 7 <= self.level_data.data[str(i + 1)] <= 11:
                for k in range(2):
                    gold_star_rect = gold_star.get_rect()
                    gold_star_rect.center = self.centers[i][0] + (k - 1) * 40, self.centers[i][1] + 80
                    self.window.blit(gold_star, gold_star_rect)
            elif self.level_data.data[str(i + 1)] >= 12:
                for k in range(3):
                    gold_star_rect = gold_star.get_rect()
                    gold_star_rect.center = self.centers[i][0] + (k - 1) * 40, self.centers[i][1] + 80
                    self.window.blit(gold_star, gold_star_rect)

        if self.comment:
            self.b_ok.draw()
        else:
            self.b_ok.remove()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    for b_level in self.b_levels:
                        if b_level.button_down(pos) and self.level_data.data['level_access'][
                            self.b_levels.index(b_level)
                        ]:
                            if self.comment == self.b_levels.index(b_level) + 1:
                                self.comment = None
                            else:
                                self.comment = self.b_levels.index(b_level) + 1
                    if self.b_back.button_down(pos):
                        self.running = False
                        self.comment = 'back'
                    elif self.b_ok.button_down(pos):
                        self.running = False
            pygame.display.flip()
            clock.tick(fps)


class LossPage(Surface):
    def __init__(self, window, level):
        super().__init__(window)
        self.name = 'losspage'
        self.comment = None
        self.background = loss_bg
        self.you_loss_text = you_loss
        self.you_loss_text_rect = self.you_loss_text.get_rect()
        self.you_loss_text_rect.center = (screen_center[0], screen_center[1] - 200)
        self.b_retry = AdvancedButton(replay_button, self.window, (screen_center[0] + 75, screen_center[1] + 50),
                                      100, 100, replay_buttonc, button_down_sound)
        self.b_menu = AdvancedButton(menu2_button, self.background, (screen_center[0] - 75, screen_center[1] + 50),
                                     100, 100, menu2_buttonc, button_down_sound)
        self.level = level
        loss_mus.play()

    def draw_surface(self):
        super().draw_surface()
        self.window.blit(self.you_loss_text, self.you_loss_text_rect)
        self.b_menu.draw()
        self.b_retry.draw()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.b_retry.button_down(pos)
                    self.b_menu.button_down(pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    if self.b_retry.button_up(pos):
                        self.running = False
                        self.comment = self.level
                    elif self.b_menu.button_up(pos):
                        self.comment = 'menu'
                        self.running = False
            pygame.display.flip()
            clock.tick(fps)


class WinPage(Surface):
    def __init__(self, window, level, score):
        super().__init__(window)
        self.name = 'winpage'
        self.comment = None
        self.background = win_bg
        self.b_retry = AdvancedButton(replay_button, self.window, (screen_center[0] - 150, screen_center[1] + 150), 100,
                                      100, replay_buttonc, button_down_sound)
        self.b_menu = AdvancedButton(menu2_button, self.background, (screen_center[0], screen_center[1] + 150), 100,
                                     100, menu2_buttonc, button_down_sound)
        self.b_next = AdvancedButton(next_button, self.window, (screen_center[0] + 150, screen_center[1] + 150), 100
                                     , 100, next_buttonc, button_down_sound)
        self.level = level
        self.score = score
        self.stars = Star(self.window, self.score)
        win_mus.play()
        self.save_game()

    def draw_surface(self):
        super().draw_surface()
        self.stars.draw()
        self.b_menu.draw()
        self.b_retry.draw()
        self.b_next.draw()

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.b_retry.button_down(pos)
                    self.b_menu.button_down(pos)
                    self.b_next.button_down(pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    if self.b_retry.button_up(pos):
                        self.running = False
                        self.comment = self.level
                    elif self.b_menu.button_up(pos):
                        self.comment = 'menu'
                        self.running = False
                    elif self.b_next.button_up(pos):
                        self.comment = int(self.level) + 1
                        self.running = False
            pygame.display.flip()
            clock.tick(fps)

    def save_game(self):
        for i in range(8):
            if self.level == f'{i + 1}':
                if i <= 6:
                    LevelData().get_level(i + 2)
                if self.score > LevelData().data[f'{i + 1}']:
                    LevelData().save_score(i + 1, self.score)
