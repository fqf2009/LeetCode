# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
import bisect
from typing import List

# Binary Search:
# - using bisect.bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


# Binary Search: Template 2
# - like bisect.bisect_left
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            k = (i + j) // 2
            if nums[k] < target:
                i = k + 1
            else:
                j = k

        return i


# Binary Search: Template 1
# Notes:
#  - starts from 0, not -1
#  - if nums[k] == target, we found the pos, i.e., k.
#  - only if nums[k] < target, we know insert pos will be on 
#    the right side of k, i.e. k+1
#  - if nums[k] > target, do not set pos to k-1, because possibly
#    the insert pos is k.
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        res = 0
        while i <= j:
            k = (i + j) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
                res = i
            else:
                j = k - 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.searchInsert(nums=[1, 3], target=2)
        print(r)
        assert(r == 1)

        r = sol.searchInsert(nums=[1, 3], target=5)
        print(r)
        assert(r == 2)

        r = sol.searchInsert(nums=[1, 3, 5, 6], target=0)
        print(r)
        assert(r == 0)

        r = sol.searchInsert(nums=[1, 3, 5, 6], target=5)
        print(r)
        assert(r == 2)

        r = sol.searchInsert(nums=[1, 3, 5, 6], target=2)
        print(r)
        assert(r == 1)

        r = sol.searchInsert(nums=[1, 3, 5, 6], target=7)
        print(r)
        assert(r == 4)

    unitTest(Solution1())
    unitTest(Solution2())
