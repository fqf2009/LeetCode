# Given an array of integers nums containing n + 1 integers where each 
# integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses 
# only constant extra space.
# Constraints:
#   1 <= n <= 10^5
#   nums.length == n + 1
#   1 <= nums[i] <= n
#   All the integers in nums appear only once except for precisely one
#       integer which appears two or more times.
# Follow up:
#   How can we prove that at least one duplicate number must exist in nums?
#   Can you solve the problem in linear runtime complexity?
from typing import List


# negative marking: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = -1
        for v in nums:
            pos = abs(v)
            if nums[pos] < 0:
                res = pos
                break
            nums[pos] = -nums[pos]
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return res


# Swap each num into position by its value
# Note: nums will be modified!
#       if using recursion, then need O(n) space in stack (which will overflow)
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


# Binary Search, no need to sort: T/S: O(n*log(n)), O(1)
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums)
        while lo < hi:
            mid = (lo+hi) // 2
            cnt = sum(v <= mid for v in nums)
            if cnt <= mid:
                lo = mid + 1
            else:
                hi = mid

        return lo


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([2,2,2,2,2], 2),
            ([1,3,4,2,2], 2),
            ([3,1,3,4,2], 3),
        ])
        def test_findDuplicate(self, nums, expected):
            sol = self.solution()       # type:ignore
            nums2 = nums.copy()
            r = sol.findDuplicate(nums)
            self.assertEqual(r, expected)
            self.assertEqual(nums2, nums)

    main()
