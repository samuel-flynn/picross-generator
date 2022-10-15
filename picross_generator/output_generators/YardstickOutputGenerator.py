
import logging

from picross_generator.model.Image import Image


def get_sizing(image: Image):

    max_clues_per_column = 0
    for column in image.column_metadata:
        num_clues = len(column.values)
        if num_clues > max_clues_per_column:
            max_clues_per_column = num_clues

    logging.info(f'Columns: {str(max_clues_per_column)}')

    max_clues_per_row = 0
    for row in image.row_metadata:
        num_clues = len(row.values)
        if num_clues > max_clues_per_row:
            max_clues_per_row = num_clues

    logging.info(f'Rows: {str(max_clues_per_row)}')

    return [max_clues_per_column, max_clues_per_row]
