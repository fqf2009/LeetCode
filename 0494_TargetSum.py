# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols
# '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".

# Return the number of different expressions that you can build, which
# evaluates to target.

# Constraints:
#   1 <= nums.length <= 20
#   0 <= nums[i] <= 1000
#   0 <= sum(nums[i]) <= 1000
#   -1000 <= target <= 1000
from typing import List
from functools import cache


# DP + Recursion + Memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(n: int, k: int) -> int:
            if n == 0:
                return 1 if k == 0 else 0
            return dp(n-1, k - nums[n-1]) + dp(n-1, k + nums[n-1])

        return dp(len(nums), target)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
        print(r)
        assert r == 5

        r = sol.findTargetSumWays(nums=[1], target=1)
        print(r)
        assert r == 1

    unitTest(Solution())
