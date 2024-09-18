import random
import math
import pyperclip as clip # pip install pyperclip

bingerBoard = '['

easyTasks = ['1 of each grave (no golden variants)',
             str(random.randint(30,60)) + ' Molotov Cocktails', # 30-60
             'Obsidian Skull',
             'Fruit Salad and Fruit Juice',
             str(random.randint(25,75)) + ' Cracked Dungeon Bricks', # 25-75
             'Any Gem Staff',
             'Die to Corrupt/Vicious Penguin',
             'Any Animal Cage',
             'Reef Chandelier',
             str(random.randint(100,200)) + ' Boulders', # 100-200
             str(random.randint(800,1200)) + ' Ice Blocks', # 800-1200
             str(random.randint(15,25)) + ' Stars in a Bottle', # 15-25
             'Monster Lasagna',
             'Throne',
             'Magic Mirror',
             str(random.randint(3,6)) + ' Unique Banners', # 3-6
             str(random.randint(30,50)) + ' Scarab Bombs', # 30-50
             'Seafood Dinner',
             str(random.randint(7,10)) + ' Unique Sinks', # 7-10
             str(random.randint(4,6)) + ' Grub Soups', # 4-6
             str(random.randint(150,250)) + ' Orange Torches', # 150-250
             str(random.randint(15,30)) + ' Antlion Eggs', # 15-30
             str(random.choice(['Glass', 'Frozen', 'Honey', 'Marble', 'Granite']) + ' Bookcase'),
             str(random.choice(['Amethyst', 'Topaz', 'Sapphire', 'Emerald', 'Ruby', 'Amber', 'Diamond'])) + ' Gem Lock',
             'Glowing Snail',
             str(random.randint(80,120)) + ' Copper/Tin Bars', # 80-120
             str(random.randint(20,30)) + ' Feathers', # 20-30
             ]
numEasyTasks = len(easyTasks)

medTasks = ['Boomstick',
            'Encumbering Stone',
            'Solidifier',
            'Abeemination',
            'Torch God\'s Favor',
            str(random.randint(20,30)) + ' Enchanted Nightcrawlers', # 20-30
            'Ash Wood Clock',
            str(random.randint(5,7)) + ' Unique Dye Items', # 5-7
            str(random.choice(['Gender Change Potion', 'Garland'])),
            'Blade of Grass',
            str(random.choice(['Flinx Staff', 'Flinx Fur Coat'])),
            'Ancient Armor Piece',
            str(random.randint(2,3)) + ' Unique Crates', # 2-3
            'Axe of Regrowth',
            'Mandible Blade',
            str(random.randint(60,90)) + ' Green Stucco', # 60-90
            str(random.randint(80,120)) + ' Aetherium Brick', # 80-120
            str(random.randint(2,3)) + ' Unique Grappling Hooks', # 2-3
            'Guide to Peaceful Coexistance',
            str(random.randint(30,50)) + ' TNT Barrels', # 30-50
            str(random.choice(['Amethyst', 'Topaz', 'Sapphire', 'Emerald', 'Ruby', 'Amber', 'Diamond'])) + ' Robe',
            'Faeling',
            str(random.randint(2000,3000)) + ' Poisoned Knives', # 2000-3000
            str(random.randint(100,200)) + ' Hellstone Brick', # 100-200
            str(random.randint(25,40)) + ' Skyware Candles', # 25-40
            ]
numMedTasks = len(medTasks)

hardTasks = ['3x3 Underworld Painting',
             'Aether Monolith',
             str(random.choice(['Purple', 'Yellow', 'Blue', 'Green', 'Red', 'Orange', 'White'])) + ' Phaseblade', # Any color phaseblade
             'Full Fossil Armor',
             'Boss ' + str(random.choice(['Mask', 'Trophy'])), # Boss Mask/Trophy
             'Any Spell Book',
             str(random.randint(1000,2000)) + ' Illuminant Coating', # 1000 - 2000
             str(random.choice(['Life', 'Mana'])) + ' Hair Dye', # Life/Mana Hair Dye
             'Ambrosia',
             str(random.randint(500,1000)) + ' Javelins', # 500 - 1000
             'Bronze Golf Trophy',
             str(random.randint(6,10)) + ' Unique Enemy Statues', # 6 - 10
             str(random.randint(4,7)) + ' Geysers', # 4 - 7
             'Used Gas Trap',
             'Night Vision Helmet',
             'Void Vault',
             'Black Pearl',
             str(random.randint(8,12)) + ' Life Crystal Boulders', # 8 - 12
             'Dead Man\'s Sweater',
             str(random.randint(300,500)) + ' Poo', # 300 - 500,
             'Trimarang',
             'Meteorite Piano',
             str(random.randint(50,60)) + ' Shadow Candles', # 50 - 60
             'Full Necro Armor',
             'The Grand Design',
             'Full Obsidian Armor'
             ]
