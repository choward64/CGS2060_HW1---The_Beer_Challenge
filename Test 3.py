# The next step will be for you to call the mashConversion routine. You will pass it a value of "0"
# to have the tank filled with water. A return value of "1" indicates that the tank has been filled.
# Next you'll pass it a value of "1" and this will cause the water to be heated. A return value of "1"
# indicates that the water has been heated. Finally, you'll call it with a value of "2" and this will
# cause the malt mixture to be loaded into the mash conversion tank. A return value of "1"
# indicates that the malt mixture has been loaded. If any of these stages returns a "0" then
# something is wrong.

# Importing the needed files
import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")

# Putting the values in the Options file into a format that the code can understand.
lines = Options.readlines()
# Changing the values in the options file into strings so they can be "mathed" (lol)
str(lines)
# Setting the var fill to line
fill = lines[3]
HWBeerFunctions.mashConversion(
    ourWorld=lines[1],

    if lines[1] == 0:
        action = "fill";
# TODO: 1) Have it check for the return value and 2) Print that the tank is filled
#   then 3) set the action to the "heat" variable. 4) Check the return value, if
#   it is 1 then 5) have the action change to 2 (load).
#   |||| If any of these steps return 0 then break and throw an error that ends
#   the program with the error message "0 - ERROR Thrown by Partition 2: Mash Conversion"
#   All of this goes off of the instructions pretty much word for word.

    else:
        if

    action = lines[3]: # Fills water tanks Code 0
# TODO: After there is a value return of 1 it means that the tank is full
    print("Water Tanks Filling"),
    action=lines[3],
)
# Closing the options File NOTE: This will only be done once in the actual Beer Challenge File!
Options.close()