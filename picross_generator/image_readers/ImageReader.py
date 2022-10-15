import re
import png
import urllib.request
from picross_generator.image_readers.FileNameFilter import filter_name
from picross_generator.image_readers.ImageMatrixBuilder import ImageBuilder

def read_image(file_path : str):
    
    file_url = 'file:///' + file_path.replace("\\", "/")
    file_name_tokens = file_url.split('/')
    file_name = file_name_tokens[len(file_name_tokens) - 1]
    file_name_extension_tokens = file_name.split('.')
    name = file_name_extension_tokens[len(file_name_extension_tokens) - 2]
    name = filter_name(name)

    reader = png.Reader(file=urllib.request.urlopen(file_url))
    raw_image = reader.asRGBA()
    width = raw_image[0]
    rows = raw_image[2]

    builder = ImageBuilder(name, width)

    for row in rows:
        for pixel_index in range(width):

            start_index = pixel_index * 4
            r = row[start_index]
            g = row[start_index + 1]
            b = row[start_index + 2]
            a = row[start_index + 3]

            is_blank = a == 0 or (r == 255 and g == 255 and b == 255)

            builder.append(not is_blank)

    return builder.finalize()