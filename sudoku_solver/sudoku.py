from typing import List
from cell import Cell
import numpy as np


class Sudoku:
    def __init__(self, numbers: List[int]):
        self.dimension = int(np.sqrt(len(numbers)))
        self.grid = [
            [Cell(numbers[i * self.dimension + j])
             for j in range(self.dimension)]
            for i in range(self.dimension)
        ]

    def get_row(self, row: int) -> List[Cell]:
        return self.grid[row]

    def get_col(self, col: int) -> List[Cell]:
        return [self.grid[row][col] for row in range(self.dimension)]

    def get_block(self, block_row: int, block_col: int) -> List[List[Cell]]:
        if self.dimension <= 3:
            return self.grid
        else:
            block_size = int(np.sqrt(self.dimension))
            cells = [
                [self.grid[i][j] for j in range(
                    block_col * block_size,
                    block_size * (block_col + 1)
                    )]
                for i in range(
                    block_row * block_size,
                    (block_row + 1) * block_size
                    )
            ]
            return cells

    def is_valid(self, row, col, number):
        if any(cell.value == number for cell in self.get_row(row)):
            return False
        if any(cell.value == number for cell in self.get_col(col)):
            return False
        block_row = row // int(np.sqrt(self.dimension))
        block_col = col // int(np.sqrt(self.dimension))
        block = self.get_block(block_row, block_col)
        if any(cell.value == number for r in block for cell in r):
            return False

        return True


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,
               4, 5, 6, 7, 8, 9, 1, 2, 3,
               7, 8, 9, 1, 2, 3, 4, 5, 6,
               2, 3, 4, 5, 6, 7, 8, 9, 1,
               5, 6, 7, 8, 9, 1, 2, 3, 4,
               8, 9, 1, 2, 3, 4, 5, 6, 7,
               3, 4, 5, 6, 7, 8, 9, 1, 2,
               6, 7, 8, 9, 1, 2, 3, 4, 5,
               9, 1, 2, 3, 4, 5, 6, 7, 8
               ]
    first_sudoku = Sudoku(numbers)
    for i in range(3):
        for j in range(3):
            print(first_sudoku.get_block(i, j))