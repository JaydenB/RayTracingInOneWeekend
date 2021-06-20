import math

import constants
import image
from geom.vector import Vector3
import colour
from geom.ray import Ray
import utils
from geom.hittable import HitRecord, HittableList
from geom.sphere import Sphere
from camera import Camera

from geom.lambertian import Lambertian
from geom.metal import Metal
from geom.diffuse_light import DiffuseLight

from datetime import datetime


def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.sqr()
    half_b = oc.dot(r.direction)
    c = oc.sqr() - radius*radius
    discriminant = half_b*half_b - a*c
    if discriminant < 0:
        return -1.0
    else:
        return (-half_b - math.sqrt(discriminant)) / a


def ray_colour(r, background, world, depth):
    hit, rec = world.hit(r, 0.001, utils.INFINITY)

    if depth <= 0:
        return Vector3(0, 0, 0)

    if not hit:
        return background

    emitted = rec.material.emitted()
    result, scattered, attenuation = rec.material.scatter(r, rec)
    if not result:
        return emitted

    return emitted + attenuation.mul(ray_colour(scattered, background, world, depth-1))


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 256
    image_height = image_width/aspect_ratio
    background = Vector3(0, 0, 0)
    samples_per_pixel = 20
    max_depth = 1

    # World
    world = HittableList()

    # material_ground = Lambertian(Vector3(0.8, 0.8, 0.0))
    # material_center = Lambertian(Vector3(0.7, 0.3, 0.3))
    # material_left = Metal(Vector3(0.8, 0.8, 0.8))
    material_emissive = DiffuseLight(Vector3(1,1,1), Vector3(1,1,1))
    # material_right = Metal(Vector3(0.8, 0.6, 0.2))

    # world.append(Sphere(Vector3(0, 0, -1), 0.5, material_center))
    # world.append(Sphere(Vector3(1, 0.5, -0.5), 1, material_emissive))
    # world.append(Sphere(Vector3(-1, 0, -1), 0.5, material_right))
    # world.append(Sphere(Vector3(0, -100.5, -1), 100, material_ground))
    sphere_count = 35
    sphere_dist = 100
    for i in range(0, sphere_count):
        world.append(Sphere(Vector3(utils.rand_range(-50, 50), utils.rand_range(-40, 40),
                                    sphere_dist),
                            1,
                            material_emissive))

    # Camera
    look_from = Vector3(0, 0, 0)
    look_at = Vector3(0, 0, 1)
    v_up = Vector3(0, 1, 0)
    dist_to_focus = (look_from - look_at).length()
    f_stop = 8
    aperture = 1/f_stop
    cam = Camera(look_from, look_at, v_up, 30.0, aspect_ratio, aperture, dist_to_focus)

    # Render
    render_data = list()
    print("Commencing Rendering.")
    start_time = datetime.now()
    for j in reversed(range(0, int(image_height))):
        print("Scanlines remaining: %s" % j)
        for i in range(0, image_width):
            pixel_colour = Vector3(0, 0, 0)
            for s in range(0, samples_per_pixel):
                u = (i + utils.rand()) / (image_width-1)
                v = (j + utils.rand()) / (image_height-1)
                r = cam.get_ray(u, v, s)
                pixel_colour += ray_colour(r, background, world, max_depth)
            render_data.append(colour.write_colour(pixel_colour, samples_per_pixel))
    print("\nDone.\nTime Spent: %s" % (datetime.now() - start_time))

    file = image.write_image(
        width=image_width,
        height=image_height,
        data=render_data
    )
    return file


if __name__ == "__main__":
    image_path = main()
    print("File path: %s" % image_path)
