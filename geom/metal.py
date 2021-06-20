from material import Material
from geom.vector import Vector3
from geom.ray import Ray


class Metal(Material):
    def __init__(self, a):
        self.albedo = a

    def scatter(self, r_in, rec):
        reflected = Vector3.reflect(r_in.direction.normalized(), rec.normal)
        # Catch degenerate scatter direction
        if reflected.near_zero():
            reflected = rec.normal
        scattered = Ray(rec.pos, reflected)
        attenuation = self.albedo
        return scattered.direction.dot(rec.normal) > 0, scattered, attenuation
