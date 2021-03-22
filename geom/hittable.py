import math
from geom.vector import Vector3


class Hittable:
    def hit(self, r, t_min, t_max, rec):
        pass


class HitRecord:
    def __init__(self, pos, t):
        self.pos = pos
        self.normal = Vector3(0, 0, 0)
        self.t = t

        self.front_face = False

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.direction.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class HittableList(Hittable):
    def __init__(self, *args):
        super().__init__(*args)
        self.objects = list()

    def append(self, appendage):
        self.objects.append(appendage)

    def hit(self, r, t_min, t_max, recc=None):
        temp_rec = HitRecord(Vector3(0, 0, 0), 0.0)
        hit_anything = False
        closest_so_far = t_max
        rec = None
        for obj in self.objects:
            if obj.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec

        return hit_anything, rec
