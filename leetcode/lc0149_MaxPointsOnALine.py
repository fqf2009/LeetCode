# Given an array of points where points[i] = [xi, yi] represents
# a point on the X-Y plane, return the maximum number of points
# that lie on the same straight line.
# Constraints:
#   1 <= points.length <= 300
#   points[i].length == 2
#   -10^4 <= xi, yi <= 10^4
#   All the points are unique.
from typing import List
from math import gcd
from collections import defaultdict


# Math - T/S: O(n^2), O(n)
# - if two lines pass through a same point, and both lines
#   have the same slope (dy/dx), then they are the same line.
# - however slope are double, and is inaccurate in comparison,
#   therefore, use co-prime of (dy, dx) instead.
# - algorithm:
#   - iterate over each point, for this point P[i],
#   - iterate over remaining points P[i+1], ..., P[n-1]
#   - calculate slope between two points,
#   - count max duplicate slopes, and then plus 1, this is the
#     max points in the same line pass throught this point[i].
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getSlope(p1: List[int], p2: List[int]):
            (x1, y1), (x2, y2) = p1, p2
            if x1 == x2: return (0, 1)
            if y1 == y2: return (1, 0)
            dx, dy = x1 - x2, y1 - y2
            divisor = gcd(dx, dy)
            dx /= divisor
            dy /= divisor
            if dx < 0:
                dx, dy = -dx, -dy
            return (dx, dy)

        n = len(points)
        res = 1
        for i, p1 in enumerate(points[:n-1]):
            slopes = defaultdict(int)
            for p2 in points[i+1:]:
                slopes[getSlope(p1, p2)] += 1
            res = max(res, max(slopes.values()) + 1)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxPoints([[0, 0]])
        print(r)
        assert r == 1

        r = sol.maxPoints([[0, 1], [0, 0]])
        print(r)
        assert r == 2

        r = sol.maxPoints([[1, 1], [2, 2], [3, 3]])
        print(r)
        assert r == 3

        r = sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
        print(r)
        assert r == 4

    unitTest(Solution())
