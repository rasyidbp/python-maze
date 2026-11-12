from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    # Create a 10x10 maze
    maze = Maze(
        50,
        50,
        10,
        10,
        50,
        50,
        win,
    )

    win.wait_for_close()


if __name__ == "__main__":
    main()
