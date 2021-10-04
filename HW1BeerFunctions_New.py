import random

yeastGrams = 0


'''
 * Function Name: millGrain
 * Function ID: 2
 *
 * Description:
 * This function accepts a value for the amount of malt that is to be milled. The
 * milling machine will be checked to see if it is broken or operational. If it is
 * broken, then a "0" will be returned. If it is operational then the malt will be
 * milled and the amount milled will be printed out every 10 pounds. The function
 * will return the number of pounds of malt that were milled.
 *
 * Inputs:
 *      int maltQuantity - number of pounds of malt to be milled
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the milling machine is broken
 *      # - number of pounds of malt that were milled
 *
'''

def millGrain(barleyQuantity, ourWorld):
    broken = 0.0
    numTenPounds = 0

    print("=== Starting The YumYum Brewing Company's Milling Process ===")

    if (ourWorld == 2):
        return(0)

    broken = (random.randrange(0,100)/100)

    if (broken < 0.5):
        return(0)
    else:
        numTenPounds = int(barleyQuantity / 10)
        for i in range (1,numTenPounds):
            print("{0:4d} pounds of barley have been milled".format(i*10))
        print("{0:4d} pounds of barley have been milled".format(barleyQuantity))

    return(barleyQuantity)


'''
 * Function Name: mashConversion
 * Function ID: 3
 *
 * Description:
 * This function accepts a command and performs one of the following actions:
 *    "fill" - fill the mash tank with water
 *    "heat" - heat the water
 *    "load" - load the malt mixture into the tank
 * If any of these actions cannot be performed, then an error code of 0 will be returned.
 *
 * Inputs:
 *      int action - mash conversion action to be performed (1,2,3)
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
'''


def mashConversion(action, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Mash Conversion ===")

    if (ourWorld == 3):
        return(0)


    if (action == 0):
        print("The tank is being filled!")
        return(1)
    else:
        if (action == 1):
            print("The tank is being heated.")
            return(2)
        else:
            if (action == 2):
                print("The tank is being loaded with mash.")
                return(1)
            else:
                print("Error: unrecognized action.")
                exit(-1)


'''
 * Function Name: kettle
 * Function ID: 6
 *
 * Description:
 * This function loads the kettle with the wort. If it is successful, it returns
 * a 1. If it fails, it returns a 0.
 *
 * Inputs:
 *      int wortQuantity - how many gallons of wort you want to load into the kettle
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
 '''


def kettle (mashQuantity, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Kettle Process ===")

    if (ourWorld == 6):
        return 0

    print("The wort loading into the kettle process has been completed.")

    return 1

'''
 * Function Name: heatKettle
 * Function ID: 7
 *
 * Description:
 * This function loads heats the kettle to boiling. If it is successful, it returns
 * a 1. If it fails, it returns a 0.
 *
 * Inputs:
 *      int onOff - activate the heating process
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
 '''


def heatKettle (onOff, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Kettle Heating Process")

    if (ourWorld == 7):
        return(0)

    if (onOff == 1):
        for i in range(70,212,20):
            print("The kettle temperature is {0}".format(i))

        print("The kettle temperature is 212")

        print("\nThe kettle heating process has been completed.")
    else:
        print("The kettle was not heated.")
        exit(-1)

    return 1

'''
 * Function Name: addHops
 * Function ID: 8
 *
 * Description:
 * This function loads the hops into the kettle at the start and the finish of the boil process.
 * If it is successful, it returns a 1. If it fails, it returns a 0.
 *
 * Inputs:
 *      int hops - activate the heating process (either "bittering" or "finishing") 
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
 '''


def addHops (hops, amountOfHops, beerAmount, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Kettle Hops Adding Process \n")

    if (ourWorld == 8):
        return(0)

    if (hops == 0):
        print("Adding bittering hops at the start of the boil")
        print("Adding {0:.1f} hops to the kettle.".format(float(beerAmount)/amountOfHops))
    else:
        if (hops == 1):
            print("Adding finishing hops at the end of the boil")
            print("Adding {0:.1f} hops to the kettle.".format(float(beerAmount)/amountOfHops))
        else:
            print("Error: Unrecognized command - hops were not added to the kettle.")
            exit(-1)

    return 1

'''
 * Function Name: prepareYeast
 * Function ID: 11
 *
 * Description:
 * This function prepares the yeast that will be used as a part of the fermentation process.
 * It will prepare the yeast that will be used in this process.
 * If it is successful, it returns a 1. If it fails, it returns a 0.
 *
 * Inputs:
 *      int amountOfYeast - amount of yeast to be used in the fermentation step
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
 '''


def prepareYeast (amountOfYeast, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Yeast Preperation Process")

    if (ourWorld == 11):
        return(0);

    if (amountOfYeast > 0):
        print("The yeast has been loaded for the fermentation step.")
        print("{0} grams of yeast will be used per gallon of beer.".format(amountOfYeast))
        yeastGrams = amountOfYeast
    else:
        print("Unrecognized yeast amount.")
        exit(-1)

    return 1


'''               
 * Function Name: startFermentataion
 * Function ID: 12
 *
 * Description:
 * This function prepares the yeast that will be used as a part of the fermentation process.
 * It will prepare the yeast that will be used in this process.
 * If it is successful, it returns a 1. If it fails, it returns a 0.
 *
 * Inputs:
 *      int amountOfYeast - amount of yeast to be used in the fermentation step
 *      int ourWorld - flag to indicate if we are living in a perfect world
 *
 * Outputs:
 *      0 - the requested action could not be performed
 *      1 - the action was performed successfully
 '''


def startFermentatation (maltAmount, action, ourWorld):

    print("\n=== Starting The YumYum Brewing Company's Yeast Fermentation Process")

    if (ourWorld == 12):
        return(0)

    if (action == 1):
        print("The fermentation process has been started.")
        print("{0} gallons of beer will be produced..".format(maltAmount))
    else:
        print("Unrecognized fermentation action.")
        exit(-1)

    return 1
