from typing import List

# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Binary search in sorted array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        p1, p2 = -1, -1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                p1 = mid
                right = mid - 1

        if p1 != -1:
            left, right = p1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    p2 = mid
                    left = mid + 1

        return [p1, p2]


if __name__ == "__main__":
    r = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
    print(r)
    assert(r == [3, 4])

    r = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
    print(r)
    assert(r == [-1, -1])

    r = Solution().searchRange(nums=[], target=0)
    print(r)
    assert(r == [-1, -1])
