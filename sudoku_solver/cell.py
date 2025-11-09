class Cell:
    """
    Represents a single cell in a Sudoku grid.

    Attributes:
        value (int): The current value of the cell (0 means empty).
    """
    def __init__(self, value: int) -> None:
        """
        Stores the value of a cell (0 means empty).

        Parameters:
            value (int): The value of the cell.

        Returns:
            None.
        """
        self.value = value

    def __repr__(self) -> str:
        return f"Cell({self.value})"

    def __str__(self) -> str:
        return str(self.value)