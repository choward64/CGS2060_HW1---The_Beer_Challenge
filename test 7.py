


import HWBeerFunctions
HWBeerFunctions.heatKettle()

infile = open("HW_1_Data.txt", "r")

WORLD = 0

try:
    heated = kettle(1, WORLD)
    if heated == 0:
        raise ValueError
    else:
        print("Ketle was heated.")
except ValueError:
    Print("something went wrong")
    exit(-1)

