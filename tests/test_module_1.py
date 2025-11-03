from sudoku_solver.cell import Cell
from sudoku_solver.sudoku import Sudoku


def test_first_cell():
    first_cell = Cell(1)
    assert first_cell.value == 1
