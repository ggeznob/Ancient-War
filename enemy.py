import pygame
from random import randint, random
from pygame.mixer import Sound
import math

from setting import *
from path import *
from project import collide, RedSlash, GreenSpells, collide_group

walking_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["walking"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["walking"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["walking"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["walking"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["walking"])),

    enemy_type[5]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[5]]),
                                          (enemy_size[enemy_type[5]][0],
                                           enemy_size[enemy_type[5]][1] * num_image[enemy_type[5]]["walking"])),

    enemy_type[6]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[6]]),
                                          (enemy_size[enemy_type[6]][0],
                                           enemy_size[enemy_type[6]][1] * num_image[enemy_type[6]]["walking"]))}

attack_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["attacking"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["attacking"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["attacking"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["attacking"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["attacking"])),

    enemy_type[5]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[5]]),
                                          (enemy_size[enemy_type[5]][0],
                                           enemy_size[enemy_type[5]][1] * num_image[enemy_type[5]]["attacking"])),

    enemy_type[6]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[6]]),
                                          (enemy_size[enemy_type[6]][0],
                                           enemy_size[enemy_type[6]][1] * num_image[enemy_type[6]]["attacking"]))}

dying_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["dying"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["dying"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["dying"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["dying"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["dying"])),

    enemy_type[5]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[5]]),
                                          (enemy_size[enemy_type[5]][0],
                                           enemy_size[enemy_type[5]][1] * num_image[enemy_type[5]]["dying"])),

    enemy_type[6]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[6]]),
                                          (enemy_size[enemy_type[6]][0],
                                           enemy_size[enemy_type[6]][1] * num_image[enemy_type[6]]["dying"]))}

ability_all_image = {
    enemy_type[3]: pygame.transform.scale(pygame.image.load(ability_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["run_attacking"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(ability_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["sliding"])),

    enemy_type[5]: pygame.transform.scale(pygame.image.load(ability_images[enemy_type[5]]),
                                          (enemy_size[enemy_type[5]][0],
                                           enemy_size[enemy_type[5]][1] * num_image[enemy_type[5]]["falling"]))
}


elves_hit = Sound(elves_hit)
elves_hit.set_volume(0.2)
ogre_hit = Sound(ogre_hit)
ogre_hit.set_volume(0.2)
viking_hit = Sound(viking_hit)
viking_hit.set_volume(0.2)
barbarian_hit = Sound(barbarian_hit)
barbarian_hit.set_volume(0.2)
masker_hit = Sound(masker_hit)
masker_hit.set_volume(0.2)
phantom_cry = Sound(phantom_cry)
phantom_cry.set_volume(0.2)
elementals_attack = Sound(elementals_attack)
elementals_attack.set_volume(0.2)
phantom_attack = Sound(phantom_attack)
phantom_attack.set_volume(0.2)
elves_fallen = Sound(elves_fallen)
elves_fallen.set_volume(0.6)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, enemy_size[self.name][0], enemy_size[self.name][1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.walking_all_image = walking_all_image[self.name]
        self.attacking_all_image = attack_all_image[self.name]
        self.dying_all_image = dying_all_image[self.name]
        self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
        # value
        self.HP = HP_value[self.name]
        self.damage = damage_value[self.name]
        self.move_speed = move_speed[self.name] + randint(-100 * move_speed[self.name],
                                                          100 * move_speed[self.name]) / 1000
        self.p_drop = p_drop[self.name]
        self.live = True
        self.state = "walking"
        self.last_attack_time = 0

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]


class Viking(Enemy):
    def __init__(self):
        self.name = 'VIKING'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size['VIKING'][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
                self.y = 0
            if self.y == 1000:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        viking_hit.play()
        if soldier.name == 'ARCHER':
            soldier.take_damage(self.damage * 2)
        else:
            soldier.take_damage(self.damage)


class Barbarian(Enemy):
    def __init__(self):
        self.name = 'BARBARIAN'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size['BARBARIAN'][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 30
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
                self.y = 0
            if self.y == 1100:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        barbarian_hit.play()
        if soldier.name == 'MANIPULATOR':
            soldier.take_damage(self.damage * 2)
        else:
            soldier.take_damage(self.damage)


class Elementals(Enemy):
    def __init__(self):
        self.name = 'ELEMENTALS'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[3]][1]
        super().__init__()
        self.ability_all_image = ability_all_image[self.name]

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "run_attacking":
            if self.y < self.ability_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles):
        if self.live:
            collide_opponent = collide(self, opponents, 0.5)
            if collide_opponent:
                if self.state != 'attacking':
                    self.state = 'attacking'
                    self.y = 0
                if self.y == 700:
                    elementals_attack.play()
                    self.attack(collide_opponent)
            else:
                if self.spot(opponents):
                    if self.state != "run_attacking":
                        self.state = "run_attacking"
                    if self.y == 600:
                        elementals_attack.play()
                        self.run_attack(projectiles)
                else:
                    if self.state != 'walking':
                        self.state = 'walking'
        self.update_image()

    def move(self):
        if self.state == 'run_attacking':
            self.rect_x -= (self.move_speed - 0.25)
        elif self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        if soldier.name == 'SHIELD':
            soldier.take_damage(self.damage * 2)
        else:
            soldier.take_damage(self.damage)

    def run_attack(self, projectiles):
        slash = RedSlash(self.rect_x, self.rect_y, self.damage)
        projectiles.add(slash)

    def spot(self, opponent_group):
        if self.live:
            for enemy in opponent_group:
                if -20 <= self.rect_y - enemy.rect_y <= 20 and self.rect_x <= enemy.rect_x + attack_range[self.name]:
                    return True


class Masker(Enemy):
    def __init__(self):
        self.name = 'MASKER'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[4]][1]
        super().__init__()
        self.ability_all_image = ability_all_image[self.name]
        self.state = 'sliding'

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "sliding":
            if self.y < self.ability_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        if self.live:
            opponent = collide(self, opponents, 0.5)
            if opponent:
                if self.state == 'sliding':
                    self.attack(opponent)
                    self.state = 'attacking'
                    self.y = 0
                else:
                    if self.state != 'attacking':
                        self.state = 'attacking'
                        self.y = 0
                    if self.y == 460:
                        masker_hit.play()
                    if self.y == 600:
                        self.attack(opponent)
            else:
                if self.state != 'sliding':
                    if self.state != "walking":
                        self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'sliding':
            self.rect_x -= self.move_speed * 3
        elif self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        if self.state == 'sliding':
            if soldier.name == 'SWORDSMAN':
                soldier.take_damage(self.damage * 20)
            else:
                soldier.take_damage(self.damage * 10)
        else:

            if soldier.name == 'SWORDSMAN':
                soldier.take_damage(self.damage * 2)
            else:
                soldier.take_damage(self.damage)


class Ogre(Enemy):
    def __init__(self):
        self.name = 'OGRE'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[2]][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.3)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
                self.y = 0

            if self.y == 500:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        ogre_hit.play()
        if soldier.name == 'ARCHMAGE':
            soldier.take_damage(self.damage * 2)
        else:
            soldier.take_damage(self.damage)


