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

    def draw(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # Skip drawing if no window is provided
        if self._win is None:
            return

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

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
