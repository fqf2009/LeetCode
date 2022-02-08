# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this
# place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have a security
# system connected, and it will automatically contact the police if two
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each
# house, return the maximum amount of money you can rob tonight without
# alerting the police.
from typing import List

# DP + Iteration - T/S: O(n), O(1)
# dp[i] = max value at position i
# dp[i] only rely on dp[i-1] and dp[i-2]
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robNoCircle(nums: List[int]) -> int:
            dp2 = dp1 = dp0 = nums[0]
            if len(nums) > 1:
                dp2 = dp1 = max(nums[:2])
            for i in range(2, len(nums)):
                dp2 = max(dp1, dp0 + nums[i])
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

    unitTest(Solution())
