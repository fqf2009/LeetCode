# You are given an integer array nums of length n and an integer 
# numSlots such that 2 * numSlots >= n. There are numSlots slots 
# numbered from 1 to numSlots.

# You have to place all n integers into the slots such that each 
# slot contains at most two numbers. The AND sum of a given placement 
# is the sum of the bitwise AND of every number with its respective 
# slot number.

# For example, the AND sum of placing the numbers [1, 3] into slot 1 
# and [4, 6] into slot 2 is equal to (1 AND 1) + (3 AND 1) + (4 AND 2) 
# + (6 AND 2) = 1 + 1 + 0 + 2 = 4.
# Return the maximum possible AND sum of nums given numSlots slots.

# Constraints:
#   n == nums.length
#   1 <= numSlots <= 9
#   1 <= n <= 2 * numSlots
#   1 <= nums[i] <= 15
from typing import List
from functools import cache 


# Ideas from https://leetcode.com/problems/maximum-and-sum-of-array/discuss/1766824/JavaC%2B%2BPython-DP-Solution
# A little bit improvement for performance.
# - if nums[i] == slot, then nums[i] & slot == nums[i] == slot,
#   so this number is the best value or best fit for this slot.
# - Remove these best fit number from array, and also remove the corresponding
#   spaces from slots, it will greatly reduce the number of recursive retry attempts.
# - evidence:
#     Input:  nums = list(range(1, 19)), numSlots = 9
#     Output of dp.cache_info():
#       before: CacheInfo(hits=98416, misses=19683, maxsize=None, currsize=19683)
#       after : CacheInfo(hits=1793, misses=512, maxsize=None, currsize=512)
# - However, if nums[i] is outside of then [1..numSlots] range,
#   this over optimization is meaningless.
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @cache
        def dp(i, mask):
            res = 0
            if i == len(A): return 0
            for slot in range(1, numSlots + 1): # for nums[i], try every slot
                b = 3 ** (slot - 1)
                if mask // b % 3 > 0:
                    res = max(res, (A[i] & slot) + dp(i + 1, mask - b))
            return res

        A = []
        mask = 3 ** numSlots - 1
        res = 0
        for v in nums:
            b = 3**(v-1)
            if v <= numSlots and mask // b % 3 > 0:
                mask -= b
                res += v
            else:
                A.append(v)
        res += dp(0, mask)
        print(dp.cache_info())
        return res


# Ideas from https://leetcode.com/problems/maximum-and-sum-of-array/discuss/1766824/JavaC%2B%2BPython-DP-Solution
# DP + Recursion + Memo
# Analysis:
# - use bit mask to indicate which slot is available or not
# - base-3 is perfect for this:
#   0 - no space available in this slot
#   1 - one space available in this slot
#   2 - two spaces available in this slot 
# - initially, mask = 3^ns - 1, to indicate all slots with available spaces:
#   e.g., for ns = 5, mask = 22222 (base-3)
# - for each number, nums[i], it will try every slot, each time when it pick a slot,
#   it modify mask, and let remaining number to try left over slots and spaces.
# - b = 3 ^ (slot - 1), bit for each slot,
#   e.g., for slot 1, 2, 3, bit is 1, 3, 9.
# - mask // b, remove the trailing (slot - 1) mask,
#   e.g., mask = 22210 (base-3), slot = 3,
#   then b = 3^(3-1), mask // b = 222, i.e. the trailing two bits are chopped off.
# - mask // b % 3, in above example, get the '2', two spaces available in slot 3.
#
# Time: O(ns * 3^ns), Space: O(3^ns), where ns is numSlots
# - evidence:
#     Input:  nums = list(range(1, 19)), numSlots = 9
#     Output of dp.cache_info():
#             CacheInfo(hits=98416, misses=19683, maxsize=None, currsize=19683)
#     where 19683 == 3^9
# - The reason is, in dp[i, mask], the mask already has the info of slot used?
#   because of the (mask - b)?
# - for @cache, it is automatic that only O(3^ns) memory is used.
#   if using array, memo[i, mask] vs. memo[mask], a lot of memory is wasted or saved.
class Solution1:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @cache
        def dp(i, mask):
            res = 0
            if i == len(nums): return 0
            for slot in range(1, numSlots + 1): # for nums[i], try every slot
                b = 3 ** (slot - 1)
                if mask // b % 3 > 0:
                    res = max(res, (nums[i] & slot) + dp(i + 1, mask - b))
            return res
        
        res = dp(0, 3 ** numSlots - 1)
        print(dp.cache_info())
        return res


# Same solution using base-10, easier to understand than base-3
class Solution2:
    def maximumANDSum(self, A: List[int], ns: int) -> int:
        @cache
        def dp(i, mask):
            if i == len(A): return 0
            res = 0
            for slot in range(1, ns + 1):
                b = 10 ** (slot - 1)
                if ((mask // b) % 10) < 2:
                    res = max(res, dp(i + 1, mask + b) + (A[i] & slot))
            return res
        
        res = dp(0, 0)
        print(dp.cache_info())
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumANDSum([1,2,3,4,5,6], 3)
        print(r)
        assert r == 9

        r = sol.maximumANDSum([1,3,10,4,7,1], 9)
        print(r)
        assert r == 24

        r = sol.maximumANDSum(list(range(1, 19)), 9)
        print(r)
        assert r == 87

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
