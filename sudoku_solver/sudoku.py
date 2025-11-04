from typing import List, Optional, Tuple
from cell import Cell
import numpy as np


class Sudoku:
    def __init__(self, numbers: List[int]):
        self.dimension = int(np.sqrt(len(numbers)))
        if self.dimension >= 4:
            self.block_size = int(np.sqrt(self.dimension))
        else:
            self.block_size = self.dimension
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
            cells = [
                [self.grid[i][j] for j in range(
                    block_col * self.block_size,
                    self.block_size * (block_col + 1)
                    )]
                for i in range(
                    block_row * self.block_size,
                    (block_row + 1) * self.block_size
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
    
    def find_empty(self) -> Optional[Tuple[int, int]]:
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grid[i][j].value == 0:
                    return (i,j)
        return None
    
    def find_best_cell(self) -> Optional[Tuple[int, int]]:
        min_options = float('inf')
        best_cell = None
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.grid[row][col].value == 0:
                    options = [
                        num for num in range(1, self.dimension + 1)
                        if self.is_valid(row, col, num)
                    ]
                    if len(options) < min_options:
                        min_options = len(options)
                        best_cell = (row, col)
                    if min_options == 1:
                        return best_cell
        return best_cell

    def solve(self) -> bool:
        best = self.find_best_cell()
        if not best:
            return True
        row, col = best

        for num in range(1, self.dimension + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col].value = num
                if self.solve():
                    return True
                self.grid[row][col].value = 0

        return False

    def display(self):
        for i, row in enumerate(self.grid):
            if i % self.block_size == 0 and i != 0:
                print ("-" * (self.dimension * 2 + self.block_size - 1))
            row_str = ""
            for j, cell in enumerate(row):
                if j % self.block_size == 0 and j != 0:
                    row_str += "| "
                row_str += str(cell) + " "
            print(row_str)

if __name__ == "__main__":
    numbers = [0, 5, 0, 8, 0, 2, 0, 0, 7,
               0, 9, 7, 6, 1, 0, 4, 0, 0,
               3, 0, 0, 0, 4, 0, 0, 2, 1,
               0, 8, 2, 7, 0, 0, 5, 0, 0,
               0, 0, 0, 0, 5, 9, 8, 4, 0,
               0, 0, 6, 3, 0, 0, 0, 0, 0, 
               8, 0, 0, 0, 0, 6, 0, 9, 2,
               4, 3, 0, 9, 0, 0, 0, 6, 0,
               6, 0, 0, 1, 7, 5, 3, 8, 0
               ]
    sudoku = Sudoku(numbers)
    print("Original Puzzle:")
    sudoku.display()
    if sudoku.solve():
        print("\nSolved Puzzle:")
        sudoku.display()
    else:
        print("No solution exists")