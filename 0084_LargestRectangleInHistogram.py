from typing import List

# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle 
# in the histogram.

# data structure: Stack
# eabPos[] - stack to keep position of Ever Ascending Bars
#  - each time encounter a higher bar, push its pos into stack;
#  - each time encounter a bar shorter than the one at the top of stack,
#    in turn, pop up every item high than this one, calculate square area
#    from that one until just before this one. Those popup-ed does not need
#    to be pushed back, because future calculation of square area will be
#    limited by this one (shorter).
#  - At the end, simulate a shortest one to calculate all squares of bars in stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def getMaxArea(rightBarPos, rightBarHeight) -> int:
            maxArea = 0
            h = 0
            while len(eabPos) > 0 and heights[eabPos[-1]] > rightBarHeight:
                i = eabPos.pop()
                h = heights[i]
                if len(eabPos) == 0:
                    leftBarPos = -1
                else:
                    leftBarPos = eabPos[-1]
                maxArea = max(maxArea, (rightBarPos - leftBarPos - 1) * h)
            return maxArea

        maxArea = 0
        eabPos = []        
        for i in range(len(heights)):
            if len(eabPos) != 0 and heights[eabPos[-1]] > heights[i]:
                maxArea = max(maxArea, getMaxArea(i, heights[i]))
            eabPos.append(i)

        maxArea = max(maxArea, getMaxArea(len(heights), -1))
        return maxArea


if __name__ == '__main__':
    sol = Solution()

    r = sol.largestRectangleArea([4,2,0,3,2,5])
    print(r)
    assert(r == 6)

    r = sol.largestRectangleArea([2,1,5,6,2,3])
    print(r)
    assert(r == 10)

    r = sol.largestRectangleArea([2,4])
    print(r)
    assert(r == 4)
