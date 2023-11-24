VIKING, BARBARIAN, OGRE, ELEMENTALS, MASKER = 'VIKING', 'BARBARIAN', 'OGRE', 'ELEMENTALS', 'MASKER'
ELVES, PHANTOM = 'ELVES', 'PHANTOM'
INFANTRY, ARCHER, SHIELD, FAIRY, ARCHMAGE = 'INFANTRY', 'ARCHER', 'SHIELD', 'FAIRY', 'ARCHMAGE'
MANIPULATOR, MINER, SWORDSMAN, MORTAR = 'MANIPULATOR', 'MINER', 'SWORDSMAN', 'MORTAR'

level_num = 8

level_enemies = {
    '1': [VIKING, BARBARIAN],
    '2': [VIKING, BARBARIAN, OGRE],
    '3': [VIKING, BARBARIAN, ELEMENTALS],
    '4': [VIKING, BARBARIAN, OGRE, MASKER],
    '5': [VIKING, BARBARIAN, OGRE, ELVES],
    '6': [VIKING, BARBARIAN, PHANTOM],
    '7': [VIKING, BARBARIAN, OGRE, MASKER, ELVES],
    '8': [VIKING, BARBARIAN, OGRE, ELEMENTALS, MASKER, ELVES, PHANTOM]
}
level_towers = {
    '1': [MINER, ARCHER],
    '2': [MINER, ARCHER, INFANTRY],
    '3': [MINER, ARCHER, INFANTRY, ARCHMAGE],
    '4': [MINER, ARCHER, INFANTRY, ARCHMAGE, SHIELD],
    '5': [MINER, ARCHER, INFANTRY, ARCHMAGE, SHIELD, SWORDSMAN],
    '6': [MINER, ARCHER, INFANTRY, ARCHMAGE, SHIELD, SWORDSMAN, MANIPULATOR],
    '7': [MINER, ARCHER, INFANTRY, ARCHMAGE, SHIELD, SWORDSMAN, MANIPULATOR, FAIRY],
    '8': [MINER, ARCHER, INFANTRY, ARCHMAGE, SHIELD, SWORDSMAN, MANIPULATOR, FAIRY]
}
level1 = [[[VIKING], [1], 20],
          [[VIKING], [2], 20],
          [[BARBARIAN], [1], 10],
          [[VIKING, BARBARIAN], [2, 1], 15],
          [[VIKING, BARBARIAN], [4, 2], 15],
          [[VIKING, BARBARIAN], [5, 3], 20],
          None]

level2 = [[[VIKING], [1], 20],
          [[VIKING, BARBARIAN], [1, 1], 20],
          [[OGRE], [1], 10],
          [[BARBARIAN, OGRE], [2, 1], 25],
          [[VIKING, BARBARIAN], [3, 2], 15],
          [[VIKING, BARBARIAN, OGRE], [5, 3, 1], 20],
          None]

level3 = [[[VIKING], [1], 20],
          [[VIKING, BARBARIAN], [2, 1], 15],
          [[ELEMENTALS, VIKING], [1, 1], 15],
          [[VIKING, BARBARIAN], [2, 1], 20],
          [[VIKING, BARBARIAN], [3, 2], 15],
          [[VIKING, BARBARIAN, ELEMENTALS], [3, 1, 1], 20],
          [[VIKING, BARBARIAN, ELEMENTALS], [5, 3, 1], 15],
          None]

level4 = [[[BARBARIAN], [1], 15],
          [[MASKER], [1], 15],
          [[VIKING], [2], 5],
          [[VIKING, OGRE], [3, 1], 10],
          [[BARBARIAN, OGRE, MASKER], [2, 1, 1], 25],
          [[VIKING, BARBARIAN], [3, 1], 5],
          [[VIKING, BARBARIAN, MASKER], [3, 2, 2], 20],
          [[VIKING, BARBARIAN, OGRE, MASKER], [1, 2, 1, 1], 20],
          [[VIKING, BARBARIAN], [3, 2], 10],
          [[VIKING, BARBARIAN, OGRE, MASKER], [3, 2, 1, 3], 25],
          None]

