# You are given two integer arrays nums1 and nums2. We write the 
# integers of nums1 and nums2 (in the order they are given) on 
# two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two 
# numbers nums1[i] and nums2[j] such that:
#  - nums1[i] == nums2[j], and
#  - the line we draw does not intersect any other connecting 
#    (non-horizontal) line.
# Note that a connecting line cannot intersect even at the 
# endpoints (i.e., each number can only belong to one connecting line).
# Return the maximum number of connecting lines we can draw in this way.
from functools import cache
from typing import List

# DP + Recursion + Memo: O(M*N)
# This problem is exactly the same as the 1143 Longest Common Subsequence.
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i, j-1), dp(i-1, j), dp(i-1, j-1))

        return dp(len(nums1)-1, len(nums2)-1)


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4])
        print(r)
        assert r == 2

        r = sol.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2])
        print(r)
        assert r == 3

        r = sol.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1])
        print(r)
        assert r == 2


    unitTest(Solution())
