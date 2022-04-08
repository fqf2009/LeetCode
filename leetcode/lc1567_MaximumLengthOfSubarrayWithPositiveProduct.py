# Given an array of integers nums, find the maximum length of a subarray
# where the product of all its elements is positive.
# A subarray of an array is a consecutive sequence of zero or more values
# taken out of that array.
# Return the maximum length of a subarray with positive product.
# Constraints:
#   1 <= nums.length <= 10^5
#   -109 <= nums[i] <= 10^9
from typing import List
from functools import cache


# Count the numbers: O(n)
# - posLen, negLen: length of current subarray with positive or negtive product
# - iterate over the array:
#   - if value == 0: reset the posLen and negLen to 0.
#   - if value > 0:  increase posLen
#                    increase negLen only if negLen > 0.
#   - if value < 0:  swap posLen and negLen
#                    increase negLen
#                    increase posLen only if posLen > 0
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        posLen = negLen = 0
        for v in nums:
            if v == 0:
                posLen = negLen = 0
            elif v > 0:
                posLen += 1
                negLen = negLen + 1 if negLen > 0 else 0
            else:
                posLen, negLen = negLen, posLen
                negLen += 1
                posLen = posLen + 1 if posLen > 0 else 0

            res = max(res, posLen)
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.getMaxLen([1, -2, -3, 4])
        print(r)
        assert r == 4

        r = sol.getMaxLen([0, 1, -2, -3, -4])
        print(r)
        assert r == 3

        r = sol.getMaxLen([-1, -2, -3, 0, 1])
        print(r)
        assert r == 2


    unitTest(Solution())
