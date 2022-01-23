# Given an integer array nums, return the number of elements that have both a 
# strictly smaller and a strictly greater element appear in nums.
from typing import List

# Time complexity O(n)
class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxVal = max(nums)
        minVal = min(nums)
        maxCnt = nums.count(maxVal)
        minCnt = nums.count(minVal)
        if len(nums) > maxCnt + minCnt:
            return len(nums) - (maxCnt + minCnt)
        else:
            return 0

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countElements(nums= [11,7,2,15])
        print(r)
        assert(r == 2)

        r = sol.countElements(nums=[5])
        print(r)
        assert(r == 0)

        r = sol.countElements(nums=[5, 6])
        print(r)
        assert(r == 0)

        r = sol.countElements(nums=[-3,3,3,90])
        print(r)
        assert(r == 2)

    unitTest(Solution())
