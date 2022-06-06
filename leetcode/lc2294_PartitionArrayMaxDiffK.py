# You are given an integer array nums and an integer k. You may partition 
# nums into one or more subsequences such that each element in nums appears 
# in exactly one of the subsequences.
# Return the minimum number of subsequences needed such that the difference 
# between the maximum and minimum values in each subsequence is at most k.
# A subsequence is a sequence that can be derived from another sequence by 
# deleting some or no elements without changing the order of the remaining 
# elements.
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^5
#   0 <= k <= 10^5
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = nums[0]
        res = 1
        for v in nums[1:]:
            if v > start + k:
                start = v
                res += 1
        
        return res


class Solution1:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, i = 0, 0
        while i < len(nums):
            res += 1
            j = i
            while(i < len(nums) and nums[i] - nums[j] <= k):
                i += 1

        return res


if __name__ == '__main__':
    def unit_partitionArray(sol):
        r = sol.partitionArray([3,6,1,2,5], k = 2)
        print(r)
        assert r == 2

        r = sol.partitionArray([1,2,3], k = 1)
        print(r)
        assert r == 2

        r = sol.partitionArray([2,2,4,5], k = 0)
        print(r)
        assert r == 3

    unit_partitionArray(Solution())
    unit_partitionArray(Solution1())
