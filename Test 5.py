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