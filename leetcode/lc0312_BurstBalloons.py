# You are given n balloons, indexed from 0 to n - 1. Each balloon is
# painted with a number on it represented by an array nums. You are
# asked to burst all the balloons.
# If you burst the ith balloon, you will get:
#   nums[i - 1] * nums[i] * nums[i + 1] coins.
# If i - 1 or i + 1 goes out of bounds of the array, then treat it as if
# there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.
# Example 1:
#   Input: nums = [3,1,5,8]
#   Output: 167
#   Explanation:
#   nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#   coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Constraints:
#   n == nums.length
#   1 <= n <= 300
#   0 <= nums[i] <= 100
from functools import cache
from typing import List, Tuple


# Naive DP (Recursion + Memo): O(n*2^n)
# - result is correct, but TLE - Time Limit Exceeded
# - one-by-one burst each balloons, and choose max value
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(nums: Tuple[int]) -> int:
            res = 0
            for i, v in enumerate(nums):
                v1 = nums[i - 1] if i > 0 else 1
                v2 = nums[i + 1] if i + 1 < len(nums) else 1
                res = max(res, v1 * v * v2 + dp(nums[:i] + nums[i + 1 :]))
            return res

        return dp(tuple(nums))


# DP (Recursion + Memo) - T/S: O(n^3), O(n^2), 
# - due to memo, there is n^2 states, each state iterate max n times
# Ref: https://en.wikipedia.org/wiki/Matrix_chain_multiplication
# Analysis
# - assume dp(l, r) is max coins collected for bursting nums[l:r], r is inclusive.
# - one-by-one choose the LAST burst balloon i, dp transition formula:
#   dp(l, r) = max(dp(l, i-1) + dp(i+1, r) + nums[l-1]*nums[i]*nums[r+1]), for i in [l, r]
# - note the: nums[l-1]*nums[i]*nums[r+1], why nums[l-1], nums[r+1] can be used?
#   because we always choose balloon to burst last, when the nums[l:r] is used
#   to calculate dp, its surroundings are not burst yet.
class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(l, r) -> int:
            if l > r:
                return 0
            v1 = nums[l - 1] if l > 0 else 1
            v2 = nums[r + 1] if r + 1 < len(nums) else 1
            res = 0
            for i in range(l, r + 1):
                res = max(res, dp(l, i - 1) + dp(i + 1, r) + v1 * v2 * nums[i])
            return res

        return dp(0, len(nums) - 1)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.maxCoins([8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2])
        print(r)
        assert r == 3394

        r = sol.maxCoins([3, 1, 5, 8])
        print(r)
        assert r == 167

        r = sol.maxCoins([1, 5])
        print(r)
        assert r == 10

    # unitTest(Solution())
    unitTest(Solution1())
