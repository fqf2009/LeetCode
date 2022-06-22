# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
# and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance
#  (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique
#  (except for the order that it is in).
# Constraints:
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
from math import sqrt
import random
from typing import List
import heapq


# PriorityQueue or heapq - T/S: O(n*log(k)), O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heapq.heapify(closest)

        for (x, y) in points:
            distance = sqrt(x * x + y * y)
            if len(closest) < k:
                heapq.heappush(closest, (-distance, x, y))
            elif distance < -closest[0][0]:
                heapq.heapreplace(closest, (-distance, x, y))

        return [[x, y] for _, x, y in closest]


# Per Python doc: this is the same as sorted(iterable, key=...)[k]
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))


# Sort - T/S: O(n*log(n)), O(n)
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))[:k]


# Binary Search - T/S: O(n), O(n)
# - O(n + n/2 + n/4 + ... + n/n) => O(2n) => O(n)
class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(sqrt(x * x + y * y), x, y) for x, y in points]
        res = []
        while len(res) < k:
            mid_dist = (max(distance)[0] + min(distance)[0]) / 2
            near, far = [], []
            for dist, x, y in distance:
                if dist <= mid_dist:  # '<=' is Ok, '<' endless loop sometimes
                    near.append((dist, x, y))
                else:
                    far.append((dist, x, y))
            if len(near) <= k - len(res):
                res.extend([[x, y] for _, x, y in near])
                distance = far
            else:
                distance = near

        return res


# Quick Select - T/S: O(n), O(n)
# - O(n + n/2 + n/4 + ... + n/n) => O(2n) => O(n)
class Solution4:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(sqrt(x * x + y * y), x, y) for x, y in points]
        n = len(points)

        # to partition nums[left:right+1) around nums[pvt_idx],
        # and then return new pivot index
        def partition(left, right):
            # randint get random int in [a, b], not [a, b)
            pvt_idx = random.randint(left, right)
            pvt_dist = distance[pvt_idx][0]

            # move pivot to the right end
            distance[pvt_idx], distance[right] = distance[right], distance[pvt_idx]

            # move items smaller than pivot to the left
            pvt_idx = left
            for i in range(left, right):
                if distance[i][0] < pvt_dist:
                    distance[pvt_idx], distance[i] = distance[i], distance[pvt_idx]
                    pvt_idx += 1

            # move pivot back to pvt_idx position
            distance[pvt_idx], distance[right] = distance[right], distance[pvt_idx]

            return pvt_idx

        def select(left, right, k):  # k-th smallest
            if left == right:
                return
            pvt_idx = partition(left, right)
            if k == pvt_idx:
                return
            elif k < pvt_idx:
                return select(left, pvt_idx - 1, k)
            else:
                return select(pvt_idx + 1, right, k)

        select(0, n - 1, k)
        return [[x, y] for _, x, y in distance[:k]]


if __name__ == "__main__":

    def unitTest(solution):
        print()
        print(solution.__name__)
        sol = solution()

        r = sol.kClosest([[0, 1], [1, 0]], 2)
        print(r)
        assert sorted(r) == [[0, 1], [1, 0]]

        r = sol.kClosest([[1, 3], [-2, 2]], 1)
        print(r)
        assert r == [[-2, 2]]

        r = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
        print(r)
        assert sorted(r) == [[-2, 4], [3, 3]]

    unitTest(Solution)
    unitTest(Solution1)
    unitTest(Solution2)
    unitTest(Solution3)
    unitTest(Solution4)
