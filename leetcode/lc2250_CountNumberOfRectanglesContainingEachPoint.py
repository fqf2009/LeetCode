# You are given a 2D integer array rectangles where rectangles[i] = [li, hi] 
# indicates that ith rectangle has a length of li and a height of hi. You are 
# also given a 2D integer array points where points[j] = [xj, yj] is a point
# with coordinates (xj, yj).

# The ith rectangle has its bottom-left corner point at the coordinates (0, 0) 
# and its top-right corner point at (li, hi).

# Return an integer array count of length points.length where count[j] is the 
# number of rectangles that contain the jth point.

# The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. 
# Note that points that lie on the edges of a rectangle are also considered 
# to be contained by that rectangle.

# Constraints:
#   1 <= rectangles.length, points.length <= 5 * 104
#   rectangles[i].length == points[j].length == 2
#   1 <= li, xj <= 10^9
#   1 <= hi, yj <= 100
#   All the rectangles are unique.
#   All the points are unique.
from bisect import bisect_left
from typing import Counter, List
from sortedcontainers import SortedList


# Binary Search
# T/S: O(R*log(R) + P*log(R)), O(R + P), where:
#      P = len(points), R = len(rectangles)
# Optimize:
# - use SortedList to add items grandually, and reduce sort overhead
class Solution:
    def countRectangles(self, rectangles: List[List[int]], 
                        points: List[List[int]]) -> List[int]:
        res = [0] * len(points)
        rect_width = SortedList()
        counter = Counter(y for _, y in points)
        y0 = 101
        for y in reversed(sorted(counter.keys())):
            for w, h in rectangles:
                if h >= y and h < y0:
                    rect_width.add(w)
            y0 = y
            if len(rect_width) == 0: continue
            for i, (x1, y1) in enumerate(points):
                if y1 != y: continue
                lo = rect_width.bisect_left(x1)
                if lo < len(rect_width):
                    res[i] = len(rect_width) - lo

        return res


# Binary Search
# T/S: O(Y*R*log(R) + P*log(R)), O(R + P), where:
#      Y = unique_y_in_points, P = len(points), R = len(rectangles)
# Analysis:
# - the hi, yj's range indicates we can change this 2-d problem into 1-d problem
# - all the points with same y, can use the same prefix_sum to search
class Solution1:
    def countRectangles(self, rectangles: List[List[int]], 
                        points: List[List[int]]) -> List[int]:
        res = [0] * len(points)
        counter = Counter(y for _, y in points)
        for y in sorted(counter.keys()):    # cost of sort 100 items is very low
            rect_width = [w for w, h in rectangles if h >= y]
            if len(rect_width) == 0:
                break           # benefit of sorted(counter.keys()), otherwise use continue
            rect_width.sort()   # important!

            for i, (x1, y1) in enumerate(points):
                if y1 != y:
                    continue
                lo, hi = 0, len(rect_width)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if rect_width[mid] < x1:    # bisect.bisect_left
                        lo = mid + 1
                    else:
                        hi = mid
                if lo < len(rect_width):
                    res[i] = len(rect_width) - lo

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.countRectangles(
            [[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [5, 9]],
            [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]],
        )
        print(r)
        assert r == [1, 0, 4, 1, 0, 0, 0, 1]

        r = sol.countRectangles([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]])
        print(r)
        assert r == [2, 1]

        r = sol.countRectangles([[1, 1], [2, 2], [3, 3]], [[1, 3], [1, 1]])
        print(r)
        assert r == [1, 3]

    unit_test(Solution())
    unit_test(Solution1())
