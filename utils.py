import math
import random

INFINITY = math.inf
PI = 3.1415926535897932385

RAND_MAX = 1000000


def degrees_to_radias(degrees):
    return degrees * PI / 180.0


def rand():
    return random.random()


def rand_range(minimum, maximum):
    return minimum + (maximum-minimum)*rand()


def clamp(x, minimum, maximum):
    if x < minimum:
        return minimum
    if x > maximum:
        return maximum
    return x