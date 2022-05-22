# As the ruler of a kingdom, you have an army of wizards at your command.
# You are given a 0-indexed integer array strength, where strength[i] 
# denotes the strength of the ith wizard. For a contiguous group of 
# wizards (i.e. the wizards' strengths form a subarray of strength),
# the total strength is defined as the product of the following two values:
#   The strength of the weakest wizard in the group.
#   The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. 
# Since the answer may be very large, return it modulo 109 + 7.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Constraints:
# 1 <= strength.length <= 10^5
# 1 <= strength[i] <= 10^9
from itertools import accumulate
from typing import List


# T/S: O(n), O(n)
# From: https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2061985/Python-Solution-O(n)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        A = strength
        n = len(A)
        mod = 10**9 + 7

        # position of next smaller on the right, or, n
        right = [n] * n
        stack = []  # mono-increasing stack
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        # position of next smaller or equal on the left, or, -1
        left = [-1] * n
        stack = []
        for i in reversed(range(n)):
            while stack and A[stack[-1]] >= A[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each A[i] as minimum, compute the sum
        # initial=0 will make acc = [0, ...], length is n+1
        acc = list(accumulate(accumulate(A), initial=0))
        res = 0
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res = (res + A[i] * (racc * ln - lacc * rn)) % mod

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.totalStrength([1, 3, 1, 2])
        print(r)
        assert r == 44

        r = sol.totalStrength([5, 4, 6])
        print(r)
        assert r == 213

    unit_test(Solution())
