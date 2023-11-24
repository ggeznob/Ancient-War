# initialize inventory
init_coin = {
    '1': 50, '2': 50, '3': 50, '4': 50, '5': 50, '6': 50, '7': 100, '8': 150
}

HP_value = {"INFANTRY": 150, "ARCHER": 150, "SHIELD": 500, "VIKING": 250, "BARBARIAN": 150,
            'OGRE': 500, 'KING': 150, 'ELEMENTALS': 200, 'FAIRY': 150, 'MASKER': 200,
            'ARCHMAGE': 150, 'MANIPULATOR': 200, 'MINER': 200, 'ELVES': 250, 'SWORDSMAN': 250,
            'PHANTOM': 300
            }
damage_value = {"INFANTRY": -8, "ARCHER": -10, "SHIELD": -3, "VIKING": -10, "BARBARIAN": -8,
                'OGRE': -8, 'KING': -10, 'ELEMENTALS': -15, 'FAIRY': 15, 'MASKER': -12,
                'ARCHMAGE': -15, 'MANIPULATOR': -6, 'MINER': 0, 'ELVES': -15, 'SWORDSMAN': -12,
                'PHANTOM': -150, "MORTAR": -100
                }
ability_value = {'infantry_attack_per_coin': 3, 'miner_time_per_coin': 20, 'vectorspells_distance': 20,
                 'infantry_max_coin': 5
                 }
attack_range = {"ELEMENTALS": 300, 'SWORDSMAN': 400}

# my soldier value
cost_value = {"INFANTRY": -50, "ARCHER": -75, "SHIELD": -75, 'FAIRY': -150, 'ARCHMAGE': -250,
              'MANIPULATOR': -125, "MORTAR": -500, 'MINER': -50, 'SWORDSMAN': -250}

cd_value = {"INFANTRY": 5, "ARCHER": 5, "SHIELD": 15, 'FAIRY': 20, 'ARCHMAGE': 10, 'MANIPULATOR': 15,
            'MINER': 5, 'SWORDSMAN': 15, "SHELL": 25}

cd_init = {"INFANTRY": False, "ARCHER": True, "SHIELD": False, 'FAIRY': False, 'ARCHMAGE': True,
           'MANIPULATOR': True, 'MINER': True, 'SWORDSMAN': False, "MORTAR": False}

# enemy value
move_speed = {"VIKING": 0.5, "BARBARIAN": 0.9, 'OGRE': 0.4, 'ELEMENTALS': 0.5, 'MASKER': 0.5,
              'ELVES': 0.7, 'PHANTOM': 0.35}

p_drop = {"VIKING": 0.01, "BARBARIAN": 0.01, 'OGRE': 0.15, 'ELEMENTALS': 0.15, 'MASKER': 0.15,
          'ELVES': 0.12, 'PHANTOM': 0.25}

# tips
tips = ['Try to resist the phantom with the manipulator!',
        'Make sure to protect the fairy',
        'Infantry is a good choice for the early game.',
        'Maskers slides deal a significant amount of damage! Be carefully!',
        'Mortars can inflict substantial damage on large groups of enemies',
        "Don't think you can hide in the back and escape notice...",
        "Mortar? I don't know what that is...",
        'Nobody can work while getting hit',
        'In order to earn three stars, only when the king is unharmed',
        'In China, there is an ancient saying: "One counters one."']

# ui and map
screen_width, screen_height = 1280, 720
screen_center = (screen_width / 2, screen_height / 2)
map_point1, map_point2 = (160, 280), (1150, 680)
campfire_x, campfire_y = 30, [380, 580]
coin_box_pos = (100, 90)
mortar_box_pos = (145, 160)
flag_pos = (60, 160)
mortar_pos = (680, 160)
num_row, num_column = 4, 11
rows = [330, 430, 530, 630]
tip_pos = (60, 660)

# fps
fps = 60

# size
flag_size = (65, 130)
campfire_size = (65, 130)
character_size = (100, 100)
tower_size = {'ARCHER': (character_size[0], character_size[1]),
              'SHIELD': (character_size[0] * 1.3, character_size[1] * 1.3),
              'INFANTRY': (character_size[0] * 1.2, character_size[1] * 1.2),
              'FAIRY': (character_size[0], character_size[1]),
              'ARCHMAGE': (character_size[0], character_size[1]),
              'MANIPULATOR': (character_size[0], character_size[1]),
              'MINER': (character_size[0], character_size[1]),
              'SWORDSMAN': (character_size[0] * 1.2, character_size[1] * 1.2)}
king_size = (character_size[0] * 1.2, character_size[1] * 1.2)

enemy_size = {'VIKING': (character_size[0] * 1.2, character_size[1] * 1.2),
              'BARBARIAN': (character_size[0] * 1.2, character_size[1] * 1.2),
              'OGRE': (character_size[0] * 1.4, character_size[1] * 1.2),
              'ELEMENTALS': (character_size[0] * 1.2, character_size[1] * 1.2),
              'MASKER': (character_size[0] * 1.2, character_size[1] * 1.2),
              'ELVES': (character_size[0] * 1.2, character_size[1] * 1.2),
              'PHANTOM': (character_size[0] * 1.2, character_size[1] * 1.2)
              }
card_size = (130, 155)
arrow_size = (32, 10)
shell_size = (40, 146)
boom_size = (200, 200)
slash_size = (75, 75)
spells_size = (25, 25)
coin_box_size = (160, 45)
coin_size = (50, 50)
small_coin_size = (35, 35)
box_size = (70, 70)
cell_size = (90, 100)
crosshair_size = (100, 100)
write_flag_size = (80, 80)
tip_size = 50
heart_size = (30, 30)
small_star_size = (140, 140)
big_star_size = (180, 180)

# define soldiers' attribution
tower_type = ['INFANTRY', 'ARCHER', 'SHIELD', 'FAIRY', 'ARCHMAGE', 'MANIPULATOR', 'MINER', 'SWORDSMAN', 'MORTAR',
              'KING']
enemy_type = ['VIKING', 'BARBARIAN', 'OGRE', 'ELEMENTALS', 'MASKER', 'ELVES', 'PHANTOM']

num_image = {
    "INFANTRY": {"idle": 12, "attacking": 12, "dying": 15},
    "ARCHER": {"idle": 12, "shooting": 15, "dying": 15},
    'KING': {"idle": 12, "attacking": 12, "dying": 15},
    "BARBARIAN": {"walking": 18, "attacking": 12, "dying": 9},
    'VIKING': {"walking": 18, "attacking": 12, "dying": 15},
    "SHIELD": {"idle": 18, "attacking": 12, "dying": 15},
    'OGRE': {"walking": 18, "attacking": 12, "dying": 15},
    'ELEMENTALS': {"walking": 24, "attacking": 12, "dying": 15, "run_attacking": 12},
    'FAIRY': {"idle": 12, "attacking": 12, "dying": 15},
    'MASKER': {"walking": 24, "attacking": 12, "dying": 15, "sliding": 6},
    'ARCHMAGE': {"idle": 12, "attacking": 12, "dying": 15},
    'MANIPULATOR': {"idle": 12, "attacking": 12, "dying": 15},
    'MINER': {"idle": 12, "attacking": 12, "dying": 15},
    'ELVES': {"walking": 24, "attacking": 12, "dying": 15, "falling": 6},
    'SWORDSMAN': {"idle": 18, "attacking": 12, "dying": 15},
    'PHANTOM': {"walking": 18, "attacking": 12, "dying": 15}
}
