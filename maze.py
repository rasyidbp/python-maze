import time

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window,
    ) -> None:
        # Store constructor arguments
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        # Initialize the grid
        self.__cells = []

        # Create and draw cells
        self.__create_cells()

    def __create_cells(self) -> None:
        # Create columns containing rows
        for i in range(self.__num_cols):
            column = []

            for j in range(self.__num_rows):
                column.append(Cell(self.__win))

            self.__cells.append(column)

        # Draw all cells
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int) -> None:
        # Calculate cell coordinates
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y

        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        # Draw the cell
        self.__cells[i][j].draw(x1, y1, x2, y2)

        # Animate the drawing
        self.__animate()

    def __animate(self) -> None:
        self.__win.redraw()
        time.sleep(0.05)
