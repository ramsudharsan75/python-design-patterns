from math import cos, sin


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PointFactory:
    @staticmethod  # factory method
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho + sin(theta))


if __name__ == "__main__":
    p = Point(1, 2)
    p2 = PointFactory.new_cartesian_point(2, 3)
    p3 = PointFactory.new_polar_point(30, 45)

    print(p3.x)
