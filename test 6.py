

'''

]]]
'''

#
# Test environment 6
#
# NOTE: All comments go to the lines below them



from HW1BeerFunctions import kettle


infile = open("Hw_1_Data.txt","r")


WORLD = 0
Maltratio = 0
try:
    loaded = kettle(Maltratio,WORLD)
    if loaded == 0:
        raise ValueError
    else:
        print("Wort has been put into kettle.")
except ValueError:
    print("something went wrong")
    exit(-1)
