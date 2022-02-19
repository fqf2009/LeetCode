# Given an integer n, break it into the sum of k positive 
# integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.
# Example 1:
#   Input: n = 2
#   Output: 1
#   Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#   Input: n = 10
#   Output: 36
#   Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Constraints:
#   2 <= n <= 58
from functools import cache


# Math - except for special case, let each component near 3
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        q, r = divmod(n, 3)
        if r == 0:
            r = 1
        elif r == 1:
            r = 4
            q -= 1
        return 3**q * r


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.integerBreak(2)
        print(r)
        assert r == 1

        r = sol.integerBreak(10)
        print(r)
        assert r == 36

        r = sol.integerBreak(6)
        print(r)
        assert r == 9
        
    unitTest(Solution())
