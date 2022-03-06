# You are given an integer array nums and an integer k. Append k unique 
# positive integers that do not appear in nums to nums such that the 
# resulting total sum is minimum.
# Return the sum of the k integers appended to nums.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i], k <= 10^9
from typing import List


# Array
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        v0 = 0          # previous num
        res = 0
        cnt = 0
        for v in nums:  # v is current num
            if v > v0 + 1:
                if v - (v0 + 1) > (k - cnt):
                    v = (v0 + 1) + k - cnt
                cnt += v - (v0 + 1)
                res += (v + v0) * (v - v0 - 1) // 2
                if cnt == k: break
            v0 = v

        if cnt < k:
            res += (v0 + 1 + v0 + (k-cnt)) * (k-cnt) // 2

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minimalKSum(nums = [1,4,25,10,25], k = 2)
        print(r)
        assert r == 5

        r = sol.minimalKSum(nums = [5,6], k = 6)
        print(r)
        assert r ==25
        
    unitTest(Solution())
