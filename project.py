import pygame
from pygame.mixer import Sound
from math import sin

from utils import Button, Image
from random import randint
from setting import *
from path import *

coin_all_image = pygame.transform.scale(pygame.image.load(coin_image), (coin_size[0], coin_size[1] * 6))
smallcoin_all_image = pygame.transform.scale(pygame.image.load(coin_image),
                                             (small_coin_size[0], small_coin_size[1] * 6))
boom_all_image = pygame.transform.scale(pygame.image.load(boom_image), (boom_size[0] * 7, boom_size[1]))

projectile_image = {'arrow': pygame.transform.scale(pygame.image.load(arrow_image), arrow_size),
                    'shell': pygame.transform.scale(pygame.image.load(shell_image), shell_size),
                    'ele_slash': pygame.transform.scale(pygame.image.load(elementals_slash), slash_size),
                    'fairy_spells': pygame.transform.scale(pygame.image.load(fairy_spells), spells_size),
                    'big_spells': pygame.transform.scale(pygame.image.load(big_spells),
                                                         (spells_size[0] * 1.5, spells_size[1] * 1.5)),
                    'vector_spells': pygame.transform.scale(pygame.image.load(vector_spells), spells_size),
                    'sword_slash': pygame.transform.scale(pygame.image.load(sword_slash), slash_size),
                    'green_spells': pygame.transform.scale(pygame.image.load(green_spells), spells_size)}

flags_image = [pygame.transform.scale(pygame.image.load(flags[0]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[1]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[2]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[3]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[4]), (flag_size[0] * 6, flag_size[1]))]
flag_x = [randint(424, 586), randint(606, 768), randint(788, 950), randint(1114, 1240), randint(566, 804),
          randint(1138, 1186)]
flag_y = [randint(148, 206), randint(100, 171), randint(163, 183)]

campfires_image = [pygame.transform.scale(pygame.image.load(campfires[0]), (campfire_size[0] * 6, campfire_size[1])),
                   pygame.transform.scale(pygame.image.load(campfires[1]),
                                          (campfire_size[0] * 6, campfire_size[1] / 2))]

small_gold_star = pygame.transform.scale(pygame.image.load(gold_star), small_star_size)
big_gold_star = pygame.transform.scale(pygame.image.load(gold_star), big_star_size)

arrow_hit = Sound(arrow_hit)
arrow_hit.set_volume(0.2)
boom_sound = Sound(boom_sound)
boom_sound.set_volume(0.5)
vector_hit = Sound(vector_hit)
vector_hit.set_volume(0.2)
redslash_hit = Sound(redslash_hit)
redslash_hit.set_volume(0.5)

coin_sound = Sound(coin_sound)
coin_sound.set_volume(0.3)
coin_fall_sound = Sound(coin_fall_sound)
coin_fall_sound.set_volume(0.3)
star_sound = Sound(star_sound)
star_sound.set_volume(0.7)


