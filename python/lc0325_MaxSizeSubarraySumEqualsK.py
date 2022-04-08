# Given an integer array nums and an integer k, return the maximum length
# of a subarray that sums to k. If there is not one, return 0 instead.

from typing import List


# PrefixSum: time complexity: O(n), space complexity: O(n)
# - Assume a prefixSum array is calculted as:
#       prefixSum[i] = sum(nums[:i+1]), i.e., sum(nums[0], ..., nums[i])
# - note subarray is not sub sequence, subarray are continuous, so,
#       if prefixSum[j] - prefixSum[i] == k, then
#       sum(nums[j+1], ..., nums[i]) == k, and len(subarray) is (i - j)
# - Similar to the solution for TwoSum problem, there is no need to use two
#   level of nested loop: TwoSum build hash table during the scan, and keep
#   testing whether (k - nums[i]) is already in the hash table.
# - So the solution for this problem is like "TwoMinus". We build PrefixSum
#   hash table (dict) during the scan. if the current (PrefixSum - k) already
#   exists in the hash table, we know there is an subarray which sums to k.
# - Because we need the longest subarray, and PrefixSum maps to position i,
#   each time a PrefixSum already exists in hash table, we will not update
#   its position, because the older one has lower pos.
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = {0: -1}     # prefixSum is 0, when pos is -1
        csum = 0
        maxLen = 0
        for i in range(len(nums)):
            csum += nums[i]
            if csum - k in prefixSum:
                maxLen = max(maxLen, i - prefixSum[csum - k])
            if csum not in prefixSum:
                prefixSum[csum] = i

        return maxLen


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxSubArrayLen([1, -1, 5, -2, 3], k=3)
        print(r)
        assert r == 4

        r = sol.maxSubArrayLen([-2, -1, 2, 1], k=1)
        print(r)
        assert r == 2

    unitTest(Solution())
