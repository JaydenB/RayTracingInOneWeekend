from material import Material
from geom.vector import Vector3
from geom.ray import Ray
from geom.hittable import HitRecord


class DiffuseLight(Material):
    def __init__(self, a, c):
        self.emit = a
        self.colour = c

    def scatter(self, r_in, rec):
        return False, Ray(Vector3(0,0,0), Vector3(0,0,0)), HitRecord(Vector3(0,0,0), 0.0)

    def emitted(self):
        return self.colour
