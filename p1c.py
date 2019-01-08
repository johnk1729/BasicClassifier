import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from p1a import *
from p1b import *


# Draws a 2D line on matplotlib
def draw_line(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')


# Main method
def main():
    # Weights have been set to w0=-6.6, w1=0.88, w2=1.4 based off of trial and error
    weights = [-6.6, 0.88, 1.4]

    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])

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
    draw_line(-1 * weights[1]/weights[2], -1 * weights[0]/weights[2])

    # Plot is shown
    plt.show()


# Runs main method
if __name__ == "__main__": main()
