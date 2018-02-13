import unittest
from csc131.Point import Point


class MyTestCase(unittest.TestCase):
    """
    Unit test suite for the Point class.
    """
    def test_default_initializer(self):
        x, y = 0, 0
        p1 = Point()
        self.assertTrue(p1._x == x and p1._y == y)

    def test_one_param_initializer(self):
        x, y = 2, 0
        p1 = Point(x)
        self.assertTrue(p1._x == x and p1._y == y)

    def test_two_param_initializer(self):
        x, y = 1, 2
        p1 = Point(x, y)
        self.assertTrue(p1._x == x, p1._y == y)

    def test_equality_of_point_with_itself(self):

        point = Point()
        self.assertEqual(point, point)

    def test_equality_of_points_same_coords(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertEqual(p1, p2)

    def test_point_inequality_same_points(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertFalse(p1 != p2)

    def test_point_inequality_different_points(self):
        p1 = Point(1, 2)
        p2 = Point(2, 1)
        self.assertTrue(p1 != p2)

    def test_lhs_point_gt(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertTrue(p2 > p1)

    def test_rhs_point_gt(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertFalse(p1 > p2)

    def test_lhs_point_gte(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertTrue(p2 >= p1)

    def test_rhs_point_gte(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertFalse(p1 >= p2)

    def test_gte_with_equal(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        self.assertTrue(p1 >= p2)

    def test_lhs_point_lt(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertTrue(p1 < p2)

    def test_rhs_point_lt(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertFalse(p2 < p1)

    def test_lhs_point_lte(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertTrue(p1 <= p2)

    def test_rhs_point_lte(self):
        p1 = Point()
        p2 = Point(2, 4)
        self.assertFalse(p2 <= p1)

    def test_lte_with_equal(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        self.assertTrue(p1 <= p2)

    def test_string_conversion(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")

    def test_get_x(self):
        self.assertEqual(Point(1, 3).get_x(), 1)

    def test_get_y(self):
        self.assertEqual(Point(1, 3).get_y(), 3)

    def test_distance_from_east(self):
        self.assertAlmostEqual(Point(3).distance(Point()), 3, places=6)

    def test_distance_from_north(self):
        self.assertAlmostEqual(Point(0, 3).distance(Point()), 3, places=6)

    def test_distance_from_west(self):
        self.assertAlmostEqual(Point(-3, 0).distance(Point()), 3, places=6)

    def test_distance_from_south(self):
        self.assertAlmostEqual(Point(0, -3).distance(Point()), 3, places=6)

    def test_distance_from_north_east(self):
        self.assertAlmostEqual(Point(3, 4).distance(Point()), 5, places=6)

    def test_distance_from_two_non_origin_points(self):
        self.assertAlmostEqual(Point(3, 4).distance(Point(6, 8)), 5, places=6)

    def test_distance_from_origin_east(self):
        self.assertAlmostEqual(Point(3).origin_distance(), 3, places=6)

    def test_distance_from_origin_north(self):
        self.assertAlmostEqual(Point(0, 3).origin_distance(), 3, places=6)

    def test_distance_from_origin_west(self):
        self.assertAlmostEqual(Point(-3).origin_distance(), 3, places=6)

    def test_distance_from_origin_south(self):
        self.assertAlmostEqual(Point(0, -3).origin_distance(), 3, places=6)

    def test_distance_from_origin_north_west(self):
        self.assertAlmostEqual(Point(-4, 3).origin_distance(), 5, places=6)


if __name__ == '__main__':
    unittest.main()
