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
from p2e import *
from p3a import *


def main():
    # Weights have been set to w0=-6.6, w1=0.88, w2=1.4 based off of trial and error
    weights = [-10, 1, 2.5]

    # Reads and organizes data input and returns a 2D array of
    # [0]: petal lengths, [1]: petal widths, [2]: species, [3]: actual class
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])
    remove_setosa(input)
    input.append([])
    input[3] = class_number(input[2])

    scatter_data = get_xy(input[0], input[1], input[2])

    # Here begins the first plot
    plt.subplot(3, 2, 1)
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('Original Weights')
    plt.legend()

    # Line is drawn onto matplotlib
    draw_line(-1 * weights[1] / weights[2], -1 * weights[0] / weights[2])

    index = 0
    errors = []
    iterations = []
    error = mse([input[0], input[1]], weights, input[3])
    first_mse = error
    errors.append(error)
    iterations.append(index)

    # Displays second graph
    plt.subplot(3, 2, 2)
    plt.plot(iterations, errors)
    plt.xlabel('Iterations')
    plt.ylabel('Mean Squared Error')

    # Updates weights halfway
    learning_rate = 0.5
    while error > 0.06:
        weights = add_1d_matrices(weights, scalar_times_1d_matrix(learning_rate,
                                                                  gradient([input[0], input[1]], weights, input[3])))
        error = mse([input[0], input[1]], weights, input[3])
        index += 1
        errors.append(error)
        iterations.append(index)

    # Here begins the third plot
    plt.subplot(3, 2, 3)
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('Halfway')
    plt.legend()

    # Line is drawn onto matplotlib
    draw_line(-1 * weights[1] / weights[2], -1 * weights[0] / weights[2])

    # Displays fourth graph
    plt.subplot(3, 2, 4)
    plt.plot(iterations, errors)
    plt.xlabel('Iterations')
    plt.ylabel('Mean Squared Error')

    # Updates weights completely
    learning_rate = 0.5
    error = mse([input[0], input[1]], weights, input[3])
    errors.append(error)
    iterations.append(index)
    while error > 0.04:
        weights = add_1d_matrices(weights, scalar_times_1d_matrix(learning_rate,
                                                                  gradient([input[0], input[1]], weights, input[3])))
        error = mse([input[0], input[1]], weights, input[3])
        index += 1
        errors.append(error)
        iterations.append(index)

    # Here begins the fifth plot
    plt.subplot(3, 2, 5)
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.ylim((0.7, 2.9))
    plt.xlim((2.5, 7.5))
    plt.title('End')
    plt.legend()

    # Line is drawn onto matplotlib
    draw_line(-1 * weights[1] / weights[2], -1 * weights[0] / weights[2])

    # Displays sixth graph
    plt.subplot(3, 2, 6)
    plt.plot(iterations, errors)
    plt.xlabel('Iterations')
    plt.ylabel('Mean Squared Error')

    plt.tight_layout()

    # Plot is shown
    plt.show()


# Runs main method
if __name__ == "__main__": main()