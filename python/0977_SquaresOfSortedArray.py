# Given an integer array nums sorted in non-decreasing order, return
# an array of the squares of each number sorted in non-decreasing order.

from typing import List

# Two Pointers - O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        for i in reversed(range(len(nums))):
            n1, n2 = nums[p1]**2, nums[p2]**2
            if n1 >= n2:
                res[i] = n1
                p1 += 1
            else:
                res[i] = n2
                p2 -= 1

        return res

# O(n*log(n))
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.sortedSquares([-4, -1, 0, 3, 10])
        print(r)
        assert r == [0, 1, 9, 16, 100]

        r = sol.sortedSquares([-7, -3, 2, 3, 11])
        print(r)
        assert r == [4, 9, 9, 49, 121]

    unitTest(Solution())
    unitTest(Solution1())
