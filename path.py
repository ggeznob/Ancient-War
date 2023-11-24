# get paths of fonts and images
font_path = './font/'
image_path = './img/'
ui_path = image_path + 'ui/'
cha_path = image_path + 'character/'
mus_path = './music/'
user_path = './user/'

# user
level_data_path = user_path + 'level_data.json'

# music
mus_menu = mus_path + 'menu1.ogg'
first_wave_mus = [mus_path + 'first_wave1.ogg', mus_path + 'first_wave2.ogg', mus_path + 'first_wave3.ogg']
final_wave_mus = [mus_path + 'final_wave1.ogg', mus_path + 'final_wave1.ogg', mus_path + 'final_wave1.ogg']
fight_mus = mus_path + 'fightmusic1.ogg'
win_mus = mus_path + 'win.ogg'
loss_mus = mus_path + 'loss.ogg'
negative1_mus = mus_path + 'negative1.ogg'
negative2_mus = mus_path + 'negative2.ogg'
rest_mus = mus_path + 'rest.ogg'

# sound
swordsman_attack = mus_path + 'swordsman_attack.wav'
fairy_cast = mus_path + 'fairy_cast.wav'
archmage_cast = mus_path + 'archmage_cast.wav'
infantry_hit = mus_path + 'infantry_hit.wav'
shield_hit = mus_path + 'shield_hit.wav'
shield_be_hit = mus_path + 'shield_be_hit.ogg'
king_die1 = mus_path + 'king_die1.ogg'
king_die2 = mus_path + 'king_die2.ogg'
king_die3 = mus_path + 'king_die3.ogg'

viking_hit = mus_path + 'viking_hit.wav'
elves_hit = mus_path + 'elves_hit.wav'
ogre_hit = mus_path + 'ogre_hit.wav'
barbarian_hit = mus_path + 'barbarian_hit.wav'
masker_hit = mus_path + 'masker_hit.wav'
phantom_cry = mus_path + 'phantom_cry.wav'
elementals_attack = mus_path + 'elementals_attack.wav'
phantom_attack = mus_path + 'phantom_attack.ogg'
elves_fallen = mus_path + 'elves_fallen.ogg'
phantom_laugh = mus_path + 'phantom_laugh.ogg'

arrow_hit = mus_path + 'arrow_hit.wav'
boom_sound = mus_path + 'boom.ogg'
vector_hit = mus_path + 'vector_hit.ogg'
redslash_hit = mus_path + 'redslash_hit.ogg'

coin_sound = mus_path + 'coin.ogg'
coin_fall_sound = mus_path + 'coin_fall.ogg'
pause_sound = mus_path + 'pause.ogg'
button_down_sound = mus_path + 'button_down.wav'
campfire_sound = mus_path + 'campfire.wav'
card_click = mus_path + 'card_click.ogg'
buy_mortar_sound = mus_path + 'buy_mortar.ogg'
set_tower_sound = mus_path + 'set_tower.ogg'
star_sound = mus_path + 'star_sound.ogg'

# define fonts and images
ALGER = font_path + 'ALGER.TTF'
ebrima = font_path + 'ebrima.ttf'
AGENCYB = font_path + 'AGENCYB.TTF'
gabriola = font_path + 'gabriola.ttf'

# ui
main_pages = [ui_path + 'main1.png',
              ui_path + 'main2.png',
              ui_path + 'main3.png',
              ui_path + 'main4.png',
              ui_path + 'main5.png']

level_menu = ui_path + 'levelmenu.png'
fight = ui_path + 'fighting.png'
pause_page = ui_path + 'pausepage.png'
win_page = ui_path + 'win.png'
loss_page = ui_path + 'loss.png'
you_loss = ui_path + 'you_lose.png'

button_path = ui_path + 'BTNs/'
level_buttons = {
    1: button_path + '1.png',
    2: button_path + '2.png',
    3: button_path + '3.png',
    4: button_path + '4.png',
    5: button_path + '5.png',
    6: button_path + '6.png',
    7: button_path + '7.png',
    8: button_path + '8.png',
}
back_button1 = button_path + 'back1.png'
ok_button = button_path + 'OK.png'
pause_button = button_path + 'pause.png'
start_button = button_path + 'start.png'
exit_button = button_path + 'exit.png'
menu1_button = button_path + 'menu1.png'

back_button2 = button_path + 'back2.png'
back_button2c = button_path + 'back2c.png'
continue_button = button_path + 'continue.png'
continue_buttonc = button_path + 'continuec.png'
replay_button = button_path + 'replay.png'
replay_buttonc = button_path + 'replayc.png'
next_button = button_path + 'next.png'
next_buttonc = button_path + 'nextc.png'
menu2_button = button_path + 'menu2.png'
menu2_buttonc = button_path + 'menu2c.png'

lock = ui_path + 'lock.png'
cursor = ui_path + 'cursor.png'
title = ui_path + 'title.png'
coin_box = ui_path + 'coin_box.png'
icon_image = ui_path + 'icon.ico'

# ornament
flags = [image_path + 'flag/' + '1.png', image_path + 'flag/' + '2.png', image_path + 'flag/' + '3.png',
         image_path + 'flag/' + '4.png', image_path + 'flag/' + '5.png']
campfires = [image_path + 'campfire/' + '1.png', image_path + 'campfire/' + '2.png']

