#
# Test environment 5
#
# NOTE: All comments go to the lines below them

'''
import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)
D_OurWorld = lines[1]
print("Value of lines:",lines)
print("Value of D_OurWorld:",D_OurWorld)
Options.close()
'''
'''
from test9 import Gallons_Of_Beer, Ratio_Of_Malt
'''
'''
import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)
D_OurWorld = lines[1]
returnvalue = 1

HWBeerFunctions.millGrain(
    barleyQuantity=lines[0],
    ourWorld=lines[1],
)
ourWorld = lines[2]
F_OurWorld = int(ourWorld + 1)
print(ourWorld)

'''

import HW1BeerFunctions_New
Options = open("HW_1_Data.txt", "r")
Gallons_Of_Beer = int(Options.readline().strip())
Ratio_Of_Malt = int(Options.readline().strip())
Pounds_Of_Hops = int(Options.readline().strip())
Grams_Of_Yeast = int(Options.readline().strip())

WORLD = 0

millGrain = HW1BeerFunctions_New.millGrain(
    barleyQuantity = Gallons_Of_Beer * Ratio_Of_Malt,
    ourWorld = int(WORLD),

)

barleyQuantity = Gallons_Of_Beer * Ratio_Of_Malt
Pounds_Of_Malt = 0

while True:
    Pounds_Of_Malt = millGrain(barleyQuantity, WORLD)
    if Pounds_Of_Malt == 0:
        print("The Milling Machine Was Broken. Trying Again...")
    else:
        break
mashConversion = HW1BeerFunctions_New.mashConversion(
    ourWorld = int(WORLD),
)
worked = 0

try:
    worked = mashConversion(0, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been filled!")
except ValueError:
    print("Oops, Something Went Wrong!")
    exit(-1)

try:
    worked = mashConversion(1, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been heated.")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)

try:
    worked = mashConversion(2, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been loaded!")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)
