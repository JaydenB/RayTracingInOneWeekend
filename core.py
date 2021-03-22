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


def ray_colour(r, world):
    hit, rec = world.hit(r, 0, utils.INFINITY)
    if hit:
        return (rec.normal + Vector3(1, 1, 1)) * 0.5
    unit_direction = r.direction.normalized()
    t = 0.5*(unit_direction.y + 1.0)
    return Vector3(1.0, 1.0, 1.0)*(1.0-t) + Vector3(0.5, 0.7, 1.0)*t


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = image_width/aspect_ratio
    samples_per_pixel = 5

    # World
    world = HittableList()
    world.append(Sphere(Vector3(0, 0, -1), 0.5))
    world.append(Sphere(Vector3(0, -100.5, -1), 100))

    # Camera
    cam = Camera()

    # Render
    render_data = list()
    print("Commencing Rendering.")
    start_time = datetime.now()
    for j in reversed(range(0, int(image_height))):
        print("Scanlines remaining: %s" % j, end="\r")
        for i in range(0, image_width):
            pixel_colour = Vector3(0, 0, 0)
            for s in range(0, samples_per_pixel):
                u = (i + utils.rand()) / (image_width-1)
                v = (j + utils.rand()) / (image_height-1)
                r = cam.get_ray(u, v)
                pixel_colour += ray_colour(r, world)
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
