import random
import math
import json

# To-Do:
# Randomize individual tasks

bingerBoard = []

easyTasks = ['1 of each grave (no golden variants)',
             '- Molotov Cocktails', # 30-60
             'Obsidian Skull',
             'Fruit Salad and Fruit Juice',
             '- Cracked Dungeon Bricks', # 25-75
             'Any Gem Staff',
             'Die to Corrupt/Vicious Penguin',
             'Any Animal Cage',
             'Reef Chandelier',
             '- Boulders', # 100-200
             '- Ice Blocks', # 800-1200
             '- Stars in a Bottle', # 15-25
             'Monster Lasanga',
             'Throne',
             'Magic Mirror',
             '- Unique Banners', # 3-6
             '- Scarab Bombs', # 30-50
             'Seafood Dinner',
             '- Unique Sinks', # 7-10
             '- Grub Soups', # 4-6
             '- Orange Torches' # 150-250
             ]

medTasks = ['Boomstick',
            'Encumbering Stone',
            'Solidifier',
            'Abeemination',
            'Torch God\'s Favor',
            '- Enchanted Nightcrawlers', # 20-30
            'Ash Wood Clock',
            '- Copper/Tin Bars', # 80-120
            '- Unique Dye Items', # 5-7
            'Gender Change Potion',
            'Blade of Grass',
            'Flinx Staff',
            'Ancient Armor Piece',
            '- Unique Crates', # 2-3
            'Axe of Regrowth',
            'Mandible Blade',

            ]

hardTasks = ['3x3 Underworld Painting',
             'Aether Monolith',
             '- Phaseblade', # add rng later
             'Full Fossil Armor',
             'Boss Trophy/Mask', # add rng later
             'Any Spell Book',
             '- Illuminant Coating', # 1000 - 2000
             'Life/Mana Hair Dye', #add rng later
             'Ambrosia',
             '- Javelins', # 500 - 1000
             'Bronze Golf Trophy',
             '- Unique Enemy Statues', # 6 - 10
             '- Geysers', # 4 - 7
             'Used Gas Trap',
             'Night Vision Helmet',
             'Void Vault',
             'Black Pearl', #add rng later
             '- Life Crystal Boulders', # 8 - 12
             'Dead Man\'s Sweater',
             '- Poo', # 300 - 500,
             'Trimarang',
             'Meteorite Piano',
             '- Shadow Candles', # 50 - 60
             'Full Necro Armor',
             'The Grand Design'
             ]

insaneTasks = [ 'Flamarang',
                '- Decorative Mana Potions', # 1500 - 2500
                '- Multicolored Stained Glass', # 800 - 1200
                'Diving Helmet',
                'Night\'s Edge',
                'Lightning Boots',
                'Obsidian Crate',
                'Full Molten Armor',
                'Mollusk Whistle',
                '- unique crafting stations', # 13 - 17
                '- Different Premium Golf Clubs', # 2 - 4
                '- Flasks of Fire/Poison', # 25 - 40
                'Sunfury'
                ]

numAllTasks = [len(tasks) for tasks in [easyTasks, medTasks, hardTasks, insaneTasks]]

for i in range(25):
    rand = random.random()
    if i == 12:                                                     # Middle Square, 100% Insane
        insaneRand = math.floor(rand*len(insaneTasks))
        name = insaneTasks[insaneRand]
        insaneTasks.remove(insaneTasks[insaneRand])
    elif (i == 4 or i == 6 or i == 18 or i == 20):                  # Green Squares (see sheet), 20% Medium, 70% Hard, 10% Insane
        if random.randint(1, 5) == 1:                               # 20% Medium
            medRand = math.floor(rand*len(medTasks))
            name = medTasks[medRand]
            medTasks.remove(medTasks[medRand])
        elif random.randint(1, 8) != 8:                             # 87.5% of remaining 80% Hard (70%)
            hardRand = math.floor(rand*len(hardTasks))
            name = hardTasks[hardRand]
            hardTasks.remove(hardTasks[hardRand])
        else:                                                       # Remaining 10% Insane
            insaneRand = math.floor(rand*len(insaneTasks))
            name = insaneTasks[insaneRand]
            insaneTasks.remove(insaneTasks[insaneRand])
    else:                                                           # Yellow Squares (see sheet), 50% Easy, 40% Medium, 8% Hard, 2% Insane
        if random.randint(1, 2) == 1:                               # 50% Easy
            easyRand = math.floor(rand*len(easyTasks))
            name = easyTasks[easyRand]
            easyTasks.remove(easyTasks[easyRand])
        elif random.randint(1, 5) != 5:                             # 80% of remaining 50% Medium (40%)
            medRand = math.floor(rand*len(medTasks))
            name = medTasks[medRand]
            medTasks.remove(medTasks[medRand])
        elif random.randint(1, 5) != 5:                             # 80% of remaining 10% Hard (8%)
            hardRand = math.floor(rand*len(hardTasks))
            name = hardTasks[hardRand]
            hardTasks.remove(hardTasks[hardRand])
        else:                                                       # Remaining 2% Insane
            insaneRand = math.floor(rand*len(insaneTasks))
            name = insaneTasks[insaneRand]
            insaneTasks.remove(insaneTasks[insaneRand])
    bingerBoard.append({'name': name})

print(json.dumps(bingerBoard, separators=(',', ':')))
print(numAllTasks)