from material import Material
from geom.vector import Vector3
from geom.ray import Ray


class Lambertian(Material):
    def __init__(self, a):
        self.albedo = a

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + Vector3.random_unit_vector()

        # Catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.pos, scatter_direction)
        attenuation = self.albedo
        return True, scattered, attenuation
