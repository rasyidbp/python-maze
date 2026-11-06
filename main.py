from cell import Cell
from graphics import Window


def main() -> None:
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(0, 0, 50, 50)

    cell2 = Cell(win)
    cell2.draw(50, 0, 100, 50)

    cell1.draw_move(cell2, undo=True)

    win.wait_for_close()


main()
