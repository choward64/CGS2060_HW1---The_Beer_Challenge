
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
    Pounds_Of_Malt = millGrain*(barleyQuantity, WORLD)
    if Pounds_Of_Malt == 0:
        print("The Milling Machine Was Broken. Trying Again...")
    else:
        break
mashConversion = HW1BeerFunctions_New.mashConversion(
   # ourWorld = int(WORLD),
   # action = 0,
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
#1