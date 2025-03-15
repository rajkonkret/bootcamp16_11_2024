import numpy as np


def lift(a, b):
    a_mean = np.mean(a)
    b_mean = np.mean(b)

    lift = (b_mean - a_mean) / a_mean

    return str(round(lift * 100, 2)) + '%'




