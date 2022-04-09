# Suppose an array of length n sorted in ascending order is rotated between
# 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#   [4,5,6,7,0,1,4] if it was rotated 4 times.
#   [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
# results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums that may contain duplicates, return 
# the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
# Constraints:
#   n == nums.length
#   1 <= n <= 5000
#   -5000 <= nums[i] <= 5000
#   nums is sorted and rotated between 1 and n times.
from typing import List


# Binary Search (Template 2)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(lo, hi):
            if lo == hi:                # exit condition
                return nums[lo]

            mid = (lo+hi) // 2

            if lo == mid:               # only two items remaining
                return min(nums[lo], nums[hi])
            if nums[lo] < nums[hi]:     # no pivot any more
                return nums[lo]
            if nums[lo] < nums[mid]:    # no pivot at left side
                return find(mid+1, hi)

            return min(find(lo, mid), find(mid+1, hi))  # both sides and mid could be smallest
            
        return find(0, len(nums) - 1)


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,),])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,3,5], 1),
            ([2,2,2,-1,1], -1),
            ([4,5,6,7,0,1,4], 0),
            ([2,3,4,4,5,7,7], 2),
            ([10], 10),
        ])
        def test_findMin(self, nums, expected):
            sol = self.solution()       # type:ignore
            r = sol.findMin(nums)
            self.assertEqual(r, expected)

    main()
