"""
Lab 4: Introduction to Classes with a Point Class
CSC131, Spring 2108
Missouri State University
Author: Alyssa Slayton <ajs41@missouristate.edu>
"""
from math import sqrt


class Point:
    """
    A class that represents a point in a two-dimensional coordinate system.
    """

    # TODO: Implement this class as per the class diagram found in the README
    def __init__(self, x_coord: float = 0, y_coord: float = 0):
        self._x = x_coord
        self._y = y_coord
    def __eq__(self,other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    def __ne__(self,other):
        return not self.__eq__(other)

    def __lt__(self,other):
        if not isinstance(other, Point):
            return False
        return self.origin_distance() < other.origin_distance()

    def __le__(self,other):
        if not isinstance(other, Point):
            return False
        return self.origin_distance() < other.origin_distance() or self.origin_distance() == other.origin_distance

    def __gt__(self,other):
        if not isinstance(other, Point):
            return False
        return self.origin_distance() > other.origin_distance()

    def __ge__(self,other):
        if not isinstance(other, Point):
            return False
        return self.origin_distance() > other.origin_distance() or self.origin_distance() == other.origin_distance()

    def distance(self, other) -> float:
        if not isinstance(other, Point):
            raise TypeError
        return sqrt( (other._x - self._x)**2 + (other._y - self._y)**2)

    def origin_distance(self):
        return self.distance(Point())

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        thisisstupid = {}
        return "({}, {})".format(self._x,self._y)


def main():
    print("Main")
    p0 = Point()
    p1 = Point(3, 4)
    p2 = Point(3)
    print("p0 =", p0)
    print("p1 =", p1)
    print("p2 =", p2)
    print("p0 == p1 evaluates to:", p0 == p1)
    print("p0 == p0 evaluates to:", p0 == p0)
    print("p0 != p1 evaluates to:", p0 != p1)
    print("p0 != p0 evaluates to:", p0 != p0)
    print("p1 == p1 evaluates to:", p1 == p1)
    print("p2 >  p1 evaluates to:", p2 > p1)
    print("p2 >= p1 evaluates to:", p2 >= p1)
    print("p2 >= p2 evaluates to:", p2 >= p2)
    print("p2 <  p2 evaluates to:", p2 < p2)
    print("p2 <  p1 evaluates to:", p2 < p1)
    print("p2 <= p1 evaluates to:", p2 <= p1)
    print("p1 == \"Hello\" is:     ", p1 == "abc")
    print("p1 != \"Hello\" is:     ", p1 != "abc")


if __name__ == '__main__':
    main()