numHardTasks = len(hardTasks)

insaneTasks = [ 'Flamarang',
                str(random.randint(1500,2500)) + ' Decorative Mana Potions', # 1500 - 2500
                str(random.randint(800,1200)) + ' Multicolored Stained Glass', # 800 - 1200
                'Diving Helmet',
                'Night\'s Edge',
                'Lightning Boots',
                'Obsidian Crate',
                'Full Molten Armor',
                'Mollusk Whistle',
                str(random.randint(13,17)) + ' unique crafting stations', # 13 - 17
                str(random.randint(2,4)) + ' Different Premium Golf Clubs', # 2 - 4
                str(random.randint(25,40)) + ' Flasks of Fire/Poison', # 25 - 40
                'Sunfury',
                'Medicated Bandage',
                ]
numInsaneTasks = len(insaneTasks)
numAllTasks = [numEasyTasks, numMedTasks, numHardTasks, numInsaneTasks]

for i in range(25):
    bingerBoard += '{\"name\": \"'
    rand = random.random()
    if i == 12:                                                     # Middle Square, 100% Insane
        insaneRand = math.floor(rand*len(insaneTasks))
        bingerBoard += insaneTasks[insaneRand]
        insaneTasks.remove(insaneTasks[insaneRand])
    elif (i == 4 or i == 6 or i == 18 or i == 20):                  # Green Squares (see sheet), 20% Medium, 70% Hard, 10% Insane
        if random.randint(1, 5) == 1:                               # 20% Medium
            medRand = math.floor(rand*len(medTasks))
            bingerBoard += medTasks[medRand]
            medTasks.remove(medTasks[medRand])
        elif random.randint(1, 8) != 8:                             # 87.5% of remaining 80% Hard (70%)
            hardRand = math.floor(rand*len(hardTasks))
            bingerBoard += hardTasks[hardRand]
            hardTasks.remove(hardTasks[hardRand])
        else:                                                       # Remaining 10% Insane
            insaneRand = math.floor(rand*len(insaneTasks))
            bingerBoard += insaneTasks[insaneRand]
            insaneTasks.remove(insaneTasks[insaneRand])
    else:                                                           # Yellow Squares (see sheet), 50% Easy, 40% Medium, 8% Hard, 2% Insane
        if random.randint(1, 2) == 1:                               # 50% Easy
            easyRand = math.floor(rand*len(easyTasks))
            bingerBoard += easyTasks[easyRand]
            easyTasks.remove(easyTasks[easyRand])
        elif random.randint(1, 5) != 5:                             # 80% of remaining 50% Medium (40%)
            medRand = math.floor(rand*len(medTasks))
            bingerBoard += medTasks[medRand]
            medTasks.remove(medTasks[medRand])
        elif random.randint(1, 5) != 5:                             # 80% of remaining 10% Hard (8%)
            hardRand = math.floor(rand*len(hardTasks))
            bingerBoard += hardTasks[hardRand]
            hardTasks.remove(hardTasks[hardRand])
        else:                                                       # Remaining 2% Insane
            insaneRand = math.floor(rand*len(insaneTasks))
            bingerBoard += insaneTasks[insaneRand]
            insaneTasks.remove(insaneTasks[insaneRand])
    bingerBoard += '\"},\n' 

bingerBoard = bingerBoard[0 : len(bingerBoard) - 2] + ']'           # minus 2 to delete last line break and comma
print(bingerBoard)
print(numAllTasks)

print('Print to clipboard? (Y/N)')
clipInput = str(input())
if clipInput == 'Y' or clipInput == 'y':
    clip.copy(bingerBoard)
    print('Copied!')
else:
    print('')
