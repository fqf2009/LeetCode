# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown
# pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return
# the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
#   1 <= nums.length <= 5000
#   -10^4 <= nums[i] <= 10^4
#   All values of nums are unique.
#   nums is an ascending array that is possibly rotated.
#   -10^4 <= target <= 10^4
from typing import List


# iteration: O(log(n))
# Analysis
# - if there is a pivot, then nums[right] < nums[left]
# - if nums[left] < nums[mid] (and left != mid), then if there is pivot, 
#   it is at right side;
#   else (i.e. nums[left] > nums[mid]) pivot is already at left side, so that
#   nums[mid] < nums[right].
# - So the algorithm is:
#   a. find middle point, check if middle value is target, return if found;
#   b. make sure left point is not the middle point, increase left by 1 if true;
#   c. if nums[left] < nums[mid], piviot is at right side, then check whether
#      target is inside left side of values, to determine next direction;
#   d. else piviot is already at left side, then check whether target is inside
#      right side of values, to determine next direction.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if left == mid:
                left = mid + 1
            elif nums[left] < nums[mid]:    # if there is pivot, it is at right side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # now pivot is at left side, so that nums[mid] < nums[right]
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Recusrsion: O(log(n))
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def searchPartial(left: int, right: int) -> int:
            if left > right:
                return -1
            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    return searchPartial(left, mid - 1)
                else:
                    return searchPartial(mid + 1, right)
            else:  # now nums[mid] < nums[right]
                if nums[mid] < target and target <= nums[right]:
                    return searchPartial(mid + 1, right)
                else:
                    return searchPartial(left, mid - 1)

        return searchPartial(0, len(nums) - 1)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
        print(r)
        assert(r == 4)

        r = Solution().search(nums=[1, 2, 4, 5, 6, 7, 0], target=0)
        print(r)
        assert(r == 6)

        r = sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
        print(r)
        assert(r == -1)

        r = sol.search(nums=[1], target=0)
        print(r)
        assert(r == -1)

        r = sol.search(nums=[3, 1], target=1)
        print(r)
        assert(r == 1)

    unitTest(Solution())
    unitTest(Solution1())
