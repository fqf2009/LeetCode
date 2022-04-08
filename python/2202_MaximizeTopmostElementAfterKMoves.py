# You are given a 0-indexed integer array nums representing the contents of a
# pile, where nums[0] is the topmost element of the pile.
#
# In one move, you can perform either of the following:
#  - If the pile is not empty, remove the topmost element of the pile.
#  - If there are one or more removed elements, add any one of them back onto the pile.
# This element becomes the new topmost element.
#
# You are also given an integer k, which denotes the total number of moves to be made.
#
# Return the maximum value of the topmost element of the pile possible after exactly k
# moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.
#
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i], k <= 10^9
from typing import List


# Analysis:
# - The target is to search as far as possible
# - when k < n, two choice:
#     1. pop up k-1 item, then put back in max one
#     2. pop up k items, then the k+1 th items is at top
#   therefore, res = max(max(nums[:k-1]), nums[k])
# - when k == n, max(nums[:k-1]), because if take all n
#   items, the pile is empty.
# - when k > n, res = max(nums), just take all n items,
#   then put back (and then pop up if necessary) any item, 
#   but the last step is to put back the max one.
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]
        if k == n:
            return max(nums[:k-1])
        if k > n:
            return max(nums)
        return max(max(nums[:k-1]), nums[k])


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumTop([2], 1)
        print(r)
        assert r == -1

        r = sol.maximumTop([2], 2)
        print(r)
        assert r == 2

        r = sol.maximumTop([2], 3)
        print(r)
        assert r == -1

        r = sol.maximumTop([2], 0)
        print(r)
        assert r == 2

        r = sol.maximumTop([5, 2, 2, 8, 0, 6], 4)
        print(r)
        assert r == 5

        r = sol.maximumTop([5, 2, 2, 3, 0, 6], 5)
        print(r)
        assert r == 6

        r = sol.maximumTop([5, 2, 2, 3, 0, 6], 6)
        print(r)
        assert r == 5

        r = sol.maximumTop([5, 2, 2, 3, 0, 6], 7)
        print(r)
        assert r == 6

        r = sol.maximumTop([5, 2, 2, 3, 0, 6], 8)
        print(r)
        assert r == 6

        r = sol.maximumTop([73, 63, 62, 16, 95, 92, 93, 52, 89, 36, 75, 79, 
                            67, 60, 42, 93, 93, 74, 94, 73, 35, 86, 96], 59)
        print(r)
        assert r == 96

        r = sol.maximumTop([35, 43, 23, 86, 23, 45, 84, 2, 18, 83, 79, 28, 54, 81, 12, 94, 14, 0, 0, 29,
                            94, 12, 13, 1, 48, 85, 22, 95, 24, 5, 73, 10, 96, 97, 72, 41, 52, 1, 91, 3,
                            20, 22, 41, 98, 70, 20, 52, 48, 91, 84, 16, 30, 27, 35, 69, 33, 67, 18, 4,
                            53, 86, 78, 26, 83, 13, 96, 29, 15, 34, 80, 16, 49], 15)
        print(r)
        assert r == 94

    unitTest(Solution())
