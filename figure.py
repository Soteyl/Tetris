from abc import ABC, abstractmethod
from typing import Tuple, List


class cell:
    __number: int
    __x: int
    __y: int
    __created = False

    def set_number(self, number: int):
        if not self.__created:
            __number = number

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def move(self, move_X: int, move_Y: int):
        self.__x += move_X
        self.__y += move_Y


class figure(ABC):

    __color: str
    __cell_coords: Tuple[List[List[int]]] = ()
    __cells: List[cell] = []
    __state: int = 0
    __is_falled: bool = False

    def __init__(self) -> None:
        for row in range(len(self.__cell_coords[self.__state])):
            for column in range(len(self.__cell_coords[self.__state][row])):
                if self.__cell_coords[row][column] == 1:
                    self.__cells.append(cell(column, row))

    def rotate(self, state: int):
        pass

    def change_state_rotation(self):
        self.__state = (self.__state + 1) // len(self.__cell_coords)

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move(self, side_X: int, side_Y: int):
        for _cell in self.__cells:
            _cell.move(side_X, side_Y)

    def get_state_number(self) -> int:
        return self.__state

    def get_state(self, number: int):
        return self.__cell_coords[number]