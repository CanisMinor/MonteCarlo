import random

def areas(N_iter):
    '''
    function: areas
    ---------------
    returns the approximate area under the curve y = x^2 in the domain [0,1]

    parameters:
        N_iter: number of iterations used in Monte Carlo simulation

    returns: approximate area under the curve y = x^2
    '''

    random.seed(123)

    count_under = 0

    for _ in range(0, N_iter):
        x = random.random()
        y = random.random()

        if y < x*x:
            count_under +=1


    return float(count_under) / float(N_iter)





