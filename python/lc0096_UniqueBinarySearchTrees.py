# Given an integer n, return the number of structurally 
# unique BST's (binary search trees) which has exactly 
# n nodes of unique values from 1 to n.

# Constraints:
#   1 <= n <= 19
from functools import cache


# Math - https://en.wikipedia.org/wiki/Catalan_number
# C[n] = 2n!/((n+1)!n!), or
# C[0] = 1, C[n+1] = C[n]*2*(2n+1)/(n+2)
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)


# DP + Recursion + Memo: O(n)
# Analysis:
# - Idea is to pick i as root, then [0..(i-1)] is in the left tree, and
#   [(i+1)..(n-1)] is in the right tree.
# - assume dp[n] is the number of unique BSTs for n unique numbers,
# - if for certain root node, left and right tree each have p and q numbers,
#   dp[p] * dp[q] is the number of unique BSTs for this root.
class Solution1:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0: return 1
        return sum(self.numTrees(i) * self.numTrees(n-1-i) for i in range(n))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numTrees(3)
        print(r)
        assert r == 5

        r = sol.numTrees(1)
        print(r)
        assert r == 1
        
    unitTest(Solution())
    unitTest(Solution1())
