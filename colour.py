def write_colour(pixel_colour):
    return "%s %s %s" % (
        255.999*pixel_colour.x,
        255.999*pixel_colour.y,
        255.999*pixel_colour.z
    )