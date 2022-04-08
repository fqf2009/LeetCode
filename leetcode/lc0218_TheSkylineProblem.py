# A city's skyline is the outer contour of the silhouette formed by all
# the buildings in that city when viewed from a distance. Given the
# locations and heights of all the buildings, return the skyline formed
# by these buildings collectively.

# The geometric information of each building is given in the array
# buildings where buildings[i] = [lefti, righti, heighti]:
#  - lefti is the x coordinate of the left edge of the ith building.
#  - righti is the x coordinate of the right edge of the ith building.
#  - heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an
# absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted
# by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key
# point is the left endpoint of some horizontal segment in the skyline
# except the last point in the list, which always has a y-coordinate
# 0 and is used to mark the skyline's termination where the rightmost
# building ends. Any ground between the leftmost and rightmost buildings
# should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the
# output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...]
# is not acceptable; the three lines of height 5 should be merged into one
# in the final output as such: [...,[2 3],[4 5],[12 7],...]

# Constraints:
#   1 <= buildings.length <= 10^4
#   0 <= lefti < righti <= 231 - 1
#   1 <= heighti <= 231 - 1
#   buildings is sorted by lefti in non-decreasing order.
from typing import List
import heapq

# PriorityQueue: O(n*log(n))
# - iterate through buildings, while always keep them sorted on x coordinate
# - assume current building is (left1, right1, height1)
# - get next building (left2, right2, height2)
# - if left2 < right1, i.e. two buildings have some overlaps:
#   - if height2 > height1, the draw skyline (if l2 != l1) using (left1, height1),
#     and put the uncovered right part of building 1 (only if right1 > right2)
#     back into queue. now the current building is building 2.
#   - if height2 < height1, put the uncovered right part of building 2
#     (only if right2 > right1) back into queue.
#     now the current building is still building 1.
#   - else (same height) extend the building 1 with building 2
# - if left2 == right1, i.e. no overlaps
#   - if h2 != h1, draw skyline using (left1, height1), then set current
#     building to building 2
#   - else extend the building 1 with building 2
# - else (left2 > right1, i.e. this is some gap), draw skyline using
#   (left1, height1) and (right1, 0), set current building to building 2
# - !!! any time drawing a skying, it is possible to have height as previous
#       one, so must avoid the duplication !!!
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def addSkyLine(sl, x, y):
            if len(sl) == 0 or sl[-1][1] != y:
                sl.append([x, y])

        heapq.heapify(buildings)
        l1, r1, h1 = heapq.heappop(buildings)
        res = []
        while buildings:
            l2, r2, h2 = heapq.heappop(buildings)
            if l2 < r1:  # with overlap
                if h2 > h1:
                    if l2 > l1:  # left part of building 1 not covered by building 2
                        addSkyLine(res, l1, h1)
                    if r1 > r2:  # right part of building 1 not covered by building 2
                        heapq.heappush(buildings, [r2, r1, h1])
                    l1, r1, h1 = l2, r2, h2
                elif h2 < h1:
                    if r1 < r2:  # right part of building 2 not covered by building 1
                        heapq.heappush(buildings, [r1, r2, h2])
                else:           # same height, extend building
                    r1 = r2
            elif l2 == r1:      # no overlap, no gap
                if h2 != h1:    # different height, draw skyline
                    addSkyLine(res, l1, h1)
                    l1, r1, h1 = l2, r2, h2
                else:           # same height, extend building
                    r1 = r2
            else:               # no overlap, with gap
                addSkyLine(res, l1, h1)
                addSkyLine(res, r1, 0)
                l1, r1, h1 = l2, r2, h2

        addSkyLine(res, l1, h1)
        addSkyLine(res, r1, 0)
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]])
        print(r)
        assert r == [[1, 3], [3, 0]]

        r = sol.getSkyline([[2, 14, 4], [4, 8, 8], [6, 16, 4]])
        print(r)
        assert r == [[2, 4], [4, 8], [8, 4], [16, 0]]

        r = sol.getSkyline([[0, 2, 3], [2, 5, 3]])
        print(r)
        assert r == [[0, 3], [5, 0]]

        r = sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
        print(r)
        assert r == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

    unitTest(Solution())
