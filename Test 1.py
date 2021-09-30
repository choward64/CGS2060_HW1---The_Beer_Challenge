#
# Test environment 1
#
# NOTE: All comments go to the lines below them


# Importing the Functions he provides us
# from builtins import function

#Importing the main functions file
import HWBeerFunctions

# Opening the data file that the program is supposed to pull options from.
Options = open("HW_1_Data.txt", "r")
# Reading the options file and putting the lines into variable "lines"
lines = Options.readlines()
str(lines)

# This is a test var, IGNORE
D_OurWorld = lines[1]

# Calling the millgrain function (Part A)
HWBeerFunctions.millGrain(
    barleyQuantity=lines[0],
    ourWorld=lines[1],
)
# Calling the mashConversion function and defining the variable that has its returns
var = HWBeerFunctions.mashConversion(

    action=1,
    ourWorld=1, # Takes the OurWorld value from ln01 of HW_Data.

)
# TODO: Find a way to get the lines value for the action then change the action value from the var value
# The following does absolutely nothing for some reason:
while action == 1:
    action = 2
    if var == 2:
        action = 2
# var = HWBeerFunctions.mashConversion()

# debugging print statement
print(type(var))
print(var)
# Does nothing
while var == 2:
    action = 2

if var == 3:
    action = 3

'''
else:
    print("Part B Completed!")
'''



# TO-DO: Read HW_1_Data and define the variables that the above functions require

# Closes the options file
Options.close()