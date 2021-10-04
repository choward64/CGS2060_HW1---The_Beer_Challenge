


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

