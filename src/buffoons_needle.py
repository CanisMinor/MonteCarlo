import random
import math
import numpy as np

def buffoons_needle(N_iter):
    '''
    function: buffoons_needle
    -------------------------
    evaluates the approximate probability that a needle (of unit length) dropped on a board with parallel lines
    (separated by unit distance) will cross one of the lines

    parameters:
        L: separation between parallel lines on board

    returns: probability of needle crossing one of the lines
    '''

    random.seed(124245)

    count_crossed = 0

    for _ in range(0, N_iter):
        theta = random.random() * np.pi / 2.0
        centre_distance = random.random() * 0.5

        if centre_distance / math.sin(theta) < 0.5:
            count_crossed += 1

    approx_pi = 2.0 * float(N_iter) / float(count_crossed)

    return approx_pi

print(buffoons_needle(10000000))




