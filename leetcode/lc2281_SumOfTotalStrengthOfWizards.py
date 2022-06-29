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
# Better Explain: https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2062017/C%2B%2B-prefix-%2B-monotonic-stack-O(N)-solution-with-thought-process
# related: monotonic stack
#   0496_NextGreaterElementI 
#   0503_NextGreaterElementII
# Algorithm
# - For each strength[i], we could find a non-empty index range (left, right) 
#   where strength[i] is the min value. So for all subarrays in this range 
#   including strength[i], the total strength is strength[i] * the sum of
#   those subarray sums.
# - left is the first index on the left side i where strength[left] < strength[i]
# - right is the first index on the right side of i where strength[right] <= strength[i]
# - These two indices can be pre-calculated using monotonic stack.
# - The reason we use < on left but <= on right is to avoid duplicates.
#   Here is an example array: 1 (2 3 4 2) 3 4 2 1
#   For the highlighted subarray 2 3 4 2, we want to calculate the strength using 
#   the 2nd 2 but not the first 2.
# - How do we get the "sum of all subarrays including strength[i] in range (left, right)"?
#   - Let's list the indices:
#       ...left-1, left, left + 1, left + 2, ... i-1, i, i+1, ... right-1, right, right+1...
#   - Let prefix[i] be the prefix sum of first i elements in strength.
#   - The sum of subarrays including i are:
#     - the subarrays that start with left+1, end with i, i+1, right-1
#         sum(left+1, ... i) = prefix[i + 1] - prefix[left + 1]
#         sum(left+1, ... i+1) = prefix[i + 2] - prefix[left + 1]
#         ...
#         sum(left+1, ... right-1) = prefix[right] - prefix[left + 1]
#     - the subarrays that start with left+2, end with i, i+1, right-1
#         sum(left+2, ... i) = prefix[i + 1] - prefix[left + 2]
#         sum(left+2, ... i+1) = prefix[i + 2] - prefix[left + 2]
#         ...
#         sum(left+2, ... right-1) = prefix[right] - prefix[left + 2]
#         ...
#     - the subarrays that start with i, end with i, i+1, right-1
#         sum(i, ... i) = prefix[i + 1] - prefix[i]
#         sum(i, ... i+1) = prefix[i + 2] - prefix[i]
#         ...
#         sum(i, ... right-1) = prefix[right] - prefix[i]
#   - Then we combine all above terms, we have:
#     - positive parts:
#         (prefix[i + 1] + prefix[i + 2] + ... + prefix[right]) * (i - left)
#     - negative parts:
#         (prefix[left + 1] + prefix[left + 2] + ... + prefix[i]) * (right - i)
# - The range sum of prefix can be optimized by pre-computing prefix-sum of prefix.
#     - let acc = prefix-sum(prefix)
#     - positive parts:
#         (acc[right] - acc[i]) * (i - left)
#     - negative parts:
#         (acc[i] - acc[left]) * (right - i)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        A = strength
        n = len(A)
        mod = 10**9 + 7

        # position of next smaller on the right, or, n
        right = [n] * n
        stack = []  # mono-increasing stack
        for i, v in enumerate(A):
            while stack and A[stack[-1]] > v:
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
