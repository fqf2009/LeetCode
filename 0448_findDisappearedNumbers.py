# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all integers in range [1, n] that do not appear in nums.
# Follow up: Could you do it without extra space and in O(n) runtime? You may 
# assume the returned list does not count as extra space.
from typing import List


# keep moving item, and save it to (val-1) position, and save as -val.
# No way to restore nums's original state
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            v = nums[i]
            while v > 0:
                v1 = nums[v-1]
                nums[v-1] = -v
                v = v1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Memo: in-place marking, i.e., set nums[i] to negative to indicate (i+1) exists
# This one is better, if there is requirement to restore nums's original state
class Solution1:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            v = nums[i]
            if v < 0:
                v = -v
            if nums[v - 1] > 0:
                nums[v - 1] = -nums[v - 1]

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    def unitTest(sol):
        r = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        print(r)
        assert r == [5, 6]

        r = Solution().findDisappearedNumbers([1, 1])
        print(r)
        assert r == [2]

    unitTest(Solution())
    unitTest(Solution1())
