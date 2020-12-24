from tkinter import *
from additional.movement import coords
import controller


class menu:
    button: Button
    logo = ""

    def initialize(self, start_button_callback):
        self.button = Button(text="Begin",
                             background="#555",
                             foreground="#ccc",
                             padx="50",
                             pady="8",
                             font="16",
                             command=start_button_callback)
        self.button.place(rely=.7, relx=.5, anchor="c")

    def destroy(self):
        self.button.destroy()
        self.destroy()


class window:
    __root: Tk
    __HEIGHT: int = 0
    __WIDTH: int = 0

    def __init__(self):
        self.__root = Tk()

    def root(self) -> Tk:
        return self.__root

    def HEIGHT(self) -> int:
        return self.__HEIGHT

    def WIDTH(self) -> int:
        return self.__WIDTH

    def initialize(self):
        self.__HEIGHT = round(self.__root.winfo_screenheight() / 1.8)
        self.__WIDTH = round(self.__HEIGHT / 1.5)
        self.__root.title("Tetris")
        self.__root.geometry(f"{self.__WIDTH}x{self.__HEIGHT}")
        self.__root.resizable(False, False)
        self.__root.mainloop()
        return


class game:
    __size = 1
    __rectangle_border_x: int = 0
    __rectangle_border_y: int = 0
    __ITEM_SIZE: int = 0
    __canvas: Canvas

    def canvas(self) -> Canvas:
        return self.__canvas

    def rectangle_border_x(self) -> int:
        return self.__rectangle_border_x

    def rectangle_border_y(self) -> int:
        return self.__rectangle_border_y

    def ITEM_SIZE(self) -> int:
        return self.__ITEM_SIZE

    def initialize(self):
        self.__rectangle_border_x = visual.window().WIDTH() // (4 * self.__size)
        self.__ITEM_SIZE = (visual.window().WIDTH() - 2 * self.__rectangle_border_x) // 10
        self.__rectangle_border_y = (visual.window().HEIGHT() - 20 * self.__ITEM_SIZE) // 2
        self.create_canvas()
        self.draw_grid()

    def create_canvas(self):
        self.__canvas = Canvas(width=visual.window().WIDTH(), height=visual.window().HEIGHT(), bg='black')
        self.__canvas.pack()
        self.__canvas.focus_set()

    def draw_grid(self):
        self.canvas().create_rectangle(self.rectangle_border_x(), self.rectangle_border_y(),
                                       visual.window().WIDTH() - self.rectangle_border_x(),
                                       visual.window().HEIGHT() - self.rectangle_border_y(), fill='gray')
        for i in range(11):
            self.canvas().create_line(self.rectangle_border_x() + self.ITEM_SIZE() * i, self.rectangle_border_y(),
                                      self.rectangle_border_x() + self.ITEM_SIZE() * i,
                                      visual.window().HEIGHT() - self.rectangle_border_y())
        for i in range(21):
            self.canvas().create_line(self.rectangle_border_x(), self.rectangle_border_y() + self.ITEM_SIZE() * i,
                                      visual.window().WIDTH() - self.rectangle_border_x(),
                                      self.rectangle_border_y() + self.ITEM_SIZE() * i)

    def refresh_figures(self):
        for _figure in controller.controller.grid().get_figures_with_falling():
            for cell in _figure.get_cells_with_main():
                if cell.is_created():
                    self.synchronize_cell(cell)
                else:
                    points = self.grid_to_pixels_cell(cell.get_x(), cell.get_y())
                    cell.set_number(
                        self.canvas().create_rectangle(points[0].x, points[0].y, points[1].x,
                                                       points[1].y, fill=_figure.get_color()))
        self.__canvas.focus_set()

    def synchronize_cell(self, cell):
        points = self.grid_to_pixels_cell(cell.get_x(), cell.get_y())
        self.canvas().coords(cell.get_number(), points[0].x, points[0].y, points[1].x, points[1].y)

    def grid_to_pixels_cell(self, x: int, y: int):
        vec = [self.grid_to_pixels_point(x, y), self.grid_to_pixels_point(x + 1, y + 1)]
        return vec

    def grid_to_pixels_point(self, x: int, y: int):
        vec = coords(self.rectangle_border_x() + self.ITEM_SIZE() * x,
                     self.rectangle_border_y() + self.ITEM_SIZE() * y)
        return vec


class visual:
    __menu: menu = menu()
    __window: window = window()
    __game: game = game()

    @staticmethod
    def menu() -> menu:
        return visual.__menu

    @staticmethod
    def window() -> window:
        return visual.__window

    @staticmethod
    def game() -> game:
        return visual.__game

    def __init__(self):
        assert "Visual can not be created. It is a static class"