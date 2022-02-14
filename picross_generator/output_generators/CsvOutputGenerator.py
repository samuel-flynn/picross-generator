import csv
import os

from picross_generator.model.Image import Image
from picross_generator import resources_dir

def export_to_csv(image : Image):
    
    with open(os.path.join(resources_dir, 'csv', 'key', f'{image.name}.csv'), 'w', newline='') as key_file:
        with open(os.path.join(resources_dir, 'csv', 'puzzle', f'{image.name}.csv'), 'w', newline='') as puzzle_file:
            key_writer = csv.writer(key_file, delimiter = ',')
            puzzle_writer = csv.writer(puzzle_file, delimiter = ',')

            header_row = [image.name]
            for column in image.column_metadata:
                str_metadata = [str(val) for val in column.values]
                header_row.append(' '.join(str_metadata))
            
            key_writer.writerow(header_row)
            puzzle_writer.writerow(header_row)

            for row_index in range(len(image.row_metadata)):
                row_metadata = image.row_metadata[row_index]
                str_metadata = [str(val) for val in row_metadata.values]
                matrix_row = image.image_matrix.matrix[row_index]

                key_row = [' '.join(str_metadata)]
                puzzle_row = [' '.join(str_metadata)]
                for column in matrix_row:
                    if column:
                        key_row.append('X')
                        puzzle_row.append('')
                    else:
                        key_row.append('')
                        puzzle_row.append('')

                key_writer.writerow(key_row)
                puzzle_writer.writerow(puzzle_row)