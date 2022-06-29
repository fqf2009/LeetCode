# Given a non-empty array nums containing only positive integers, find
# if the array can be partitioned into two subsets such that the sum of
# elements in both subsets is equal.

# Constraints:
#   1 <= nums.length <= 200
#   1 <= nums[i] <= 100
from functools import cache
from typing import List


# DP + Recursion + Memo
# - sum of subsequence equal to half of the sum of array
# - calling dp(n-1, k - nums[n-1]) before calling dp(n-1, k)
#   seems much faster.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(n: int, k: int) -> bool:
            if n == 0 or k <= 0: return k == 0      # k <= 0 !!! critical to prune pathes
            return dp(n-1, k - nums[n-1]) or dp(n-1, k)  # invoking order is more important?

        total = sum(nums)
        if total % 2 != 0: return False
        return dp(len(nums), total // 2)


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i: int, remain: int) -> bool:
            if i == len(nums) or remain <= 0:   # remain <= 0 is critical to prune pathes!!!
                return remain == 0
            return dp(i+1, remain - nums[i]) or dp(i+1, remain)

        target = sum(nums)
        if target % 2 != 0: return False
        return dp(0, target // 2)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.canPartition(nums=[1, 5, 11, 5])
        print(r)
        assert r == True

        r = sol.canPartition(nums=[1, 2, 3, 5])
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
