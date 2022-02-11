# A wiggle sequence is a sequence where the differences between successive 
# numbers strictly alternate between positive and negative. The first 
# difference (if one exists) may be either positive or negative. A sequence 
# with one element and a sequence with two non-equal elements are trivially 
# wiggle sequences.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) alternate between positive and negative.

# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The 
# first is not because its first two differences are positive, and the second is 
# not because its last difference is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the
# original sequence, leaving the remaining elements in their original order.

# Given an integer array nums, return the length of the longest wiggle 
# subsequence of nums.

# Constraints:
#   1 <= nums.length <= 1000
#   0 <= nums[i] <= 1000

from typing import List

# Analysis:
# - use sign to record previous up-turn (1) and down-turn (1)
# - only when the turn (direction) is changed, increase the result.
# - initially set sign = 0, so it is not the same as subsequent value
# - but if diff is zero, do not set sign to 0, let next diff to
#   determine whether the direction is changed, or continue.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        sign = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                if sign != 1:
                    res += 1
                sign = 1
            elif diff < 0:
                if sign != -1:
                    res += 1
                sign = -1
        
        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.wiggleMaxLength(nums = [1,7,4,9,2,5])
        print(r)
        assert r == 6

        r = sol.wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8])
        print(r)
        assert r == 7

        r = sol.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9])
        print(r)
        assert r == 2

        r = sol.wiggleMaxLength(nums = [2])
        print(r)
        assert r == 1

    unitTest(Solution())
