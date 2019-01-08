import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from p1a import *
from p1b import *
from p1c import *
from p1e import *
from p2a import *
from p2b import *


# Takes the gradient of a single data point
def gradient_step(x1, x2, weights, classification):
    z = find_z_value(x1, x2, weights)
    grad_coefficient = -2*(classification-z)*z*(1-z)
    grad_step = grad_coefficient * np.array([1, x1, x2])
    return grad_step


# Adds two 1D matrices together
def add_1d_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        result.append(m1[i]+m2[i])
    return result


# Takes the sum of the gradients of several data points
def gradient_sum(data, weights, classification):
    grad_sum = [0, 0, 0]
    for i in range(len(data[0])):
        grad_sum = add_1d_matrices(gradient_step(data[0][i], data[1][i], weights, classification[i]), grad_sum)
    return grad_sum


# Takes a parameter scalar and matrix and returns the product
def scalar_times_1d_matrix(scalar, matrix):
    output_matrix = []
    for i in range(len(matrix)):
        output_matrix.append(matrix[i]*scalar)
    return output_matrix


# Takes the gradient sum of a set of data and its classifications and weights and divides by number of data points to return gradient
def gradient(data, weights, classification):
    grad_sum = gradient_sum(data, weights, classification)
    grad = []
    for i in range(len(weights)):
        grad.append(grad_sum[i]/len(data[0]))
    return grad


def main():
    # Weights have been set to w0=-6.6, w1=0.88, w2=1.4 based off of trial and error
    weights = [-6.2, 0.88, 1.4]

    # Reads and organizes data input and returns a 2D array of
    # [0]: petal lengths, [1]: petal widths, [2]: species, [3]: actual class
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])
    remove_setosa(input)
    input.append([])
    input[3] = class_number(input[2])

    scatter_data = get_xy(input[0], input[1], input[2])

    plt.subplot(1, 2, 1)
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

    # Plots before the first step
    plt.subplot(1, 2, 1)
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of first scatter plot
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('Petal Width (cm) vs Petal Length (cm)\n of Versicolor and Virginica Irises')
    plt.legend()

    # First line is drawn onto matplotlib
    draw_line(-1 * weights[1] / weights[2], -1 * weights[0] / weights[2])

    # Updates weights
    learning_rate = 0.5
    weights = add_1d_matrices(weights, scalar_times_1d_matrix(learning_rate, gradient([input[0], input[1]], weights, input[3])))

    # Plots after the first step
    plt.subplot(1, 2, 2)
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('Petal Width (cm) vs Petal Length (cm)\n of Versicolor and Virginica Irises')
    plt.legend()

    # Line is drawn onto matplotlib
    draw_line(-1 * weights[1] / weights[2], -1 * weights[0] / weights[2])

    # Plot is shown
    plt.show()


# Runs main method
if __name__ == "__main__": main()