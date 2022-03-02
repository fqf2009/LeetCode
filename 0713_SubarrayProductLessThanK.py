# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the
# subarray is strictly less than k.
# Constraints:
#   1 <= nums.length <= 3 * 10^4
#   1 <= nums[i] <= 1000
#   0 <= k <= 10^6
from typing import List


# moving window
# Analysis:
# - e.g.: [10, 5, 2, 6, 8], k=100
#     i   j  prod  subarrays ending j      subarrays total
#     0   0  10    1                        1
#     0   1  50    2                        3
#     0   2  100   -                        3
#     1   2  10    2                        5
#     1   3  60    3                        8
#     2   4  96    3                        11
# - keep a prod (cumulative prod of sliding window), as long as
#   prod < k, count all subarrays ending with right pointer.
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        res = 0
        prod = 1
        for j, v in enumerate(nums):
            prod *= v
            while prod >= k:
                prod /= nums[i]
                i += 1
            res += j - i + 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100)
        print(r)
        assert r == 8

        r = sol.numSubarrayProductLessThanK(nums=[10, 5, 2, 6, 8], k=100)
        print(r)
        assert r == 11

        r = sol.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0)
        print(r)
        assert r == 0

    unitTest(Solution())
