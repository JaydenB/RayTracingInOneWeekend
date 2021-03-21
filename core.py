import constants
import image
from geom.vector import Vector3
import colour


def main():
    image_width = 256
    image_height = 256

    render_data = list()
    print("Commencing Rendering.")
    for j in reversed(range(0, image_height)):
        print("Scanlines remaining: %s" % j, end="\r")
        for i in range(0, image_width):
            r = i / (image_width-1)
            g = j / (image_height-1)
            b = 0.25

            pixel_colour = Vector3(i/(image_width-1),
                                   j/(image_height-1),
                                   0.25)

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
