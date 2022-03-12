# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
# Constraints:
#   1 <= nums.length <= 5 * 10^5
from typing import List


# O(n) means no sort.
# So it has to store the scan result in place:
# - assume len(nums) == n, so it can hold n pos int at most,
#   and the minium pos int will be less than or equal to n + 1.
# - therefore, all zero, negative or greater than n + 1 values
#   can be ignored.
# - scan the array, if the value (nums[i]) is between 1 and n (1 <= val <= n),
#   save it in place as nums[val-1] (note nums is zero indexed)
# - scan the array the second time, found the first position,
#   where nums[i] != i + 1, return i + 1
# - if not found, return n+1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, v in enumerate(nums):
            j = i
            while 1 <= v <= n and v != j + 1:
                j, v1 = v-1, nums[v-1]
                nums[j] = v
                v = v1

        return next((i + 1 for i, v in enumerate(nums) if v != i + 1), n + 1)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.firstMissingPositive(nums=[2, 1])
        print(r)
        assert r == 3

        r = sol.firstMissingPositive(nums=[1, 2, 0])
        print(r)
        assert r == 3

        r = sol.firstMissingPositive(nums=[3, 4, -1, 1])
        print(r)
        assert r == 2

        r = sol.firstMissingPositive(nums=[7, 8, 9, 11, 12])
        print(r)
        assert r == 1

    unit_test(Solution())
