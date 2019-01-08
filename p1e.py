import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from p1a import *
from p1b import *
from p1c import *


# Finds the z-value, or probability of either classification given data x1 and x2 and weights
def find_z_value(x, y, weights):
    hs = get_hypothesis_space([1, x, y], weights)
    return sigmoid(hs)


# Removes all instances of the first class "setosa" from a data set
def remove_setosa(data):
    # Loop differentiates by class (species) and places them in different lists for data input
    i = 0
    while i < len(data[0]):
        if data[2][i] == 'setosa':
            del data[0][i]
            del data[1][i]
            del data[2][i]
        else:
            i += 1

    return data


# Main method
def main():
    # Weights have been set to w0=-6.6, w1=0.88, w2=1.4 based off of trial and error
    weights = [-6.6, 0.88, 1.4]

    # Reads and organizes data input and returns a 2D array of
    # [0]: petal lengths, [1]: petal widths, [2]: species
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])
    remove_setosa(input)

    classification_data = []
    classification_data.append([])
    classification_data.append([])
    classification_data.append([])
    classification_data.append([])
    classification_data.append([])

    for i in range(len(input[0])):
        classification_data[0].append(input[0][i])
        classification_data[1].append(input[1][i])
        classification_data[2].append(find_z_value(input[0][i], input[1][i], weights))
        classification_data[3].append(int(classification_data[2][i]+0.5))
        classification_data[4].append(input[2][i])

    print('Petal length, Petal width, Sigmoid result, Classification, Species\n')

    # Prints all of the data
    '''for i in range(len(classification_data[0])):
        print('(', classification_data[0][i],',',classification_data[1][i],',',classification_data[2][i],',',classification_data[3][i],',',classification_data[4][i],')')'''

    # Prints examples
    print('More Ambiguous Examples: ')
    print('(', classification_data[0][20],',',classification_data[1][20],',',classification_data[2][20],',',classification_data[3][20],',',classification_data[4][20],')')
    print('(', classification_data[0][22],',',classification_data[1][22],',',classification_data[2][22],',',classification_data[3][22],',',classification_data[4][22],')')
    print('(', classification_data[0][69],',',classification_data[1][69],',',classification_data[2][69],',',classification_data[3][69],',',classification_data[4][69],')')
    print('(', classification_data[0][88],',',classification_data[1][88],',',classification_data[2][88],',',classification_data[3][88],',',classification_data[4][88],')')

    print('\nUnambiguous Examples: ')
    print('(', classification_data[0][48],',',classification_data[1][48],',',classification_data[2][48],',',classification_data[3][48],',',classification_data[4][48],')')
    print('(', classification_data[0][29],',',classification_data[1][29],',',classification_data[2][29],',',classification_data[3][29],',',classification_data[4][29],')')
    print('(', classification_data[0][68],',',classification_data[1][68],',',classification_data[2][68],',',classification_data[3][68],',',classification_data[4][68],')')
    print('(', classification_data[0][90],',',classification_data[1][90],',',classification_data[2][90],',',classification_data[3][90],',',classification_data[4][90],')')


# Runs main method
if __name__ == "__main__": main()