level5 = [[[VIKING], [1], 20],
          [[VIKING, BARBARIAN], [1, 1], 20],
          [[OGRE], [1], 10],
          [[BARBARIAN, OGRE, ELVES], [2, 1, 1], 25],
          [[VIKING, BARBARIAN, ELVES], [3, 2, 2], 15],
          [[VIKING, BARBARIAN], [5, 2], 10],
          [[VIKING, BARBARIAN, OGRE], [5, 3, 2], 20],
          [[BARBARIAN, OGRE], [2, 2], 10],
          [[VIKING, BARBARIAN, ELVES], [3, 3, 3], 25],
          [[BARBARIAN], [7], 10],
          [[OGRE, ELVES], [3, 4], 20],
          [[VIKING, BARBARIAN, OGRE, ELVES], [5, 3, 1, 5], 30],
          None]

level6 = [[[VIKING], [1], 10],
          [[BARBARIAN], [1], 15],
          [[PHANTOM], [1], 10],
          [[VIKING, BARBARIAN], [2, 1], 20],
          [[VIKING, BARBARIAN], [2, 2], 15],
          [[VIKING, BARBARIAN, PHANTOM], [3, 3, 1], 30],
          [[PHANTOM], [3], 2],
          None]

level7 = [[[VIKING], [2], 20],
          [[VIKING, BARBARIAN], [1, 2], 20],
          [[OGRE, MASKER], [1, 1], 10],
          [[BARBARIAN, OGRE, ELVES, MASKER], [2, 1, 1, 1], 25],
          [[VIKING, BARBARIAN, ELVES], [3, 2, 2], 20],
          [[MASKER], [2], 10],
          [[VIKING, BARBARIAN, OGRE], [5, 3, 2], 25],
          [[BARBARIAN, MASKER], [2, 2], 10],
          [[VIKING, BARBARIAN, ELVES], [3, 3, 3], 25],
          [[BARBARIAN, OGRE, ELVES], [3, 3, 3], 20],
          [[VIKING, BARBARIAN, ELVES], [5, 5, 1], 15],
          [[MASKER], [7], 10],
          [[OGRE, ELVES], [1, 4], 20],
          [[VIKING, BARBARIAN, OGRE, ELVES, MASKER], [3, 3, 2, 3, 1], 20],
          None]

level8 = [[[VIKING], [3], 30],
          [[VIKING, BARBARIAN], [1, 2], 20],
          [[OGRE, MASKER], [1, 1], 10],
          [[BARBARIAN, ELVES, ELEMENTALS], [2, 1, 1], 25],
          [[VIKING, BARBARIAN, MASKER], [3, 3, 2], 30],
          [[MASKER, PHANTOM], [3, 1], 20],
          [[VIKING, BARBARIAN, OGRE, ELEMENTALS], [2, 1, 1, 2], 20],
          [[BARBARIAN, MASKER], [2, 2], 20],
          [[VIKING], [10], 25],
          [[BARBARIAN], [15], 15],
          [[ELVES], [5], 20],
          [[MASKER], [7], 20],
          [[ELEMENTALS, ELVES], [4, 4], 20],
          [[VIKING, BARBARIAN, OGRE, ELVES, MASKER], [10, 8, 3, 5, 3], 25],
          [[PHANTOM], [2], 15],
          [[VIKING, BARBARIAN], [5, 5], 3],
          [[OGRE, MASKER], [3, 3], 2],
          [[VIKING, ELEMENTALS, ELVES], [3, 2, 2], 20],
          [[ELEMENTALS, PHANTOM], [2, 2], 20],
          [[BARBARIAN, OGRE], [15, 3], 2],
          [[BARBARIAN, MASKER], [8, 2], 2],
          [[ELEMENTALS, OGRE, ELVES], [3, 3, 3], 10],
          [[BARBARIAN, PHANTOM, ELVES], [20, 3, 3], 25],
          [[MASKER], [10], 20],
          [[VIKING, BARBARIAN, OGRE, ELVES, ELEMENTALS, MASKER], [15, 15, 5, 5, 5, 5], 25],
          [[PHANTOM], [3], 3],
          [[MASKER], [5], 3],
          None]

level_wave_dict = {
    '1': level1,
    '2': level2,
    '3': level3,
    '4': level4,
    '5': level5,
    '6': level6,
    '7': level7,
    '8': level8
}
