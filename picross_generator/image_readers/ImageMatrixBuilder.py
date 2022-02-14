from typing import List
from picross_generator.model.Image import Image
from picross_generator.model.ImageMatrix import ImageMatrix
from picross_generator.model.RowColumnMetadata import RowColumnMetadata

class ImageBuilder:

    image : Image

    name : str
    row : int
    column : int
    width : int

    def __init__(self, name, width) -> None:
        self.row = 0
        self.column = 0
        self.width = width

        self.image = Image()
        self.image.name = name
        self.image.image_matrix = ImageMatrix()
        self.image.image_matrix.matrix = []

    def append(self, colored : bool):

        if self.column == 0:
            self.image.image_matrix.matrix.append([])

        self.image.image_matrix.matrix[self.row].append(colored)

        self.column += 1

        if self.column >= self.width:
            self.column = 0
            self.row += 1
    
    def finalize(self):

        matrix = self.image.image_matrix.matrix
        columns_metadata : List[RowColumnMetadata] = []
        columns_currently_colored : List[bool] = []
        columns_counters : List[int] = []

        for column_index in range(self.width):
            columns_metadata.append(RowColumnMetadata())
            columns_currently_colored.append(False)
            columns_counters.append(0)

        for row_index in range(len(matrix)):
            row = matrix[row_index]
            row_metadata = RowColumnMetadata()
            row_currently_colored = False
            row_counter = 0

            for column_index in range(len(row)):
                column = row[column_index]
                if column:
                    row_currently_colored = True
                    row_counter += 1

                    columns_currently_colored[column_index] = True
                    columns_counters[column_index] += 1
                else:
                    if row_currently_colored:
                        row_metadata.values.append(row_counter)
                        row_currently_colored = False
                        row_counter = 0

                    if columns_currently_colored[column_index]:
                        columns_metadata[column_index].values.append(columns_counters[column_index])
                        columns_currently_colored[column_index] = False
                        columns_counters[column_index] = 0
                
                if row_index == len(matrix) - 1:
                    if columns_currently_colored[column_index]:
                        columns_metadata[column_index].values.append(columns_counters[column_index])
                        columns_currently_colored[column_index] = False
                        columns_counters[column_index] = 0

                    elif len(columns_metadata[column_index].values) == 0:
                        columns_metadata[column_index].values.append(0)
            
            if row_currently_colored:
                row_metadata.values.append(row_counter)
                row_currently_colored = False
                row_counter = 0

            
            if len(row_metadata.values) == 0:
                row_metadata.values.append(0)
            
            self.image.row_metadata.append(row_metadata)
        
        for column_metadata in columns_metadata:
            self.image.column_metadata.append(column_metadata)
        
        return self.image