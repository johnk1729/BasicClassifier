import numpy as np
import math
from p1a import *


# Takes the input data and the weights and returns the hypothesis space
def get_hypothesis_space(inputs, weights):
    return np.dot(inputs, weights)


# Takes a hypothesis space and returns the sigmoid of it
def sigmoid(hypothesis_space):
    return 1/(1 + math.exp(hypothesis_space))
