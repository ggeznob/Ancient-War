import pygame
import sys

from level import Level, Level8
from surface import MainPage, LevelMenu, WinPage, LossPage
from setting import *
from path import *

cursor_image = pygame.image.load(cursor)
image_cursor = pygame.cursors.Cursor((0, 0), cursor_image)
icon = pygame.image.load(icon_image)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Ancient War")
        self.clock = pygame.time.Clock()
        self.stage = MainPage(self.window)
        pygame.mouse.set_cursor(image_cursor)
        pygame.display.set_icon(icon)

    def playing(self):
        self.stage.game_loop()
        self.window.fill((0, 0, 0))
        pygame.mixer.music.stop()

        for i in range(1, 9):
            if self.stage.name == str(i):
                if self.stage.comment == 'back':
                    self.stage = LevelMenu(self.window)
                    self.playing()
                elif self.stage.comment == 'loss':
                    self.stage = LossPage(self.window, self.stage.name)
                    self.playing()
                elif self.stage.comment == 'win':
                    self.stage = WinPage(self.window, self.stage.name, self.stage.score)
                    self.playing()
                elif self.stage.comment == 'replay':
                    if i <= 7:
                        self.stage = Level(self.window, i)
                    else:
                        self.stage = Level8(self.window)
                    self.playing()

        if self.stage.name == 'mainpage':
            if self.stage.comment == 'levelmenu':
                self.stage = LevelMenu(self.window)
                self.playing()
            elif self.stage.comment == 'quit':
                pygame.quit()
                sys.exit()

        elif self.stage.name == 'levelmenu':
            if self.stage.comment == 'back':
                self.stage = MainPage(self.window)
                self.playing()
            for i in range(1, 9):
                if self.stage.comment == i and i <= 7:
                    self.stage = Level(self.window, i)
                    self.playing()
                elif self.stage.comment == i and i == 8:
                    self.stage = Level8(self.window)
                    self.playing()

        elif self.stage.name == 'losspage':
            if self.stage.comment == 'menu':
                self.stage = LevelMenu(self.window)
                self.playing()
            for i in range(1, 9):
                i = str(i)
                if self.stage.comment == str(i) and i <= '7':
                    self.stage = Level(self.window, i)
                    self.playing()
                elif self.stage.comment == str(i) and i == '8':
                    self.stage = Level8(self.window, )
                    self.playing()

        elif self.stage.name == 'winpage':
            for i in range(1, 9):
                i = str(i)
                if self.stage.comment == str(i) and i <= '7':
                    self.stage = Level(self.window, i)
                    self.playing()
                elif self.stage.comment == str(i) and i == '8':
                    self.stage = Level8(self.window)
                    self.playing()
            if self.stage.comment == 'menu':
                self.stage = LevelMenu(self.window)
                self.playing()


if __name__ == '__main__':
    game = Game()
    game.playing()
