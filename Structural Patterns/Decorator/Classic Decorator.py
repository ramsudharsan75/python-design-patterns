from abc import ABC


class Shape(ABC):
    def __str__(self) -> str:
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self) -> str:
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self):
        return f"Square of side {self.side}"


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return f"{self.shape} has the transparency {self.transparency}%"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(shape=circle, color="red")
    print(red_circle)

    red_half_transparent_circle = TransparentShape(shape=red_circle, transparency=50)
    print(red_half_transparent_circle)
