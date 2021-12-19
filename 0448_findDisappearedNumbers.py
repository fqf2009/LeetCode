from typing import List

# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all integers in range [1, n] that do not appear in nums.
# Follow up: Could you do it without extra space and in O(n) runtime? You may 
# assume the returned list does not count as extra space.

# Memo: in-place marking, i.e., set nums[i] to negative to indicate (i+1) exists
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            v = nums[i]
            if v < 0:
                v = -v
            if nums[v - 1] > 0:
                nums[v - 1] = -nums[v - 1]

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    r = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(r)
    assert r == [5, 6]

    r = Solution().findDisappearedNumbers([1, 1])
    print(r)
    assert r == [2]
