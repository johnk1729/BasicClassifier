import matplotlib.pyplot as plt
import numpy as np
import csv


# Reads through the irisdata.csv file
def read_csv():
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    species = []

    # Opens csv file and adds data into respective lists
    with open('irisdata.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        for row in reader:
            sepal_length.append(row[0])
            sepal_width.append(row[1])
            petal_length.append(row[2])
            petal_width.append(row[3])
            species.append(row[4])

    # Places only data in x and y lists
    x = petal_length[1:len(petal_length)]
    y = petal_width[1:len(petal_width)]
    species_class = species[1:len(species)]

    output = []
    output.append(x)
    output.append(y)
    output.append(species_class)

    return output


# Converts any array to have float values (if possible)
def convert_to_float(array):
    # Converts data from strings into floats
    return [float(i) for i in array]


# Returns the x and y values for virginica and versicolor for plotting
def get_xy(x, y, species_class):

    versicolor_x = []
    versicolor_y = []
    virginica_x = []
    virginica_y = []

    # Loop differentiates by class (species) and places them in different lists
    i = 0
    while i < len(species_class):
        if species_class[i] == 'versicolor':
            versicolor_x.append(x[i])
            versicolor_y.append(y[i])
        if species_class[i] == 'virginica':
            virginica_x.append(x[i])
            virginica_y.append(y[i])
        i += 1

    return [virginica_x, virginica_y, versicolor_x, versicolor_y]


# 2D plots the second and third class data points
def plot_2d_scatter(virginica_x, virginica_y, versicolor_x, versicolor_y):
    # Adds data to scatter plots
    plt.scatter(virginica_x, virginica_y, c='red', label='Virginica', s=35, marker='x')
    plt.scatter(versicolor_x, versicolor_y, c='blue', label='Versicolor', s=35, marker='+')


# Main method
def main():
    input = read_csv()
    input[0] = convert_to_float(input[0])
    input[1] = convert_to_float(input[1])

    scatter_data = get_xy(input[0], input[1], input[2])
    plot_2d_scatter(scatter_data[0], scatter_data[1], scatter_data[2], scatter_data[3])

    # Organization of scatter plot
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.title('Petal Width (cm) vs Petal Length (cm)\n of Versicolor and Virginica Irises')
    plt.legend()
    plt.show()


# Runs main method
if __name__ == "__main__": main()
