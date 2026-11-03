
from tkinter import Tk, BOTH, Canvas


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

    def close(self):
        """Stop the window's update loop."""
        self.__is_running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
