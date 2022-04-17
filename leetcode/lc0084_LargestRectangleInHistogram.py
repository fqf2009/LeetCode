# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle
# in the histogram.

# Constraints:
#   1 <= heights.length <= 10^5
#   0 <= heights[i] <= 10^4
from itertools import chain
from typing import List


# Stack (Monotonic Stack)
#  - stk[]: stack to keep position of bars;
#  - each time encounter a higher bar, push its pos into stack;
#  - each time encounter a shorter bar, one by one pop up higher bar (than
#    current one) from stack;
#  - for each poped up bar, calculate square area, height is limited by poped
#    up bar, width is from popup's left_side_bar_pos, to current_bar_pos - 1;
#  - poped up bars does not need to push back, because future calculation will
#    be limited by this one (shorter);
#  - At the end, simulate a shortest one to calculate area for all bars still
#    in stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = [-1]                                          # pos: left of first bar
        for i, height in enumerate(chain(heights, [0])):    # simulate a shortest bar at end
            while stk[-1] >= 0 and heights[stk[-1]] > height:
                rect_height = heights[stk.pop()]            # popup higher bar at stack
                rect_width = i-1 - stk[-1]                  # peek stack again after popup
                res = max(res, rect_height * rect_width)         
            stk.append(i)

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.largestRectangleArea([4, 2, 0, 3, 2, 5])
        print(r)
        assert r == 6

        r = sol.largestRectangleArea([2, 1, 5, 6, 2, 3])
        print(r)
        assert r == 10

        r = sol.largestRectangleArea([3, 5])
        print(r)
        assert r == 6

        r = sol.largestRectangleArea([2])
        print(r)
        assert r == 2

    unit_test(Solution())