# action
attacking_images = {
    'INFANTRY': cha_path + 'infantry/' + 'attacking.png',
    'ARCHER': cha_path + 'archer/' + 'shooting.png',
    'VIKING': cha_path + 'viking/' + 'attacking.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'attacking.png',
    'SHIELD': cha_path + 'shield/' + 'attacking.png',
    'OGRE': cha_path + 'ogre/' + 'attacking.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'attacking.png',
    'FAIRY': cha_path + 'fairy/' + 'healing.png',
    'MASKER': cha_path + 'masker/' + 'attacking.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'attacking.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'attacking.png',
    'MINER': cha_path + 'miner/' + 'attacking.png',
    'ELVES': cha_path + 'elves/' + 'attacking.png',
    'SWORDSMAN': cha_path + 'swordsman/' + 'attacking.png',
    'PHANTOM': cha_path + 'phantom/' + 'attacking.png'
}
dying_images = {
    'INFANTRY': cha_path + 'infantry/' + 'dying.png',
    'ARCHER': cha_path + 'archer/' + 'dying.png',
    'VIKING': cha_path + 'viking/' + 'dying.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'dying.png',
    'SHIELD': cha_path + 'shield/' + 'dying.png',
    'OGRE': cha_path + 'ogre/' + 'dying.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'dying.png',
    'FAIRY': cha_path + 'fairy/' + 'dying.png',
    'MASKER': cha_path + 'masker/' + 'dying.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'dying.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'dying.png',
    'MINER': cha_path + 'miner/' + 'dying.png',
    'ELVES': cha_path + 'elves/' + 'dying.png',
    'SWORDSMAN': cha_path + 'swordsman/' + 'dying.png',
    'PHANTOM': cha_path + 'phantom/' + 'dying.png'
}
idle_images = {
    'INFANTRY': cha_path + 'infantry/' + 'idle.png',
    'ARCHER': cha_path + 'archer/' + 'idle.png',
    'SHIELD': cha_path + 'shield/' + 'idle.png',
    'FAIRY': cha_path + 'fairy/' + 'idle.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'idle.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'idle.png',
    'MINER': cha_path + 'miner/' + 'hurt.png',
    'ELVES': cha_path + 'elves/' + 'attacking.png',
    'SWORDSMAN': cha_path + 'swordsman/' + 'idle.png'
}
walking_images = {
    'VIKING': cha_path + 'viking/' + 'walking.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'walking.png',
    'OGRE': cha_path + 'ogre/' + 'walking.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'walking.png',
    'MASKER': cha_path + 'masker/' + 'walking.png',
    'ELVES': cha_path + 'elves/' + 'walking.png',
    'PHANTOM': cha_path + 'phantom/' + 'walking.png'
}
ability_images = {
    'ELEMENTALS': cha_path + 'elementals/' + 'run_attacking.png',
    'MASKER': cha_path + 'masker/' + 'sliding.png',
    'ELVES': cha_path + 'elves/' + 'falling.png'
}

king_path = cha_path + 'king/'
king_image = [{'idle': king_path + 'king1/' + 'idle.png', 'attacking': king_path + 'king1/' + 'attacking.png',
               'dying': king_path + 'king1/' + 'dying.png'},
              {'idle': king_path + 'king2/' + 'idle.png', 'attacking': king_path + 'king2/' + 'attacking.png',
               'dying': king_path + 'king2/' + 'dying.png'},
              {'idle': king_path + 'king3/' + 'idle.png', 'attacking': king_path + 'king3/' + 'attacking.png',
               'dying': king_path + 'king3/' + 'dying.png'}]

# card
card_path = image_path + 'card/'
card_images = {'MINER': card_path + 'miner.png',
               'INFANTRY': card_path + 'infantry.png',
               'ARCHER': card_path + 'archer.png',
               'SHIELD': card_path + 'shield.png',
               'FAIRY': card_path + 'fairy.png',
               'ARCHMAGE': card_path + 'archmage.png',
               'MANIPULATOR': card_path + 'manipulator.png',
               'SWORDSMAN': card_path + 'swordsman.png'
               }
mortar_card = card_path + 'mortar.png'
# preview
preview_path = image_path + 'preview/'
pre_paths = {'INFANTRY': preview_path + 'infantry.png',
             'ARCHER': preview_path + 'archer.png',
             'SHIELD': preview_path + 'shield.png',
             'FAIRY': preview_path + 'fairy.png',
             'ARCHMAGE': preview_path + 'archmage.png',
             'MANIPULATOR': preview_path + 'manipulator.png',
             'MINER': preview_path + 'miner.png',
             'SWORDSMAN': preview_path + 'swordsman.png'}

# object
obj_path = image_path + 'object/'
coin_image = obj_path + 'coin.png'
arrow_image = obj_path + 'arrow.png'
shell_image = obj_path + 'shell.png'
boom_image = obj_path + 'boom.png'
mortar_image = obj_path + 'mortar.png'
crosshair_image = obj_path + 'crosshair.png'
elementals_slash = obj_path + 'redslash.png'
sword_slash = obj_path + 'writeslash.png'
fairy_spells = obj_path + 'fairy_spells.png'
big_spells = obj_path + 'big_spells.png'
vector_spells = obj_path + 'vector_spells.png'
green_spells = obj_path + 'green_spells.png'
write_flag = obj_path + 'writeflag.png'
live_img = obj_path + 'live.png'
grey_star = obj_path + 'grey_star.png'
gold_star = obj_path + 'gold_star.png'
