# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this
# place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have a security
# system connected, and it will automatically contact the police if two
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each
# house, return the maximum amount of money you can rob tonight without
# alerting the police.

# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 1000
from typing import List
from functools import cache


class Solution0:
    def rob(self, nums: List[int]) -> int:
        def robNoCircle(N: List[int]) -> int:
            @cache
            def dp(i):
                if i >= len(N): return 0
                return max(N[i] + dp(i+2), dp(i+1))
            
            return dp(0)
        
        if len(nums) == 1: return nums[0]
        return max(robNoCircle(nums[1:]), robNoCircle(nums[:-1]))


# DP + Recursion - T/S: O(n), O(n)
# dp[i] = max value at position i
# dp[i] only rely on dp[i-1] and dp[i-2]
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robNoCircle(N: List[int]) -> int:
            @cache
            def dp(i):
                if i < 0: return 0
                return max(dp(i-1), dp(i-2) + N[i])

            return dp(len(N) - 1)

        if len(nums) == 1:
            return nums[0]
        return max(robNoCircle(nums[1:]), robNoCircle(nums[:-1]))


# DP + Iteration - T/S: O(n), O(1)
# dp[i] = max value at position i
# dp[i] only rely on dp[i-1] and dp[i-2]
class Solution1:
    def rob(self, nums: List[int]) -> int:
        def robNoCircle(N: List[int]) -> int:
            dp2 = dp1 = dp0 = N[0]
            if len(N) > 1:
                dp2 = dp1 = max(N[:2])
            for i in range(2, len(N)):
                dp2 = max(dp1, dp0 + N[i])
                dp1, dp0 = dp2, dp1
            return dp2

        if len(nums) == 1:
            return nums[0]
        return max(robNoCircle(nums[1:]), robNoCircle(nums[:-1]))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.rob(nums=[2])
        print(r)
        assert r == 2

        r = sol.rob(nums=[2, 3, 2])
        print(r)
        assert r == 3

        r = sol.rob(nums=[1, 2, 3, 1])
        print(r)
        assert r == 4

        r = sol.rob(nums=[5, 10, 9, 8, 5])
        print(r)
        assert r == 18

    unitTest(Solution0())
    unitTest(Solution())
    unitTest(Solution1())
