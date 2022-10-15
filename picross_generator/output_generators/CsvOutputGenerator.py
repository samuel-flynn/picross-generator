import csv
import os
import pathlib

from picross_generator import resources_dir
from picross_generator.model.Image import Image

trailer_columns = 0
trailer_rows = 0

header_columns = 17
header_rows = 16

image_rows = 70
image_columns = 70


def export_to_csv(image: Image):

    key_parent_folder = os.path.join(resources_dir, 'csv', 'key')
    pathlib.Path(key_parent_folder).mkdir(parents=True, exist_ok=True)
    puzzle_parent_folder = os.path.join(resources_dir, 'csv', 'puzzle')
    pathlib.Path(puzzle_parent_folder).mkdir(parents=True, exist_ok=True)

    with open(os.path.join(key_parent_folder, f'{image.name}.csv'), 'w+', newline='') as key_file:
        with open(os.path.join(puzzle_parent_folder, f'{image.name}.csv'), 'w+', newline='') as puzzle_file:
            key_writer = csv.writer(key_file, delimiter=',')
            puzzle_writer = csv.writer(puzzle_file, delimiter=',')

            # Header Phase
            for header_row in range(header_rows):

                key_row = []
                puzzle_row = []

                for header_column in range(header_columns):
                    if header_row == header_rows - 1 and header_column == header_columns - 1:
                        key_row.append(f'{image.name} (answer key)')
                        puzzle_row.append(image.name)
                    else:
                        key_row.append('')
                        puzzle_row.append('')

                for column in image.column_metadata:

                    num_clues = len(column.values)
                    num_blanks = header_rows - num_clues
                    if header_row >= num_blanks:
                        key_row.append(
                            str(column.values[header_row - num_blanks]))
                        puzzle_row.append(
                            str(column.values[header_row - num_blanks]))
                    else:
                        key_row.append('')
                        puzzle_row.append('')

                key_writer.writerow(key_row)
                puzzle_writer.writerow(puzzle_row)

            # Main Phase
            for row_num in range(len(image.row_metadata)):

                # Row Headers
                key_row = []
                puzzle_row = []
                matrix_row = image.image_matrix.matrix[row_num]
                row_metadata = image.row_metadata[row_num]
                str_metadata = [str(val) for val in row_metadata.values]
                num_blanks = header_columns - len(row_metadata.values)

                for header_column in range(header_columns):
                    if header_column >= num_blanks:
                        key_row.append(
                            str_metadata[header_column - num_blanks])
                        puzzle_row.append(
                            str_metadata[header_column - num_blanks])
                    else:
                        key_row.append('')
                        puzzle_row.append('')

                # Main Matrix

                for column in matrix_row:
                    if column:
                        key_row.append('X')
                        puzzle_row.append('')
                    else:
                        key_row.append('')
                        puzzle_row.append('')

                key_writer.writerow(key_row)
                puzzle_writer.writerow(puzzle_row)
