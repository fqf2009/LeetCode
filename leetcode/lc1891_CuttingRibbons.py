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


# Binary Sort: Template 2
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        i, j = 0, max(ribbons)
        while i < j:
            m = (i+j+1) // 2    # <-- difference, to avoid endless loop!
            nb_ribbon = sum(x // m for x in ribbons)
            if nb_ribbon >= k:
                i = m           # <-- caused by this, i.e. if i+1 == j, and i is not moving, then ...
            else:       # nb_ribbon < k
                j = m - 1

        return i


# Binary Search: Template 1
# - T/S: O(n*log(m)), O(1), where m = max(ribbons)
# - exactly the same as: 2226_MaximumCandiesAllocatedToKChildren.py
class Solution1:
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
    unit_test(Solution1())
