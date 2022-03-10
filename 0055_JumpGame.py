# You are given an integer array nums. You are initially positioned
# at the array's first index, and each element in the array represents
# your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# Constraints:
#   0 <= nums[i] <= 10^5
from typing import List


# DP + Iteration - T/S: O(n), O(1)
# - dp - during iteration, by far the furthest place can jump to
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = 0
        for i, v in enumerate(nums):
            if dp < i: return False
            dp = max(dp, i + v)
            if dp >= n - 1: return True

        return False


# DP + Iteration - T/S: O(n*V), O(n), where V = avg(nums)
# - Time Limit Exceeded
# - the code below calculate how many pathes to each node,
#   really unnecessary.
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i, v in enumerate(nums):
            if dp[i] > 0:
                for j in range(1, v+1):
                    if i + j < n:
                        dp[i + j] += 1

        return dp[n-1] > 0


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.canJump(nums=[2, 3, 1, 1, 4])
        print(r)
        assert r == True

        r = sol.canJump(nums=[3, 2, 1, 0, 4])
        print(r)
        assert r == False

        r = sol.canJump(nums=[0])
        print(r)
        assert r == True

        r = sol.canJump(nums=[0, 2, 3])
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
