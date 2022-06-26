# You are given two 0-indexed integer arrays nums1 and nums2, 
# both of length n.
# You can choose two integers left and right where 
# 0 <= left <= right < n and swap the subarray 
# nums1[left...right] with the subarray nums2[left...right].
# For example, if nums1 = [1,2,3,4,5] and nums2 = [11,12,13,14,15] 
# and you choose left = 1 and right = 2, nums1 becomes [1,12,13,4,5] 
# and nums2 becomes [11,2,3,14,15].
# You may choose to apply the mentioned operation once or not do anything.
# The score of the arrays is the maximum of sum(nums1) and sum(nums2), 
# where sum(arr) is the sum of all the elements in the array arr.
# Return the maximum possible score.
# A subarray is a contiguous sequence of elements within an array. 
# arr[left...right] denotes the subarray that contains the elements 
# of nums between indices left and right (inclusive).
# Constraints:
#   n == nums1.length == nums2.length
#   1 <= n <= 10^5
#   1 <= nums1[i], nums2[i] <= 10^4
from typing import List


# DP - T/S: O(n), O(1)
# Analysis:
# - build two virtual array A and B:
#   A[i] = nums1[i] - nums2[i]
#   B[i] = nums2[i] - nums1[i]
# - Prefix sum of A (PSA[i]) is what nums2 will get if exchanging
#   first i items with nums1
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        min_ps1, min_ps2 = 0, 0
        ps1 = ps2 = 0
        res1 = res2 = 0
        for v1, v2 in zip(nums1, nums2):
            ps1 += v1 - v2
            ps2 += v2 - v1
            res1 = max(res1, ps1 - min_ps1)
            res2 = max(res2, ps2 - min_ps2)
            min_ps1 = min(min_ps1, ps1)
            min_ps2 = min(min_ps2, ps2)
            # print(res1, res2)

        return max(s1, s2, s1 + res2, s2 + res1)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.maximumsSplicedArray([60,60,60], nums2 = [10,90,10])
        print(r)
        assert r == 210

        r = sol.maximumsSplicedArray([20,40,20,70,30], nums2 = [50,20,50,40,20])
        print(r)
        assert r == 220

        r = sol.maximumsSplicedArray([7,11,13], nums2 = [1,1,1])
        print(r)
        assert r == 31

    unit_test(Solution())
