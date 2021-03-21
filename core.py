import constants
import image
from geom.vector import Vector3
import colour
from geom.ray import Ray


def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.dot(r.direction)
    b = 2.0 * oc.dot(r.direction)
    c = oc.dot(oc) - radius*radius
    discriminant = b*b - 4*a*c
    return discriminant > 0


def ray_colour(r):
    if hit_sphere(Vector3(0, 0, -1), 0.5, r):
        return Vector3(1, 0, 0)
    unit_direction = r.direction.normalized()
    t = 0.5*(unit_direction.y + 1.0)
    return Vector3(1.0, 1.0, 1.0)*(1.0-t) + Vector3(0.5, 0.7, 1.0)*t


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = image_width/aspect_ratio

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Vector3(0, 0, 0)
    horizontal = Vector3(viewport_width, 0, 0)
    vertical = Vector3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vector3(0, 0, focal_length)

    render_data = list()
    print("Commencing Rendering.")
    for j in reversed(range(0, int(image_height))):
        print("Scanlines remaining: %s" % j, end="\r")
        for i in range(0, image_width):
            u = i / (image_width-1)
            v = j / (image_height-1)

            r = Ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)

            pixel_colour = ray_colour(r)

            render_data.append(colour.write_colour(pixel_colour))
    print("\nDone.\n")

    file = image.write_image(
        width=image_width,
        height=image_height,
        data=render_data
    )
    return file


if __name__ == "__main__":
    image_path = main()
    print("File path: %s" % image_path)
