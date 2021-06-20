import math
import numpy as np

import utils


M_PI_F = math.pi
M_PI_2_F = math.pi / 2
M_PI_4_F = math.pi / 4


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

    def mul(self, other):
        return Vector3(self.x * other.x, self.y*other.y, self.z*other.z)

    def __truediv__(self, other):
        return Vector3(self.x/other, self.y/other, self.z/other)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def length_squared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    def normalized(self):
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

    @classmethod
    def random(cls, ):
        return Vector3(utils.rand(), utils.rand(), utils.rand())

    @classmethod
    def random_range(cls, minimum, maximum):
        return Vector3(utils.rand_range(minimum, maximum),
                       utils.rand_range(minimum, maximum),
                       utils.rand_range(minimum, maximum))

    @classmethod
    def random_in_unit_sphere(cls):
        while True:
            p = Vector3.random_range(-1.0, 1.0)
            if p.length_squared() >= 1:
                continue
            return p

    @classmethod
    def random_in_unit_disk(cls, u=0.0, v=0.0, sample=0):
        # # PHASE 1
        left_crop = 0.5
        right_crop = 0.0
        # top_crop = 0.0
        # bottom_crop = 0.0
        # v_mult = min(v-0.5, 0)
        sample_count = 10
        while True:
            p = Vector3(utils.rand_range(-1, 1),
                        utils.rand_range(-1, 1),
                        0)
            if p.length_squared() >= 1:
                continue
            # p = Vector3.concentric_sample_disk(u/((sample+1)/sample_count),
            #                                    v/((sample+1)/sample_count))
            m = u*2-1
            if p.x/2+0.5 > left_crop*(0 if m>0 else -m):
                return p
            # return p
        # # PHASE 2
        # return Vector3(utils.rand_range(-1, 1),
        #                utils.rand_range(-1, 1),
        #                0)

        # PHASE 3
        # a = 2.0 * u - 1.0
        # b = 2.0 * v - 1.0
        #
        # if a == 0 and b == 0:
        #     return [0.0, 0.0]
        # elif a * a > b * b:
        #     r = a
        #     phi = M_PI_4_F * (b / a)
        # else:
        #     r = b
        #     phi = M_PI_2_F - M_PI_4_F * (a / b)
        #
        # return Vector3(r * math.cos(phi), r * math.sin(phi), 0)

    @staticmethod
    def concentric_sample_disk(u1, u2):
        a = 2.0 * u1 - 1.0
        b = 2.0 * u2 - 1.0

        if a == 0 and b == 0:
            return [0.0, 0.0]
        elif a * a > b * b:
            r = a
            phi = M_PI_4_F * (b / a)
        else:
            r = b
            phi = M_PI_2_F - M_PI_4_F * (a / b)

        return Vector3(r * math.cos(phi), r * math.sin(phi), 0)

    @classmethod
    def random_unit_vector(cls):
        return Vector3.random_in_unit_sphere().normalized()

    def near_zero(self):
        s = 0.000000001
        return math.fabs(self.x < s) and math.fabs(self.y < s) and math.fabs(self.z < s)

    @staticmethod
    def reflect(v, n):
        return v - n*v.dot(n)*2

