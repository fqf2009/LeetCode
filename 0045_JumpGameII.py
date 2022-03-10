# Given an array of non-negative integers nums, you are initially 
# positioned at the first index of the array.
# Each element in the array represents your maximum jump length 
# at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.
# Constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
from typing import List


# DP + Iteration - T/S: O(n), O(n)
# - dp[i] - in i steps, how far can I reach
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        currStep = -1
        currDistance = -1
        nextDistance = 0
        for i, v in enumerate(nums):
            if i > currDistance and i <= nextDistance:
                currStep += 1
                currDistance = nextDistance
            elif i > nextDistance:
                break
            nextDistance = max(nextDistance, i + v)
            if nextDistance >= n - 1:
                return currStep + 1

        return -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.jump(nums=[2, 3, 1, 1, 4])
        print(r)
        assert r == 2

        r = sol.jump(nums=[2, 3, 0, 1, 4])
        print(r)
        assert r == 2


        r = sol.jump(nums=[2])
        print(r)
        assert r == 0

        r = sol.jump(nums=[2, 3])
        print(r)
        assert r == 1


    unitTest(Solution())
