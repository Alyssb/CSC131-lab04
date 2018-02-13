"""
Lab 4: Introduction to Classes with a Point Class
CSC131, Spring 2108
Missouri State University
Author: TODO: Replace this with your name in the form: Your Name <email@live.missouristate.edu>
"""


class Point:
    """
    A class that represents a point in a two-dimensional coordinate system.
    """
    # TODO: Implement this class as per the class diagram found in the README


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
