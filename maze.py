import time
import random

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window | None = None,
        seed: int | None = None,
    ):
        self._win = win

        if seed is not None:
            random.seed(seed)

        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self) -> None:
        # Create columns containing rows
        for i in range(self.__num_cols):
            column = []

            for j in range(self.__num_rows):
                x1 = self.__x1 + i * self.__cell_size_x
                y1 = self.__y1 + j * self.__cell_size_y

                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y

                column.append(
                    Cell(x1, y1, x2, y2, self._win)
                )

            self.__cells.append(column)

        # Draw all cells
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int) -> None:
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self) -> None:
        # Skip animation if no window is provided
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self) -> None:
        # Remove the entrance (top wall of the top-left cell)
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # Remove the exit (bottom wall of the bottom-right cell)
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1

        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_r(self, i: int, j: int) -> None:
        # Mark the current cell as visited
        self.__cells[i][j].visited = True

        while True:
            # Store possible directions
            possible_directions = []

            # Check the cell to the left
            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))

            # Check the cell to the right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))

            # Check the cell above
            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))

            # Check the cell below
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            # No unvisited neighbours remain
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            # Randomly choose a direction
            direction = random.randrange(len(possible_directions))
            next_i, next_j = possible_directions[direction]

            # Remove the wall between the current cell and the next cell
            if next_i < i:
                # Moving left
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False

            elif next_i > i:
                # Moving right
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False

            elif next_j < j:
                # Moving up
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            elif next_j > j:
                # Moving down
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False

            # Recursively explore the chosen cell
            self.__break_walls_r(next_i, next_j)
