import math
import numpy as np


class Vector3:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

        self.value = (self.x, self.y, self.z)

    def __str__(self):
        return "Vector%s" % str(self.value)

    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        return Vector3(self.x*float(other), self.y*float(other), self.z*float(other))

    def __truediv__(self, other):
        return Vector3(self.x/other, self.y/other, self.z/other)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def length_squared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    def normalised(self):
        return self/self.length()

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)

    def sqr(self):
        return self.dot(self)

    def colour_mult(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
