# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Constraints:
#   n == height.length
#   2 <= n <= 105
#   0 <= height[i] <= 104
from typing import List, Optional


# Two Pointers
# - The intuition behind this approach is that the area formed between 
#   the lines will always be limited by the height of the shorter line. 
#   Further, the farther the lines, the more will be the area obtained.
# - i, j point to both ends of the array, moving towards center
# - always move the smaller one a step forwad
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        print(r)
        assert r == 49

        r = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 8])
        print(r)
        assert r == 56

        r = sol.maxArea([1, 1])
        print(r)
        assert r == 1

    unitTest(Solution())
