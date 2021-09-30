# Importing the Functions he provides us
# from builtins import function

import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)
D_OurWorld = lines[1]


HWBeerFunctions.millGrain(
    barleyQuantity=lines[0],
    ourWorld=lines[1],
)

var = HWBeerFunctions.mashConversion(

    action=1,
    ourWorld=1, # Takes the OurWorld value from ln01 of HW_Data.

)
# TODO: Find a way to get the lines value for the action then change the action value from the var value
while action == 1:
    action = 2
    if var == 2:
        action = 2
# var = HWBeerFunctions.mashConversion()
print(type(var))
print(var)
while var == 2:
    action = 2

if var == 3:
    action = 3

'''
else:
    print("Part B Completed!")
'''



# TO-DO: Read HW_1_Data and define the variables that the above functions require

# Opens the data file that the functions are going to pull from

Options.close()