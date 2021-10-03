from HW1BeerFunctions import millGrain
from HW1BeerFunctions import mashConversion
from HW1BeerFunctions import kettle
from HW1BeerFunctions import heatKettle
from HW1BeerFunctions import addHops
from HW1BeerFunctions import prepareYeast
from HW1BeerFunctions import startFermentataion



infile = open("HW_1_Data.txt","r")
Gallons_Of_Beer = int(infile.readlines().strip())
Ratio_Of_Malt = int(infile.readlines().strip())
Pounds_Of_Hops = int(infile.readlines().strip())
Grams_Of_Yeast = int(infile.readlines().strip())

WORLD = 0

try:
    heated = addHops{"bittering", Pounds_Of_Hops, Gallons_Of_Beer,WORLD}
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