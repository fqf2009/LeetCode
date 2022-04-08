# Given an integer n, return the least number of perfect 
# square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself. For
# example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Constraints:
#   1 <= n <= 10^4
from functools import cache
from math import sqrt


# DP + Recursion + Memo: O(sqrt(n))
class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        root = int(sqrt(n))
        if n == root*root: return 1
        return min(self.numSquares(n - i*i) + 1 for i in range(root, 0, -1))
        

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numSquares(12)
        print(r)
        assert r == 3   # 12 = 4+4+4

        r = sol.numSquares(13)
        print(r)
        assert r == 2   # 13 = 9+4
        
    unitTest(Solution())
