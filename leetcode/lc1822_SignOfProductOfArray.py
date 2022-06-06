# There is a function signFunc(x) that returns:
#   1 if x is positive.
#   -1 if x is negative.
#   0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all
# values in the array nums.
# Return signFunc(product).
# Constraints:
#   1 <= nums.length <= 1000
#   -100 <= nums[i] <= 100
from functools import reduce
from typing import List
from math import prod


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for v in nums:
            if v == 0:
                return 0
            if v < 0:
                res = -res
        return res


class Solution1:
    def arraySign(self, nums: List[int]) -> int:
        return prod(0 if v == 0 else (1 if v > 0 else -1) for v in nums)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.arraySign([-1, -2, -3, -4, 3, 2, 1])
        print(r)
        assert r == 1

        r = sol.arraySign([1, 5, 0, 2, -3])
        print(r)
        assert r == 0

        r = sol.arraySign([-1, 1, -1, 1, -1])
        print(r)
        assert r == -1

    unitTest(Solution())
    unitTest(Solution1())
