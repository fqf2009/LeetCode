# There is only one character 'A' on the screen of a notepad. You can  
# perform two operations on this notepad for each step:
#  - Copy All: You can copy all the characters present on the 
#    screen (a partial copy is not allowed).
#  - Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get 
# the character 'A' exactly n times on the screen.

# Constraints:
#   1 <= n <= 1000
from functools import cache, reduce


# Math - prime factorization O(sqrt(n))
# Analysis
# - if n is prime number, then copy and paste n-1 times, need n steps.
# - if n is composite number, e.g. n = p*q, where p, q is prime number,
#   need p step to get p A's, then another q step to get p*q A's,
#   total p+q steps.
class Solution:
    def minSteps(self, n: int) -> int:
        i, res = 2, 0
        while n > 1 and i <= n ** 0.5 + 1:
            if n % i == 0:
                n //= i
                res += i
            else:
                i += 1

        if n > 1:
            res += n
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minSteps(3)
        print(r)
        assert r == 3

        r = sol.minSteps(6)
        print(r)
        assert r == 5

        r = sol.minSteps(1000)
        print(r)
        assert r == 21

        r = sol.minSteps(1)
        print(r)
        assert r == 0

    unitTest(Solution())        
