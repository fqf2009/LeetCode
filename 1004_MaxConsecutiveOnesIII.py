# Given a binary array nums and an integer k, return the maximum number 
# of consecutive 1's in the array if you can flip at most k 0's.
# Constraints:
#   1 <= nums.length <= 10^5
#   nums[i] is either 0 or 1.
#   0 <= k <= nums.length
from typing import List


# Sliding Window
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zeros = 0
        j = 0
        for i, v in enumerate(nums):
            zeros += 1 - v
            if zeros <= k:
                res = max(res, i - j + 1)
            else:                       # zeros > k
                while nums[j] != 0:     # find first 0
                    j += 1
                j += 1                  # skip 0
                zeros -= 1

        return res    


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2)
        print(r)
        assert r == 6

        r = sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
        print(r)
        assert r == 10

    unit_test(Solution())
