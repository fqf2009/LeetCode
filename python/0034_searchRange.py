# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


# Binary search in sorted array
# - Simplify the code, reduce redundancy or duplicate
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left, right, leftEdge: bool = True) -> int:
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    res = mid
                    if leftEdge:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res

        n = len(nums)
        p1 = binarySearch(0, n - 1)
        p2 = binarySearch(p1, n - 1, False) if p1 != -1 else -1
        return [p1, p2]


# Binary search in sorted array
class Solution1:
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
                p2 = max(p1, p2)    # p2 set to the largest pos ever found
                right = mid - 1

        if p2 != -1:
            left, right = p2 + 1, len(nums) - 1
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
    def unitTest(sol):
        r = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
        print(r)
        assert(r == [3, 4])

        r = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
        print(r)
        assert(r == [-1, -1])

        r = sol.searchRange(nums=[], target=0)
        print(r)
        assert(r == [-1, -1])

    unitTest(Solution())
    unitTest(Solution1())
