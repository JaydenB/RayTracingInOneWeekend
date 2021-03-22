import utils


def write_colour(pixel_colour, samples_per_pixel):
    r = pixel_colour.x
    g = pixel_colour.y
    b = pixel_colour.z

    scale = 1.0/samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    return "%s %s %s" % (
        256 * utils.clamp(r, 0.0, 0.999),
        256 * utils.clamp(g, 0.0, 0.999),
        256 * utils.clamp(b, 0.0, 0.999)
    )