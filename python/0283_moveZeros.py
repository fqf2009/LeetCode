# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Follow up: Could you minimize the total number of operations done?
from typing import List

# Exercise again, almost same
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p0, p1, n = 0, 0, len(nums)
        while p0 < n and p1 < n:
            if nums[p0] != 0:
                p0 += 1
                continue
            if p1 <= p0:
                p1 = p0 + 1
                continue
            if nums[p1] == 0:
                p1 += 1
                continue
            nums[p0], nums[p1] = nums[p1], 0
            p0 += 1
            p1 += 1


# Two pointers: O(n)
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        p0, p1, n = 0, 0, len(nums)
        while p0 < n and p1 < n:
            if nums[p0] != 0:
                p0 += 1
                if p1 <= p0:
                    p1 = p0 + 1
                continue
            if nums[p1] != 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p1 += 1
                p0 += 1
            else:
                p1 += 1


if __name__ == '__main__':
    def unitTest(sol):
        nums = [0, 1, 0, 3, 12]
        sol.moveZeroes(nums)
        print(nums)
        assert nums == [1, 3, 12, 0, 0]

        nums = [0]
        sol.moveZeroes(nums)
        print(nums)
        assert nums == [0] 

    unitTest(Solution())
    unitTest(Solution1())
