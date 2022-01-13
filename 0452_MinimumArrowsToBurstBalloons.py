# There are some spherical balloons taped onto a flat wall that represents 
# the XY-plane. The balloons are represented as a 2D integer array points 
# where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter 
# stretches between xstart and xend. You do not know exact y-coordinates of balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from 
# different points along the x-axis. A balloon with xstart and xend is burst by an 
# arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows 
# that can be shot. A shot arrow keeps traveling up infinitely, bursting any 
# balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to 
# burst all balloons.

from typing import List, Optional


# time complexity: n*log(n) + n, i.e., O(n*log(n)) 
# greedy algorithm:
#   - first sort balloons' position by end pos
#   - take first balloon's end pos as end line
#   - any balloon with start pos before end line, can be shot together
#   - any balloon with start pos after end line, has to use another arrow
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1]) # sort by end pos
        endLine = points[0][1]
        arrows = 1
        for start, end in points[1:]:
            if start > endLine:
                arrows += 1
                endLine = end
        
        return arrows


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
        print(r)
        assert(r == 2)

        r = sol.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
        print(r)
        assert(r == 4)

        r = sol.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
        print(r)
        assert(r == 2)

    unitTest(Solution())