class Elves(Enemy):
    def __init__(self):
        self.name = 'ELVES'
        self.y = randint(0, num_image[self.name]['falling'] - 1) * enemy_size[enemy_type[5]][1]
        super().__init__()
        self.ability_all_image = ability_all_image[self.name]
        self.state = 'falling'
        self.landing_y = rows[randint(0, 3)]
        self.distance = 0
        self.falling_speed = 0

    def update_image(self):
        if self.state == "falling":
            if self.y < self.ability_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.3)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
                self.y = 0
            if self.y == 1000:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'falling':
            self.rect_y += self.falling_speed
            if self.rect_y >= self.landing_y:
                self.state = 'walking'
                elves_fallen.play()
        elif self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def attack(self, soldier):
        elves_hit.play()
        if soldier.name == 'FAIRY':
            soldier.take_damage(self.damage * 2)
        else:
            soldier.take_damage(self.damage)

    def set(self, pos):
        super().set(pos)
        self.distance = self.landing_y - self.rect_y
        self.falling_speed = self.distance * 0.005


class Phantom(Enemy):
    def __init__(self):
        self.name = 'PHANTOM'
        self.y = 100
        super().__init__()
        self.pace = 0
        self.state = 'incorporeal'
        self.action = 'walking'
        self.change_state = randint(-100, 200)
        self.change_time = randint(150, 250)
        self.origin_x, self.origin_y = 0, 0
        self.p_blink = randint(8, 15) / 100
        self.p_disappear = randint(5, 8) / 100
        self.max_alpha = 150
        self.min_alpha = 10
        self.alpha_num = 0
        self.t = randint(0, 100)
        self.stop = False

    def update_image(self):
        if self.action == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.pace += 1
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.action == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.stop = False
                self.action = 'walking'
                self.y = 100
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.action == "dying":
            self.stop = True
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

        if self.state == 'incorporeal':
            random_num = random()
            if random_num < self.p_blink:
                self.rect_x, self.rect_y = self.origin_x + randint(-20, 20), self.origin_y + randint(-20, 20)
                self.alpha_num = randint(0, self.max_alpha // 2)
            random_num = random()
            if random_num < self.p_disappear:
                self.alpha_num = 0
            self.image.set_alpha(self.alpha_num)
        if self.state == 'corporeal':
            self.t += 1
            self.image.set_alpha(max(self.min_alpha, int(self.max_alpha * (0.5 + math.sin(0.05 * self.t) / 2.0))))
            self.rect_x, self.rect_y = self.origin_x, self.origin_y
        self.move()

    def update(self, opponents, projectiles):
        if self.live:
            end_x = self.spot(opponents)
            if end_x and self.pace >= 4 and self.state == 'corporeal':
                self.stop = True
                if self.action != 'attacking':
                    self.action = 'attacking'
                    self.y = 0
                if self.y == 0:
                    phantom_attack.play()
                if self.y == 7 * self.height:
                    self.avada(projectiles, end_x)
                    self.pace = 0

            self.change_state += 1
            if self.change_state >= self.change_time and self.state == 'incorporeal':
                self.state = 'corporeal'
                self.change_state = 0
            elif self.change_state >= 2 * self.change_time and self.state == 'corporeal' and self.action != 'attacking':
                self.state = 'incorporeal'
                self.change_state = 0

        self.update_image()

    def set(self, pos):
        super().set(pos)
        phantom_cry.play()
        self.origin_x, self.origin_y = pos

    def move(self):
        if not self.stop:
            self.rect_x -= self.move_speed
            self.origin_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        if self.rect_x <= -50:
            self.kill()

    def take_damage(self, damage):
        if self.state != 'incorporeal':
            if damage <= -75:
                damage = -75
            self.HP += damage
        if self.HP <= 0:
            self.live = False

    def avada(self, projectiles, end_x):
        spells = GreenSpells(self.origin_x, self.origin_y, self.damage, end_x)
        projectiles.add(spells)

    def spot(self, opponent_group):
        if self.live:
            min_x = screen_width
            for enemy in opponent_group:
                if -20 <= self.rect_y - enemy.rect_y <= 20 and self.rect_x >= enemy.rect_x + 20:
                    if min_x > enemy.rect_x:
                        min_x = enemy.rect_x
            return min_x
