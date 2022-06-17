# Given an array of distinct integers nums and a target integer target,
# return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
# Example 1:
#   Input: nums = [1,2,3], target = 4
#   Output: 7
#   Explanation:
#   The possible combination ways are:
#   (1, 1, 1, 1)
#   (1, 1, 2)
#   (1, 2, 1)
#   (1, 3)
#   (2, 1, 1)
#   (2, 2)
#   (3, 1)
#   Note that different sequences are counted as different combinations.
# Example 2:
#   Input: nums = [9], target = 3
#   Output: 0
# Constraints:
#   1 <= nums.length <= 200
#   1 <= nums[i] <= 1000
#   All the elements of nums are unique.
#   1 <= target <= 1000
# Follow up: What if negative numbers are allowed in the given array?
#           How does it change the problem? What limitation we need
#           to add to the question to allow negative numbers?
from functools import cache
from typing import List


# DP + Memo (Top-down)
# - T/S: O(T*n), O(T) where T=target
# - assume dp(target) is the combinations to form a target
# - each time pick a number, and then calc dp(remaining), sum it up
# - e.g.: nums = [1,2,3], target = 4
#   pick 1, remain = 3   =>   pick 1, remain = 2, => ... (1, 1)
#                                                        (2)
#                        =>   pick 2, remain = 1  => ... (1)
#                        =>   pick 3 (3)
#   pick 2, remain = 2   =>   ...
#   pick 3, remain = 1   =>   ...
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(remain):
            if remain == 0:
                return 1
            res = 0
            for v in nums:
                if remain - v >= 0:
                    res += dp(remain - v)
            return res

        return dp(target)


# DP + Memo (Bottom-up)
# - T/S: O(T*n), O(T) where T=target
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for total in range(1, target + 1):
            for v in nums:
                if total - v >= 0:
                    dp[total] += dp[total - v]
        return dp[target]


# Backtracking
# - cannot use cache/memo
# - TLE - Time Limit Exceeded
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = list()
        comb = []

        def backtrack(remaining):
            nonlocal res
            if remaining < 0:
                return
            if remaining == 0:
                res.append(comb.copy())
                return
            for i in range(n):
                comb.append(nums[i])
                backtrack(remaining - nums[i])
                comb.pop()

        backtrack(target)
        return len(res)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.combinationSum4([4, 2, 1], target=32)
        print(r)
        assert r == 39882198

        r = sol.combinationSum4([1, 2, 3], target=4)
        print(r)
        assert r == 7

        r = sol.combinationSum4([9], target=3)
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
