"""An inherited class object should be able to replace the base class object (interface object) from which it was
 inherited"""


class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self.width * self.height

    def __str__(self) -> str:
        return f"Width: {self._width}, Height: {self._height}"

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


class Square(Rectangle):
    def __init__(self, size):
        super.__init__(size, size)

    @Rectangle.width.setter  # wrong implementation as this will change the way the area is calculated for a square
    def width(self, value):
        self._width = self._width = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)
