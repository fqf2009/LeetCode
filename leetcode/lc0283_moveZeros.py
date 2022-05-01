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
# Analysis:
# - scan through array, each time find a zero, use another pointer to find next
#   first non-zero to swap with it.
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


# https://leetcode.com/discuss/interview-question/385860/Google-or-Onsite-or-Move-Target-Elements
# - Given an array nums and an int target, write a function to move all 
#   target elements to the beginning of the array while maintaining the 
#   relative order of the non-target elements.
# - Input: nums = [1, 2, 4, 2, 5, 7, 3, 7, 3, 5], target = 5
# - Output: [5, 5, 1, 2, 4, 2, 7, 3, 7, 3]
# Analysis:
# - scan from right to left, each time find the target, use another pointer
#   to search next non-target to swap with.
class Solution2:
    def move_target_to_front(self, nums: List[int], target) -> None:
        p1 = p2 = len(nums) - 1
        while p1 > 0 and p2 >= 0:
            if nums[p1] != target:
                p1 -= 1
            elif p2 >= p1:
                p2 = p1 - 1
            elif nums[p2] == target:
                p2 -= 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 -= 1
                p2 -= 1


# - One step further:
#   input:
#   [1,5,1,3,'a',9,8,'c',4,'b']
#   output:
#   [1,5,1,3,9,8,4,'a','c',b']
# - Analysis
#   - if extra O(n) space is allowed:
#     return [x for x in arr if isinstance(x, int)] + [x for x in arr if isinstance(x, str)]
#   - if extra space is not allowed, and must manipulate array in-place
#     Bubble sort it in O(n^2), but is it possible do it in O(n)?


if __name__ == '__main__':
    def unit_test1(sol):
        nums = [0, 1, 0, 3, 12]
        sol.moveZeroes(nums)
        print(nums)
        assert nums == [1, 3, 12, 0, 0]

        nums = [0]
        sol.moveZeroes(nums)
        print(nums)
        assert nums == [0] 

    def unit_test2(sol):
        nums = [1, 2, 4, 2, 5, 7, 3, 7, 3, 5]
        sol.move_target_to_front(nums, 5)
        print(nums)
        assert nums == [5, 5, 1, 2, 4, 2, 7, 3, 7, 3]


    unit_test1(Solution())
    unit_test1(Solution1())

    unit_test2(Solution2())
