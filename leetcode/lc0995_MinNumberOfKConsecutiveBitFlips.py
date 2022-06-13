# You are given a binary array nums and an integer k.
# A k-bit flip is choosing a subarray of length k from nums and 
# simultaneously changing every 0 in the subarray to 1, and 
# every 1 in the subarray to 0.
# Return the minimum number of k-bit flips required so that there
# is no 0 in the array. If it is not possible, return -1.
# A subarray is a contiguous part of an array.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= k <= nums.length
from typing import List


# Greedy + Sliding window - T/S: O(n), O(n)
# Analysis
# - iterate over nums, find first 0 in A[i]
# - there is only one way to filp A[i], just starting from
#   that position, not left, not right
# - so, use greedy, from left to right, flip any existing or flipped 0's
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = [0] * n
        flips = 0   # flips in k-sliding-window
        res = 0
        for i in range(n):
            if i - k >= 0:
                flips -= flipped[i - k]
            if flips % 2 == nums[i]:
                if i + k > n:
                    return -1
                flipped[i] = 1
                flips += 1
                res += 1
        
        return res


# Greedy + Sliding window - T/S: O(n), O(1)
# - Use nums to save flipped info in place, change it back
#   when sliding window is moving out of the view.
class Solution1:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        res = 0
        for i in range(n):
            if i - k >= 0 and nums[i-k] >= 2:
                nums[i-k] -= 2
                flips -= 1
            if flips % 2 == nums[i]:
                if i + k > n:
                    return -1
                nums[i] += 2
                flips += 1
                res += 1
        
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minKBitFlips([0,1,0], k = 1)
        print(r)
        assert r == 2

        r = sol.minKBitFlips([1,1,0], k = 2)
        print(r)
        assert -1

        r = sol.minKBitFlips([0,0,0,1,0,1,1,0], k = 3)
        print(r)
        assert 3

    unit_test(Solution())
    unit_test(Solution1())
