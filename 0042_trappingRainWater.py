from typing import List

# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining.

# DP (Dynamic Programing): O(n)
# dpLeft[i] : by far the highest wall to the left
# dpRight[i]: by far the highest wall to the right
class Solution:
    def trap(self, height: List[int]) -> int:
        dpLeft, dpRight = [0] * len(height), [0] * len(height)
        dp0 = 0
        for i in range(len(height)):
            dpLeft[i] = max(dp0, height[i])
            dp0 = dpLeft[i]

        dp0 = 0
        for i in reversed(range(len(height))):
            dpRight[i] = max(dp0, height[i])
            dp0 = dpRight[i]

        res = 0
        for i in range(1, len(height) - 1):
            water = min(dpLeft[i], dpRight[i]) - height[i]
            if water > 0:
                res += water

        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6
    r = Solution().trap(height)
    print(r)
    assert(r == expected)

    height = [4, 2, 0, 3, 2, 5]
    expected = 9
    r = Solution().trap(height)
    print(r)
    assert(r == expected)
