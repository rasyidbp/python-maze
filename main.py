from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2
        )


class Window:
    def __init__(self, width, height):
        # Create the main window
        self.__root = Tk()
        self.__root.title("Maze Solver")

        # Create the canvas
        self.__canvas = Canvas(
            self.__root,
            width=width,
            height=height
        )
        self.__canvas.pack(fill=BOTH, expand=True)

        # Track whether the window is running
        self.__is_running = False

        # Handle the window's close button
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Update the window and process pending events."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Keep updating the window until it is closed."""
        self.__is_running = True

        while self.__is_running:
            self.redraw()

        self.__root.destroy()

    def close(self):
        """Stop the window's update loop."""
        self.__is_running = False

    def draw_line(self, line, fill_color):
        """Draw a line on the window's canvas."""
        line.draw(self.__canvas, fill_color)


def main():
    win = Window(800, 600)

    # Create points
    point1 = Point(100, 100)
    point2 = Point(300, 100)
    point3 = Point(300, 300)
    point4 = Point(100, 300)
    point5 = Point(400, 150)

    # Create lines
    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point1)
    line5 = Line(point1, point5)

    # Draw lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.draw_line(line4, "black")
    win.draw_line(line5, "purple")

    win.wait_for_close()


if __name__ == "__main__":
    main()
