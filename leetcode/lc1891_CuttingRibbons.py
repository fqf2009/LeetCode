# You are given an integer array ribbons, where ribbons[i] represents the length 
# of the ith ribbon, and an integer k. You may cut any of the ribbons into any 
# number of segments of positive integer lengths, or perform no cuts at all.
# For example, if you have a ribbon of length 4, you can:
#  - Keep the ribbon of length 4,
#  - Cut it into one ribbon of length 3 and one ribbon of length 1,
#  - Cut it into two ribbons of length 2,
#  - Cut it into one ribbon of length 2 and two ribbons of length 1, or
#  - Cut it into four ribbons of length 1.
# Your goal is to obtain k ribbons of all the same positive integer length. 
# You are allowed to throw away any excess ribbon as a result of cutting.
# Return the maximum possible positive integer length that you can obtain 
# k ribbons of, or 0 if you cannot obtain k ribbons of the same length.
# Constraints:
#   1 <= ribbons.length <= 10^5
#   1 <= ribbons[i] <= 10^5
#   1 <= k <= 10^9
from typing import List


# Binary Search - T/S: O(n*log(m)), O(1), where m = max(ribbons)
# - exactly the same as: 2226_MaximumCandiesAllocatedToKChildren.py
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        i, j = 1, max(ribbons)
        res = 0
        while i <= j:
            rb_size = (i+j) // 2
            rb_cnt = sum(x // rb_size for x in ribbons)
            if rb_cnt >= k:
                res = rb_size
                i = rb_size + 1
            else:
                j = rb_size - 1

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.maxLength([9,7,5], k = 3)
        print(r)
        # assert r == 5

        r = sol.maxLength([7,5,9], k = 4)
        print(r)
        assert r == 4

        r = sol.maxLength([5,7,9], k = 22)
        print(r)
        assert r == 0

    unit_test(Solution())
