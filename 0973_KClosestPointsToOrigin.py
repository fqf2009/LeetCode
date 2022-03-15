# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Constraints:
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
from math import sqrt
from typing import List
import heapq


# PriorityQueue or heapq - T/S: O(n*log(k)), O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x, y in points[:k]:
            closest.append((-sqrt(x*x + y*y), x, y))

        heapq.heapify(closest)
        for (x, y) in points[k:]:
            heapq.heappush(closest, (-sqrt(x*x + y*y), x, y))
            heapq.heappop(closest)

        return [[x, y] for _, x, y in closest]


# Per Python doc: this is the same as sorted(iterable, key=...)[k]
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: sqrt(p[0]**2 + p[1]**2))


# Sort - T/S: O(n*log(n)), O(n)
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: sqrt(p[0]**2 + p[1]**2))[:k]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.kClosest([[1, 3], [-2, 2]], 1)
        print(r)
        assert r == [[-2, 2]]

        r = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
        print(r)
        assert sorted(r) == [[-2, 4], [3, 3]]


    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
