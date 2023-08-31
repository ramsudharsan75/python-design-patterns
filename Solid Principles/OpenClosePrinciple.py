"""Open for extension, Closed for modification."""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:  # poor implementation -> doesn't follow Open-Close principle
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# Specification Pattern


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(
    Specification
):  # combinator for combining multiple specifications
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green products (old): ")

    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    bf = BetterFilter()

    print("Green products (new): ")
    green = ColorSpecification(Color.GREEN)

    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products: ")
    large = SizeSpecification(Size.LARGE)

    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large Blue items: ")
    blue = ColorSpecification(Color.BLUE)
    # large_blue = AndSpecification(large, blue)
    large_blue = large and blue

    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
