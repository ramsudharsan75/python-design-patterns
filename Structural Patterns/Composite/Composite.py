# A mechanism to treat both individual and composite objects in an uniform manner.


class GraphicObject:
    def __init__(self, colour=None) -> None:
        self.colour = colour
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        pass


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = "drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Square("Yellow"))

    group = GraphicObject()
    group.children.append(Square("Blue"))
    group.children.append(Circle("Blue"))

    drawing.children.append(
        group
    )  # recursively adding graphic objects since a group of graphic objects is still a graphic object
    print(drawing)
