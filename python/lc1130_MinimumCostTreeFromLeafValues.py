# Given an array arr of positive integers, consider all binary trees such that:
# - Each node has either 0 or 2 children;
# - The values of arr correspond to the values of each leaf in an
#   in-order traversal of the tree.
# - The value of each non-leaf node is equal to the product of the
#   largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible
# sum of the values of each non-leaf node. It is guaranteed this sum fits
# into a 32-bit integer.

# Constraints:
#   2 <= arr.length <= 40
#   1 <= arr[i] <= 15
#   It is guaranteed that the answer fits into a 32-bit signed
#   integer (i.e., it is less than 2^31).

from typing import List, Tuple
from functools import cache

# Stack: O(n)
# Analysis:
# - ...
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        pass


# DP + Recursion + Memo: O(n^2)
# - assume dp(i, j) returns (min_sum, max_leaf) for all integers between
#   index i and index j.
# - pick every possible points to split the list of integers into left or
#   right child tree, let them compute (min_sum, max_leaf), then aggregate.
class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        @cache
        def dp(i, j) -> Tuple[int, int]:    # (min_sum, max_leaf)
            if i == j: return (0, arr[i])
            res = (2**31, 2**31)
            for k in range(i, j):
                sum1, leaf1 = dp(i, k)
                sum2, leaf2 = dp(k+1, j)
                res = min(res, (sum1 + sum2 + leaf1*leaf2, max(leaf1, leaf2)))
            return res

        return dp(0, n-1)[0]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.mctFromLeafValues([6, 2, 4])
        print(r)
        assert r == 32

        r = sol.mctFromLeafValues([4, 11])
        print(r)
        assert r == 44

    unitTest(Solution1())
