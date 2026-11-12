from graphics import Line, Point, Window


class Cell:
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        win: Window | None = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self):
        if self._win is None:
            return

        background_color = "#d9d9d9"

        walls = [
            (self.has_left_wall, self._x1, self._y1, self._x1, self._y2),
            (self.has_right_wall, self._x2, self._y1, self._x2, self._y2),
            (self.has_top_wall, self._x1, self._y1, self._x2, self._y1),
            (self.has_bottom_wall, self._x1, self._y2, self._x2, self._y2),
        ]

        for exists, x1, y1, x2, y2 in walls:
            color = "black" if exists else background_color

            self._win.draw_line(
                Line(Point(x1, y1), Point(x2, y2)),
                color,
            )

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if self._win is None:
            return

        color = "gray" if undo else "red"

        self._win.draw_line(
            Line(
                Point(
                    (self._x1 + self._x2) / 2,
                    (self._y1 + self._y2) / 2,
                ),
                Point(
                    (to_cell._x1 + to_cell._x2) / 2,
                    (to_cell._y1 + to_cell._y2) / 2,
                ),
            ),
            color,
        )
