import logging
import os

from picross_generator import resources_dir
from picross_generator.image_readers.ImageReader import read_image
from picross_generator.output_generators.CsvOutputGenerator import \
    export_to_csv
from picross_generator.output_generators.YardstickOutputGenerator import \
    get_sizing


def main():

    source_dir = os.path.join(resources_dir, 'images')
    files = [os.path.join(source_dir, file) for file in os.listdir(
        source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    maxes = [0, 0]
    for file in [filtered_file for filtered_file in files if True]:
        image = read_image(file)
        clues = get_sizing(image)
        if clues[0] > maxes[0]:
            maxes[0] = clues[0]

        if clues[1] > maxes[1]:
            maxes[1] = clues[1]
        export_to_csv(image)

    logging.info(
        f'Max clues in columns: {maxes[0]}, Max clues in rows: {maxes[1]}')


if __name__ == '__main__':
    main()
