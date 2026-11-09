from graphics import Window
from maze import Maze


def main():
    win = Window(1000, 700)

    maze = Maze(
        25,
        25,
        20,     # 20 rows
        30,     # 30 columns
        25,     # Cell width
        25,     # Cell height
        win
    )

def __animate(self) -> None:
    self.__win.redraw()
    time.sleep(0.05)

if __name__ == "__main__":
    main()
