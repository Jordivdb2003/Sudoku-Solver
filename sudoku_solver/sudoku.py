from typing import List
from cell import Cell
import numpy as np


class Sudoku:
    def __init__(self, numbers: List[int]):
        self.dimension = int(np.sqrt(len(numbers)))
        self.numbers = [
            [Cell(numbers[i * self.dimension + j]) for j in range(self.dimension)]
            for i in range(self.dimension)
        ]

    def create_groups(self):
        dim = self.dimension
        self.rows = []
        self.cols = []

        for i in range(dim):
            self.rows.append(self.numbers[i * dim : (i + 1) * dim])
            self.cols.append(
                [number for j, number in enumerate(self.numbers) if j % dim == i]
            )
        if dim >= 4:
            square_dim = int(np.sqrt(dim))


if __name__ == "__main__":
    first_sudoku = Sudoku([1, 2, 3, 4, 5, 6, 7, 8, 9])
    first_sudoku.create_groups()
    print(first_sudoku.rows)
    print(first_sudoku.cols)
