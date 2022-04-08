# You are given two positive integers n and k. A factor of an integer n is 
# defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the 
# kth factor in this list or return -1 if n has less than k factors.
# Constraints:
#   1 <= k <= n <= 1000
import math


# T/S: O(sqrt(n)), O(k)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = int(math.sqrt(n))
        factors = []
        for i in range(1, root + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    return factors[-1]

        if root**2 == n:
            factors.pop()
            k -= 1

        if k - len(factors) <= len(factors):
            return n // (factors[- (k - len(factors))])
        else:
            return -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.kthFactor(12, 3)
        print(r)
        assert r == 3

        r = sol.kthFactor(7, 2)
        print(r)
        assert r == 7

        r = sol.kthFactor(4, 4)
        print(r)
        assert r == -1

    unitTest(Solution())
