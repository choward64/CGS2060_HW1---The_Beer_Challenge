#
# Test environment 2
#
# NOTE: All comments go to the lines below them

import random
def millGrain(barleyQuantity, ourWorld):
    broken = 0.0
    numTenPounds = 1
    Options = open("HW_1_Data.txt", "r")
    lines = Options.readlines()
    str(lines)
    barleyQuantity = 200



    print("=== Starting The YumYum Brewing Company's Milling Process ===")
    str(barleyQuantity)

    if (ourWorld == 2):
        return(0)

    broken = (random.randrange(0, 100)/100)

    if (broken < 0.5):
        return(0)
    else:

        numTenPounds = int(barleyQuantity / 10)
        for i in range(1, numTenPounds):
            print("{0:4d} pounds of barley have been milled".format(i*10))
        print("{0:4d} pounds of barley have been milled".format(barleyQuantity))

    return(barleyQuantity)
