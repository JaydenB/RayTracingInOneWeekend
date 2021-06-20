from geom.hittable import HitRecord
from geom.ray import Ray
from geom.vector import Vector3


class Material(object):

    def emitted(self):
        return Vector3(0, 0, 0)

    def scatter(self, r_in, rec):
        return True, Ray(Vector3(0,0,0), Vector3(0,0,0)), HitRecord(Vector3(0,0,0), 0.0)
