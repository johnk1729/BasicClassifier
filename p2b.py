import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from p1a import *
from p1b import *
from p1c import *
from p1e import *
from p2a import *


# Main method
def main():
    realistic_weights = [-6.7, 0.88, 1.5]
    unrealistic_weights = [6.8, -2, 1.5]

    # Reads and organizes data input and returns a 2D array of
    # [0]: petal lengths, [1]: petal widths, [2]: species, [3]: actual class
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])
    remove_setosa(input)
    input.append([])
    input[3] = class_number(input[2])

    print(mse([input[0], input[1]], realistic_weights, input[3]))
    print(mse([input[0], input[1]], unrealistic_weights, input[3]))

    scatter_data = get_xy(input[0], input[1], input[2])
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('Petal Width (cm) vs Petal Length (cm)\n of Versicolor and Virginica Irises')
    plt.legend()

    # Line is drawn onto matplotlib
    draw_line(-1 * realistic_weights[1]/realistic_weights[2], -1 * realistic_weights[0]/realistic_weights[2])
    draw_line(-1 * unrealistic_weights[1] / unrealistic_weights[2], -1 * unrealistic_weights[0] / unrealistic_weights[2])

    # Plot is shown
    plt.show()


# Runs main method
if __name__ == "__main__": main()