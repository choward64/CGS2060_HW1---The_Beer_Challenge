
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