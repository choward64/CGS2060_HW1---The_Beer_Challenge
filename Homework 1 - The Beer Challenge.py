#
# Group Homework Project 1 - The Beer Challenge
# Ryan Hatcher and Carlton Howard
# Instructions: Create a Python Program that can keep track of the entire brewing process from start to finish.
# TODO: Outline the entire brewing Process
# DUE 10.04.2021 for Class CGS2060 (Intro to Computer Programming)
#
# All Comments go to the line(s) below them

# Importing the Functions he provides us
import HWBeerFunctions
HWBeerFunctions.millGrain()
HWBeerFunctions.mashConversion()
HWBeerFunctions.kettle()
HWBeerFunctions.heatKettle()
HWBeerFunctions.addHops()
HWBeerFunctions.prepareYeast()
HWBeerFunctions.startFermentataion()

# TODO: Read HW_1_Data and define the variables that the above functions require

# Part 1: MILL GRAIN FUNCTION
import HWBeerFunctions
Options = open("HW_1_Data.txt", "r")
lines = Options.readlines()
str(lines)
# TODO: Implement the "the milling machine is broken today" statement return if world=1 & broken > 0.5

HWBeerFunctions.millGrain(
    barleyQuantity = lines[0],
    ourWorld = lines[1],

)

# Opens the data file that the functions are going to pull from
Options = open("HW_1_Data", "r")

ourWorld = 2



hello