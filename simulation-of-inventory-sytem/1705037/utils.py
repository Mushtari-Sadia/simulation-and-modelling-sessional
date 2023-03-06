from lcgrand import *
import math


def expon(mean):
    val = -mean * math.log(lcgrand(1))
    return val


def uniform(a, b):
    return a + (b - a) * lcgrand(1)


def random_integer(prob_distrib):
    u = lcgrand(1)
    i = 0
    while u >= prob_distrib[i]:
        i += 1
    return i+1