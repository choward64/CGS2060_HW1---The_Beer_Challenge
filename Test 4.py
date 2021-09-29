import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)
D_OurWorld = lines[1]


HWBeerFunctions.millGrain(
    barleyQuantity=lines[0],
    ourWorld=lines[1],
)
HWBeerFunctions.mashConversion(
    action=lines[2],
    ourWorld=int(D_OurWorld+"1") # Takes the OurWorld value from ln01 of HW_Data.

)