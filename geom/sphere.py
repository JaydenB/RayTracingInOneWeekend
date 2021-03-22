import math

from geom.hittable import Hittable, HitRecord


class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max, rec):
        oc = r.origin - self.center
        a = r.direction.sqr()
        half_b = oc.dot(r.direction)
        c = oc.sqr() - self.radius*self.radius

        discriminant = half_b*half_b - a*c
        if discriminant < 0:
            return False
        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.pos = r.at(rec.t)
        rec.set_face_normal(r, (rec.pos - self.center) / self.radius)
        return True
