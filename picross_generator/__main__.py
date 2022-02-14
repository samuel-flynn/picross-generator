import os
from picross_generator import resources_dir
from picross_generator.image_readers.ImageReader import read_image
from picross_generator.output_generators.CsvOutputGenerator import export_to_csv

def main():

    source_dir = os.path.join(resources_dir, 'images')
    files = [os.path.join(source_dir, file) for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    for file in files:
        image = read_image(file)
        export_to_csv(image)

if __name__ == '__main__':
    main()