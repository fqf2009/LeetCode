# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining.

from typing import List


# DP (Dynamic Programing): O(n)
# dpLeft[i] : by far the highest wall to the left
# dpRight[i]: by far the highest wall to the right
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        dpLeft, dpRight = [height[0]] * n, [height[-1]] * n
        for i in range(1, n-1):
            dpLeft[i] = max(dpLeft[i-1], height[i])
            dpRight[n-1-i] = max(dpRight[n-i], height[n-1-i])

        res = 0
        for i in range(1, n - 1):
            res += max(min(dpLeft[i], dpRight[i]) - height[i], 0)

        return res


if __name__ == "__main__":
    def unit_test(sol):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        r = Solution().trap(height)
        print(r)
        assert r == expected

        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        r = Solution().trap(height)
        print(r)
        assert r == expected

    unit_test(Solution())
