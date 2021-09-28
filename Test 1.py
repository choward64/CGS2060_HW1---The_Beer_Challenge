# Importing the Functions he provides us

import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)


HWBeerFunctions.millGrain(
    barleyQuantity = lines[0],
    ourWorld = lines[1],

)




# TO-DO: Read HW_1_Data and define the variables that the above functions require

# Opens the data file that the functions are going to pull from

Options.close()