import unittest
from unittest.mock import call, patch

from maze import Maze


class TestMaze(unittest.TestCase):

    def test_break_entrance_and_exit(self):
        maze = Maze(
            x1=0,
            y1=0,
            num_rows=2,
            num_cols=3,
            cell_size_x=10,
            cell_size_y=10,
        )

        cells = maze._Maze__cells

        # Reset walls because the constructor already breaks them
        cells[0][0].has_top_wall = True
        cells[2][1].has_bottom_wall = True

        with patch.object(maze, "_Maze__draw_cell") as draw_cell:
            maze._Maze__break_entrance_and_exit()

        self.assertFalse(cells[0][0].has_top_wall)
        self.assertFalse(cells[2][1].has_bottom_wall)

        draw_cell.assert_has_calls([
            call(0, 0),
            call(2, 1),
        ])

        self.assertEqual(draw_cell.call_count, 2)

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 3, 3, 10, 10)

        cells = maze._Maze__cells

        # Mark every cell as visited
        for column in cells:
            for cell in column:
                cell.visited = True

        # Reset visited properties
        maze._Maze__reset_cells_visited()

        # Verify every cell was reset
        for column in cells:
            for cell in column:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
