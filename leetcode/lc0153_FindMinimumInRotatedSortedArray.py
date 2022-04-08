# Suppose an array of length n sorted in ascending order is rotated between
# 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
# results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the 
# minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# Constraints:
#   n == nums.length
#   1 <= n <= 5000
#   -5000 <= nums[i] <= 5000
#   All the integers of nums are unique.
#   nums is sorted and rotated between 1 and n times.
from typing import List


# Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] <= nums[j]:  # no pivot
                return nums[i]
            k = (i+j) // 2
            if nums[k] > nums[j]:
                i = k + 1
            else:
                j = k   # j = k - 1 is wrong, when nums[k] is the minimum one

        return nums[i]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findMin([3,1,2])
        print(r)
        assert r == 1

        r = sol.findMin([3,4,5,1,2])
        print(r)
        assert r == 1

        r = sol.findMin([4,5,6,7,0,1,2])
        print(r)
        assert r == 0
        
        r = sol.findMin([11,13,15,17])
        print(r)
        assert r == 11
        
        r = sol.findMin([2,3,4,5,1])
        print(r)
        assert r == 1

    unitTest(Solution())
