# There are n buildings in a line. You are given an integer array heights of
# size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if
# the building can see the ocean without obstructions. Formally, a building
# has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view,
# sorted in increasing order.

# Constraints:
#   1 <= heights.length <= 10^5
#   1 <= heights[i] <= 10^9
from typing import List


# Monotonic Stack - T/S: O(n)/O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        for i, v in enumerate(heights):
            while stk and heights[stk[-1]] <= v:
                stk.pop()
            stk.append(i)

        return stk


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findBuildings([4, 2, 3, 1])
        print(r)
        assert r == [0, 2, 3]

        r = sol.findBuildings([4, 3, 2, 1])
        print(r)
        assert r == [0, 1, 2, 3]

        r = sol.findBuildings([1, 3, 2, 4])
        print(r)
        assert r == [3]

        r = sol.findBuildings([1])
        print(r)
        assert r == [0]

    unitTest(Solution())
