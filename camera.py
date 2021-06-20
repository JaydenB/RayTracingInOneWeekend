import utils
from geom.vector import Vector3
from geom.ray import Ray
import math


class Camera:
    def __init__(self, look_from, look_at, v_up, v_fov, aspect_ratio, aperture, focus_dist):
        theta = utils.degrees_to_radias(v_fov)
        h = math.tan(theta/2)
        self.viewport_height = 2.0 * h
        self.viewport_width = aspect_ratio * self.viewport_height

        w = (look_from-look_at).normalized()
        self.u = v_up.cross(w).normalized()
        self.v = w.cross(self.u)
        self.focal_length = 1.0

        self.origin = look_from
        self.horizontal = self.u * self.viewport_width * focus_dist
        self.vertical = self.v * self.viewport_height * focus_dist
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - w*focus_dist

        self.lens_radius = aperture/2

    def get_ray(self, s, t, sample):
        rd = Vector3.random_in_unit_disk(s, t, sample) * self.lens_radius
        # rd = Vector3.concentric_sample_disk(s*2-1, t*2-1) * self.lens_radius
        offset = self.u * rd.x + self.v * rd.y
        return Ray(
            self.origin + offset,
            self.lower_left_corner + self.horizontal*s + self.vertical*t - self.origin - offset)
