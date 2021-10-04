#
# Group Homework Project 1 - The Beer Challenge
# Carlton Howard and Ryan Hatcher
# Instructions: Create a Python Program that can keep track of the entire brewing process from start to finish.
# DUE 10.04.2021 for Class CGS2060 (Intro to Computer Programming)
#
# All Comments go to the line(s) below them


# Importing the Functions
import HW1BeerFunctions_New

# Reading the Input file
Options = open("HW_1_Data.txt", "r")
# Taking the values from the input data file
Gallons_Of_Beer = int(Options.readline().strip())
Ratio_Of_Malt = int(Options.readline().strip())
Pounds_Of_Hops = int(Options.readline().strip())
Grams_Of_Yeast = int(Options.readline().strip())

WORLD = 0

'''
millGrain = HW1BeerFunctions_New.millGrain(
    barleyQuantity = Gallons_Of_Beer * Ratio_Of_Malt,
    ourWorld = WORLD,

)
'''

# Part 1 - millGrain
barleyQuantity = Gallons_Of_Beer * Ratio_Of_Malt
Pounds_Of_Malt = 0

while True:
    Pounds_Of_Malt = HW1BeerFunctions_New.millGrain(barleyQuantity, WORLD)
    if Pounds_Of_Malt == 0:
        print("The Milling Machine Was Broken. Trying Again...")
    else:
        break
mashConversion = HW1BeerFunctions_New.mashConversion(
    ourWorld = WORLD,
    action = 0,
)

# Part 2 - mashConversion
worked = 0

try:
    worked = HW1BeerFunctions_New.mashConversion(0, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been filled!")
except ValueError:
    print("Oops, Something Went Wrong!")
    exit(-1)

try:
    worked = HW1BeerFunctions_New.mashConversion(1, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been heated!")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)

try:
    worked = HW1BeerFunctions_New.mashConversion(2, WORLD)
    if worked == 0:
        raise ValueError
    else:
        print("The tank has been loaded!")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)

# Part 3 - Kettle
infile = open("Hw_1_Data.txt","r")


WORLD = 0
Maltratio = 0
try:
    loaded = HW1BeerFunctions_New.kettle(Maltratio,WORLD)
    if loaded == 0:
        raise ValueError
    else:
        print("Wort has been put into kettle.")
except ValueError:
    print("something went wrong")
    exit(-1)

# Part 4 - HeatKettle
import HW1BeerFunctions_New
HW1BeerFunctions_New.heatKettle(
    onOff=1,
    ourWorld=0
)

infile = open("HW_1_Data.txt", "r")

WORLD = 0

try:
    heated = HW1BeerFunctions_New.kettle(1, WORLD)
    if heated == 0:
        raise ValueError
    else:
        print("Kettle was heated.")
except ValueError:
    print("Something went wrong...") # Changed this to make it work, the P was capitalized.
    exit(-1)

# Part 5 - addHops
from HW1BeerFunctions import addHops

infile = open("HW_1_Data.txt","r")
Gallons_Of_Beer = int(infile.readline().strip())

Pounds_Of_Hops = int(infile.readline().strip())


WORLD = 0

try:
    heated = addHops("bittering", Pounds_Of_Hops, Gallons_Of_Beer,WORLD)
    if heated == 0:
        raise ValueError
    else:
        print ("bittering hops added to kettle.")
except ValueError:
    print("something went wrong")
    exit(-1)

try:
    heated = addHops("finishing",Pounds_Of_Hops, Gallons_Of_Beer,WORLD)
    if heated == 0:
        raise ValueError
    else:
        print("finishing hops added to kettle.")
except ValueError:
    print("something went wrong.")
    exit(-1)

# Part 6 - prepareYeast
import HW1BeerFunctions_New

try:
    Done = HW1BeerFunctions_New.prepareYeast(Grams_Of_Yeast, WORLD)
    if Done == 0:
        raise ValueError
    else:
        print("Yeast has been prepared for the fermentation process!")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)

# Part 7 - start Fermentation
try:
    Fermentation = HW1BeerFunctions_New.startFermentatation(Gallons_Of_Beer, 1, WORLD)
    if Fermentation == 0:
        raise ValueError
    else:
        print("Fermentation process has been finished!")
except ValueError:
    print("Oops, Something went wrong!")
    exit(-1)


Options.close()