# Given a non-empty array of integers nums, every element 
# appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime 
# complexity and use only constant extra space.
# Constraints:
#   1 <= nums.length <= 3 * 104
#   -3 * 104 <= nums[i] <= 3 * 104
#   Each element in the array appears twice except 
#   for one element which appears only once.
from typing import List


# Bit Manipulation
# - x ^ 0 -> x
# - x ^ x -> 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for v in nums:
            res ^= v
        return res


# Set + Math
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


# Set
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        n2 = set()
        for v in nums:
            if v in n2:
                n2.remove(v)
            else:
                n2.add(v)
        return list(n2)[0]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.singleNumber([2,2,1])
        print(r)
        assert r == 1

        r = sol.singleNumber([4,1,2,1,2])
        print(r)
        assert r == 4

        r = sol.singleNumber([1])
        print(r)
        assert r == 1

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
