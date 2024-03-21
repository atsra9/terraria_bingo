import random
import json
from enum import Enum, auto

# To-Do:
# Randomize individual tasks

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

allTasks = [easyTasks, medTasks, hardTasks, insaneTasks]
numAllTasks = [len(tasks) for tasks in allTasks]

class Color(Enum):
    MIDDLE = auto()
    GREEN = auto()
    YELLOW = auto()

B = Color.MIDDLE
G = Color.GREEN
Y = Color.YELLOW
colors = [
    Y, Y, Y, Y, G,
    Y, G, Y, Y, Y,
    Y, Y, B, Y, Y,
    Y, Y, Y, G, Y,
    G, Y, Y, Y, Y,
]

weights = {
    Color.MIDDLE: [0, 0, 0, 1],
    Color.GREEN: [0, 2, 7, 1],
    Color.YELLOW: [50, 40, 8, 2],
}

bingerBoard = []

for i in range(25):
    rand = random.random()
    tasks = random.choices(allTasks, weights[colors[i]])[0]
    task = tasks.pop(random.randrange(len(tasks)))
    bingerBoard.append({'name': task})

print(json.dumps(bingerBoard, separators=(',', ':')))
print(numAllTasks)
