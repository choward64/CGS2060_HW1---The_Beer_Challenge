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

'''
* Below we need to do the following:
    - define ourWorld, set it to two
    - Find a way to interpret the return values from the function and use them to trigger
        the next action set
        > Action Sets:
            + "fill" (1)
            + "heat" (2)
            + "load" (3)
            + ERROR CODE 0 - if a return value of 0 is sent 
'''
HWBeerFunctions.mashConversion(
ourWorld=2,
if returnvalue == 1:
    action=lines[2],
    ourWorld == lines[2]+1; # Takes the OurWorld value from ln01 of HW_Data.
else:
    print("There has been an error, program has been terminated.");
)