# Given an integer array nums, return an array answer such
# that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed
# to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and
# without using the division operation.

# Constraints:
#   2 <= nums.length <= 10^5
#   -30 <= nums[i] <= 30
from itertools import accumulate
from typing import List


# - Scan from left to right, from right to left, doing the
#   cumulative product but shift one item.
# - e.g.                  [1,   2,   3,   4 ]
#   scan --> left_c_prod: [1,   2,   6,   24]
#             left_apply: [1,   1,   2,   6 ]
#           right_c_prod: [24,  24, 12,   4 ] <-- scan
#            right_apply: [24,  12,  4,   1 ]
#  left_apply*left_apply: [24,  12,  8,   6 ]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        cmu_prod = nums[0]
        for i in range(1, n):
            res[i] = cmu_prod
            cmu_prod *= nums[i]

        cmu_prod = nums[n-1]
        for i in reversed(range(n-1)):
            res[i] *= cmu_prod
            cmu_prod *= nums[i]

        return res


# Prefix Product
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = list(accumulate(nums[:-1], lambda x, y: x*y, initial = 1))
        p2 = list(accumulate(reversed(nums[1:]), lambda x, y: x*y, initial = 1))
        return [x*y for x, y in zip(p1, reversed(p2))]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.productExceptSelf([1, 2, 3, 4])
        print(r)
        assert r == [24, 12, 8, 6]

        r = sol.productExceptSelf([-1, 1, 0, -3, 3])
        print(r)
        assert r == [0, 0, 9, 0, 0]

    unitTest(Solution())
    unitTest(Solution1())
