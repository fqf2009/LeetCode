# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
# Constraints:
#   n == nums.length
#   1 <= n <= 10^4
#   0 <= nums[i] <= n
#   All the numbers of nums are unique.
from typing import List


# Math - sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


# Math - xor
# - note: a ^ b ^ b => a; a ^ b ^ a => b
# - res = 0 ^ 1 ^ 2 ^ ... ^ n ^ nums[0] ^ ... ^ nums[n-1]
#   then res will be the number which only appear one time
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i ^ v  # xor
        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.missingNumber([3, 0, 1])
        print(r)
        assert r == 2

        r = sol.missingNumber([0, 1])
        print(r)
        assert r == 2

        r = sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        print(r)
        assert r == 8

    unitTest(Solution())
    unitTest(Solution1())
