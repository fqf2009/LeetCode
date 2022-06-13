# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.
# Constraints:
#   1 <= nums.length <= 2 * 10^4
#   -10 <= nums[i] <= 10
#   The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
from typing import List


# DP - O(n)
# - always keep max and min among (v, v * prov_max, v * prev_min)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max0 = min0 = res = nums[0]
        for v in nums[1:]:
            max1 = max(v, max0*v, min0*v)            
            min1 = min(v, max0*v, min0*v)
            res = max(res, max1)
            max0, min0 = max1, min1
        
        return res


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [0] * len(nums)
        dpMin = [0] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        mp = nums[0]
        for i in range(1, len(nums)):
            dpMax[i] = max(nums[i], dpMax[i-1] * nums[i], dpMin[i-1] * nums[i])
            dpMin[i] = min(nums[i], dpMax[i-1] * nums[i], dpMin[i-1] * nums[i])
            mp = max(mp, dpMax[i])

        return mp


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3])
        print(r)
        assert r == 120

        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3, 2])
        print(r)
        assert r == 180

        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3, -2])
        print(r)
        assert r == 720

        r = sol.maxProduct([2,3,-2,4])
        print(r)
        assert r == 6

        r = sol.maxProduct([-2,0,-1])
        print(r)
        assert r == 0

    unitTest(Solution())
