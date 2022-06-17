# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security systems connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each
# house, return the maximum amount of money you can rob tonight without
# alerting the police.
from typing import List
from functools import cache

# DP + Memo + Recursion
class Solution0:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            return max(dp(i - 1), dp(i - 2) + nums[i])

        return dp(len(nums) - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dp(i + 2), dp(i + 1))

        return dp(0)


# DP + Memo + Iteration - T/S: O(n), O(1)
# dp[i] = max value at position i
# dp[i] only rely on dp[i-1] and dp[i-2]
class Solution1:
    def rob(self, nums: List[int]) -> int:
        dp2 = dp1 = dp0 = nums[0]
        if len(nums) > 1:
            dp2 = dp1 = max(nums[:2])
        for i in range(2, len(nums)):
            dp2 = max(dp1, dp0 + nums[i])
            dp1, dp0 = dp2, dp1

        return dp2


# DP + Memo + Iteration - T/S: O(n), O(n), space can be optimized to O(1)
# much easier to understand, and 100% correct.
# dp[i] = max value at position i
class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


# DP + Memo + Iteration - T/S: O(n), O(n), space can be optimized to O(1)
# This state transition equation is really hard to understand.
# Not sure whether this is 100% correct.
# dp[i] = max value when nums[i] has to be taken.
class Solution3:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = nums[1]
        if len(nums) > 2:
            dp[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]

        return max(dp)  # this is difference


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.rob(nums=[3, 2])
        print(r)
        assert r == 3

        r = sol.rob(nums=[1, 2, 3, 1])
        print(r)
        assert r == 4

        r = sol.rob(nums=[2, 7, 9, 3, 1])
        print(r)
        assert r == 12

        r = sol.rob(nums=[2, 17, 9, 3, 1])
        print(r)
        assert r == 20

        r = sol.rob(nums=[2, 17, 9, 3, 15, 5])
        print(r)
        assert r == 32

    unitTest(Solution())
    unitTest(Solution0())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
