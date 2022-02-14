from typing import List
from picross_generator.model.ImageMatrix import ImageMatrix
from picross_generator.model.RowColumnMetadata import RowColumnMetadata


class Image:

    name : str
    image_matrix : ImageMatrix
    column_metadata : List[RowColumnMetadata]
    row_metadata : List[RowColumnMetadata]

    def __init__(self) -> None:
        self.image_matrix = ImageMatrix()
        self.column_metadata = []
        self.row_metadata = []