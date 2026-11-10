from graphics import Window
from maze import Maze


def main():
    win = Window(1000, 700)

    Maze(
        25,
        25,
        20,     # 20 rows
        30,     # 30 columns
        25,     # Cell width
        25,     # Cell height
        win=win,
    )

    # Keep the window open until the user closes it
    win.wait_for_close()


if __name__ == "__main__":
    main()