class Coin(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, coin_size[0], coin_size[1]
        self.end_point = coin_box_pos
        self.dx = self.end_point[0] - self.rect_x
        self.dy = self.end_point[1] - self.rect_y
        self.distance = pygame.math.Vector2(self.dx, self.dy).length()
        self.speed = 0.02 * self.distance
        self.all_image = coin_all_image
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.direction = pygame.math.Vector2(self.dx, self.dy).normalize()
        self.move = self.direction * self.speed
        self.click = Button((self.rect_x, self.rect_y), coin_size[0] * 1.2, coin_size[1] * 1.2)
        self.clicked = False
        self.money = 50
        self.bling_time = 10
        self.start_time = pygame.time.get_ticks()
        self.bling = False
        self.t = 0
        coin_fall_sound.play()

    def update(self, coin, pos=None):
        if self.y < self.all_image.get_rect().h:
            if self.y % self.height == 0:
                self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
            self.y += 10
        else:
            self.y = 0
            self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
        if pos and not self.clicked:
            if self.click.button_down(pos):
                coin_sound.play()
                self.clicked = True
        if self.clicked:
            self.image.set_alpha(255)
            self.rect_x += self.move.x
            self.rect_y += self.move.y
            self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
            self.get(coin)
        else:
            if not self.bling and pygame.time.get_ticks() - self.start_time >= 1000 * self.bling_time:
                self.bling = True
                self.start_time = pygame.time.get_ticks()
            if self.bling:
                self.t += 2
                alpha = 50 + int(200 * (0.5 + sin(0.05 * self.t) / 2))
                self.image.set_alpha(alpha)
                if pygame.time.get_ticks() - self.start_time >= 1000 * self.bling_time:
                    self.kill()

    def get(self, coin):
        if self.rect_x <= self.end_point[0] and self.rect_y <= self.end_point[1]:
            coin.change(self.money)
            self.kill()


class SmallCoin(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, small_coin_size[0], small_coin_size[1]
        self.end_point = coin_box_pos
        self.dx = self.end_point[0] - self.rect_x
        self.dy = self.end_point[1] - self.rect_y
        self.distance = pygame.math.Vector2(self.dx, self.dy).length()
        self.speed = 0.02 * self.distance
        self.all_image = smallcoin_all_image
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.direction = pygame.math.Vector2(self.dx, self.dy).normalize()
        self.move = self.direction * self.speed
        self.click = Button((self.rect_x, self.rect_y), small_coin_size[0] * 1.2, small_coin_size[1] * 1.2)
        self.clicked = False
        self.money = 10
        self.bling_time = 10
        self.start_time = pygame.time.get_ticks()
        self.bling = False
        self.t = 0
        coin_fall_sound.play()

    def update(self, coin, pos=None):
        if self.y < self.all_image.get_rect().h:
            if self.y % self.height == 0:
                self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
            self.y += 7
        else:
            self.y = 0
            self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
        if pos and not self.clicked:
            if self.click.button_down(pos):
                coin_sound.play()
                self.clicked = True
        if self.clicked:
            self.image.set_alpha(255)
            self.rect_x += self.move.x
            self.rect_y += self.move.y
            self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
            self.get(coin)
        else:
            if not self.bling and pygame.time.get_ticks() - self.start_time >= 1000 * self.bling_time:
                self.bling = True
                self.start_time = pygame.time.get_ticks()
            if self.bling:
                self.t += 2
                alpha = 50 + int(200 * (0.5 + sin(0.05 * self.t) / 2))
                self.image.set_alpha(alpha)
                if pygame.time.get_ticks() - self.start_time >= 1000 * self.bling_time:
                    self.kill()

    def get(self, coin):
        if self.rect_x <= self.end_point[0] and self.rect_y <= self.end_point[1]:
            coin.change(self.money)
            self.kill()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, arrow_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, arrow_size[0], arrow_size[1]
        self.speed = 20
        self.image = projectile_image['arrow']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = arrow_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)
        if self.rect_x >= screen_width + self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        enemy_group = [sprite for sprite in enemy_group if sprite.state != ('falling' and 'incorporeal')]
        target = collide(self, enemy_group, 0.5)
        if target:
            arrow_hit.play()
            if target.name == 'BARBARIAN':
                target.take_damage(self.damage * 2)
            else:
                target.take_damage(self.damage)
            self.kill()


class RedSlash(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, slash_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], slash_size[1]
        self.speed = 7
        self.image = projectile_image['ele_slash']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = slash_damage

    def update(self, enemy_group):
        self.rect_x -= self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)
        if self.rect_x <= -self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        target = collide(self, enemy_group, 0.3)
        if target:
            redslash_hit.play()
            if target.name == 'SHIELD':
                target.take_damage(self.damage * 2)
            else:
                target.take_damage(self.damage)
            self.kill()


class WriteSlash(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, slash_damage, direction):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], slash_size[1]
        self.speed = 7
        self.image = projectile_image['sword_slash']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = slash_damage
        self.direction = pygame.math.Vector2(1, direction - 1).normalize()
        self.move = self.direction * self.speed

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.move.x
        self.rect_y += self.move.y
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)
        if self.rect_x >= screen_width + self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        enemy_group = [sprite for sprite in enemy_group if sprite.state != ('falling' and 'incorporeal')]
        target = collide(self, enemy_group, 0.3)
        if target:
            if target.name == 'ELVES':
                target.take_damage(self.damage * 2)
            else:
                target.take_damage(self.damage)
            self.kill()


class FairySpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, end_point, spells_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], spells_size[1]
        self.end_pos = end_point
        self.speed = 5
        self.image = projectile_image['fairy_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage
        self.direction = pygame.math.Vector2(end_point[0] - self.rect_x, end_point[1] - self.rect_y).normalize()
        self.move = self.direction * self.speed

    def update(self, enemy_group=None, tower_group=None):
        self.rect_x += self.move.x
        self.rect_y += self.move.y
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if (self.move.x > 0 and self.rect_x >= self.end_pos[0]) or (
                self.move.x < 0 and self.rect_x <= self.end_pos[0]):
            if (self.move.y > 0 and self.rect_y >= self.end_pos[1]) or (
                    self.move.y < 0 and self.rect_y <= self.end_pos[1]):
                self.hit(tower_group)

    def hit(self, tower_group):
        filtered_sprites = [sprite for sprite in tower_group if sprite.name != "FAIRY"]
        target = collide(self, filtered_sprites, 0.5)
        if target:
            if target.live:
                target.take_damage(self.damage)
        self.kill()


class BigSpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, spells_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, spells_size[0] * 1.5, spells_size[1] * 1.5
        self.speed = 5
        self.image = projectile_image['big_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)
        if self.rect_x >= screen_width + self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        enemy_group = [sprite for sprite in enemy_group if sprite.state != ('falling' and 'incorporeal')]
        target = collide(self, enemy_group, 0.1)
        if target:
            targets = [sprite for sprite in enemy_group if self.rect_x - 30 <= sprite.rect_x <= self.rect_x + 30]
            targets = [sprite for sprite in targets if self.rect_y - 20 <= sprite.rect_y <= self.rect_y + 20]
            for enemy in targets:
                if enemy.name == 'OGRE':
                    enemy.take_damage(self.damage * 2)
                else:
                    enemy.take_damage(self.damage)
            self.kill()


class VectorSpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, spells_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, spells_size[0], spells_size[1]
        self.speed = 8
        self.image = projectile_image['vector_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage
        self.distance = ability_value['vectorspells_distance']

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)
        if self.rect_x >= screen_width + self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        enemy_group = [sprite for sprite in enemy_group if sprite.state != ('falling' and 'incorporeal')]
        target = collide(self, enemy_group, 0.5)
        if target:
            vector_hit.play()
            if target.name == 'PHANTOM':
                target.take_damage(self.damage * 3)
                target.origin_x += self.distance * target.move_speed
            else:
                target.take_damage(self.damage)
                if target.state != 'attacking':
                    target.rect_x += randint(self.distance // 2, self.distance) * target.move_speed
            self.kill()


class GreenSpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, spells_damage, end_x):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, spells_size[0], spells_size[1]
        self.speed = 5
        self.end_x = end_x
        self.image = projectile_image['green_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x -= self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= self.end_x:
            self.hit(enemy_group)
        if self.rect_x <= -self.width / 2:
            self.kill()

    def hit(self, enemy_group):
        enemy_group = [sprite for sprite in enemy_group if sprite.name != 'KING']
        target = collide(self, enemy_group, 0.3)
        if target:
            target.take_damage(self.damage)
            self.kill()


class Shell(pygame.sprite.Sprite):
    def __init__(self, start_x, spells_damage, end_y):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, -20, spells_size[0], spells_size[1]
        self.speed = 4
        self.end_y = end_y
        self.image = projectile_image['shell']
        self.boom_width, self.boom_height = boom_size[0], boom_size[1]
        self.boom_all_image = boom_all_image
        self.x = 0
        self.boom = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage

    def update(self, enemy_group, tower_group=None):
        if not self.boom:
            self.rect_y += self.speed
            self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
            if self.rect_y >= self.end_y - 35:
                self.image = self.boom_all_image.subsurface((self.x, 0, self.boom_width, self.boom_height))
                self.boom = True
                self.rect = self.image.get_rect()
                self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y + 35))
                boom_sound.play()
                self.hit(enemy_group)
        else:
            if self.x < self.boom_all_image.get_rect().w:
                if self.x % self.boom_width == 0:
                    self.image = self.boom_all_image.subsurface((self.x, 0, self.boom_width, self.boom_height))
                self.x += 20
            else:
                self.kill()

    def hit(self, enemies):
        enemies = [sprite for sprite in enemies if sprite.state != ('falling' and 'incorporeal')]
        target = collide_group(self, enemies, 0.5)
        if target:
            for enemy in target:
                enemy.take_damage(self.damage)


class Star:
    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.left_center = (screen_center[0] - 230, screen_center[1] - 100)
        self.middle_center = (screen_center[0], screen_center[1] - 150)
        self.right_center = (screen_center[0] + 230, screen_center[1] - 100)
        self.small_grey_star_img1 = Image(grey_star, self.window, self.left_center, small_star_size[0],
                                          small_star_size[1])
        self.small_grey_star_img2 = Image(grey_star, self.window, self.right_center, small_star_size[0],
                                          small_star_size[1])
        self.big_grey_star_img = Image(grey_star, self.window, self.middle_center, big_star_size[0], big_star_size[1])

        self.small_gold_star_img1 = small_gold_star
        self.star1_rect = self.small_gold_star_img1.get_rect()
        self.star1_rect.center = self.left_center

        self.small_gold_star_img2 = small_gold_star
        self.star2_rect = self.small_gold_star_img2.get_rect()
        self.star2_rect.center = self.right_center

        self.big_gold_star_img = big_gold_star
        self.big_star_rect = self.big_gold_star_img.get_rect()
        self.big_star_rect.center = self.middle_center

        self.stars = [self.small_gold_star_img1, self.big_gold_star_img, self.small_gold_star_img2]
        self.stars_rect = [self.star1_rect, self.big_star_rect, self.star2_rect]

        self.has_sound = [False, False, False]
        self.sound = star_sound

        self.popped = [False] * 3
        self.pop_time = 0.3
        self.start_time = pygame.time.get_ticks()

    def draw(self):
        self.small_grey_star_img1.draw()
        self.small_grey_star_img2.draw()
        self.big_grey_star_img.draw()
        if not self.popped[0] and self.score > 3:
            if not self.has_sound[0]:
                self.sound.play()
                self.has_sound[0] = True
            self.pop_star(1)
        elif not self.popped[1] and self.score > 6:
            if not self.has_sound[1]:
                self.sound.play()
                self.has_sound[1] = True
            self.pop_star(2)
        elif not self.popped[2] and self.score >= 12:
            if not self.has_sound[2]:
                self.sound.play()
                self.has_sound[2] = True
            self.pop_star(3)
        for i in range(3):
            if self.popped[i]:
                self.window.blit(self.stars[i], self.stars_rect[i])

    def pop_star(self, num):
        current_time = pygame.time.get_ticks()
        fraction = (current_time - self.start_time) / (self.pop_time * 1000)
        if fraction >= 1:
            fraction = 1
        if num == 1:
            self.small_gold_star_img1 = pygame.transform.scale(small_gold_star,
                                                               (small_star_size[0] * fraction,
                                                                small_star_size[1] * fraction))
            self.star1_rect = self.small_gold_star_img1.get_rect()
            self.star1_rect.center = self.left_center
            self.window.blit(self.small_gold_star_img1, self.star1_rect)
            if fraction == 1:
                self.popped[0] = True
                self.start_time = pygame.time.get_ticks()
        elif num == 3:
            self.small_gold_star_img2 = pygame.transform.scale(small_gold_star,
                                                               (small_star_size[0] * fraction,
                                                                small_star_size[1] * fraction))
            self.star2_rect = self.small_gold_star_img2.get_rect()
            self.star2_rect.center = self.right_center
            self.window.blit(self.small_gold_star_img2, self.star2_rect)
            if fraction == 1:
                self.popped[2] = True
                self.start_time = pygame.time.get_ticks()
        elif num == 2:
            self.big_gold_star_img = pygame.transform.scale(big_gold_star,
                                                            (big_star_size[0] * fraction, big_star_size[1] * fraction))
            self.big_star_rect = self.big_gold_star_img.get_rect()
            self.big_star_rect.center = self.middle_center
            self.window.blit(self.big_gold_star_img, self.big_star_rect)
            if fraction == 1:
                self.popped[1] = True
                self.start_time = pygame.time.get_ticks()


class Flag(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.number = num
        if self.number == 5:
            self.all_image = flags_image[randint(0, 2)]
        else:
            self.all_image = flags_image[self.number]
        self.width, self.height = flag_size[0], flag_size[1]
        if self.number <= 4:
            if self.number == 4:
                self.rect = pygame.Rect(flag_x[self.number], flag_y[1], self.width, self.height)
            else:
                self.rect = pygame.Rect(flag_x[self.number], flag_y[0], self.width, self.height)
        else:
            self.rect = pygame.Rect(flag_x[self.number], flag_y[2], self.width, self.height)
        self.x = randint(0, 5) * self.width
        self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))

    def update(self):
        if self.x < self.all_image.get_rect().w:
            if self.x % self.width == 0:
                self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))
            self.x += 10
        else:
            self.x = 0
            self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))


class Campfire(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.number = num
        self.all_image = campfires_image[self.number]
        if self.number:
            self.width, self.height = campfire_size[0], campfire_size[1] / 2
        else:
            self.width, self.height = campfire_size[0], campfire_size[1]
        self.rect = pygame.Rect(campfire_x, campfire_y[self.number], self.width, self.height)
        self.x = 0
        self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))

    def update(self):
        if self.x < self.all_image.get_rect().w:
            if self.x % self.width == 0:
                self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))
            self.x += 5
        else:
            self.x = 0
            self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))


def collide(sprite, sprite_group, extent):
    collide_circle_small_ratio = pygame.sprite.collide_circle_ratio(extent)
    for spr in sprite_group:
        if collide_circle_small_ratio(sprite, spr):
            return spr


def collide_group(sprite, sprite_group, extent):
    collide_circle_large_ratio = pygame.sprite.collide_circle_ratio(extent)
    target = []
    for spr in sprite_group:
        if collide_circle_large_ratio(sprite, spr):
            target.append(spr)
    return target
