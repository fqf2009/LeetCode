# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
# numsr-1, numsr] of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
# Constraints:
#   1 <= target <= 10^9
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^5
from typing import List

# moving window (sliding window)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        res = 10**9
        csum = 0
        for j, v in enumerate(nums):
            csum += v
            while csum >= target:
                res = min(res, j - i + 1)
                if res == 1: return 1
                csum -= nums[i]
                i += 1

        return 0 if res == 10**9 else res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
        print(r)
        assert r == 2

        r = sol.minSubArrayLen(target=4, nums=[1, 4, 4])
        print(r)
        assert r == 1

        r = sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
        print(r)
        assert r == 0

    unitTest(Solution())
