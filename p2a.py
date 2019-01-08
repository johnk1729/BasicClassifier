import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from p1a import *
from p1b import *
from p1c import *
from p1e import *


# Finds the Mean Square Error given a data set, weights, and a list of real classes of the data set
def mse(data, weights, classification):
    tse = 0.0
    for i in range(len(data[0])):
        tse += (find_z_value(data[0][i], data[1][i], weights) - classification[i])**2
    return tse/len(data[0])


# Returns correct classification number for a given set of species
def class_number(species):
    classes = []
    for i in range(len(species)):
        if species[i] == 'versicolor':
            classes.append(1)
        elif species[i] == 'virginica':
            classes.append(0)
        else:
            print("You tried to classify something other than versicolor or virginica. Sanitize your input to include only these.")
    return classes


# Main method
def main():
    # Weights have been set to w0=-6.6, w1=0.88, w2=1.4 based off of trial and error
    weights = [-6.6, 0.88, 1.4]

    # Reads and organizes data input and returns a 2D array of
    # [0]: petal lengths, [1]: petal widths, [2]: species, [3]: actual class
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])
    remove_setosa(input)
    input.append([])
    input[3] = class_number(input[2])

    print(mse([input[0], input[1]], weights, input[3]))


# Runs main method
if __name__ == "__main__": main()