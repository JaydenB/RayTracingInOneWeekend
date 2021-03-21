import os
import math

import constants


def write_image(width, height, data):
    file_path = get_new_file_path()

    f = list()
    f.append("P3")
    f.append("%s %s" % (width, height))
    f.append("255")

    for d in data:
        f.append(d)

    image_file = open(file_path, "w")
    for line in f:
        image_file.write(line)
        image_file.write("\n")
    image_file.close()

    return file_path


def get_new_file_path():
    entries = os.listdir(constants.RENDER_PATH)
    return "%srender_%s.ppm" % (constants.RENDER_PATH, str(len(entries)+1).zfill(3))
