# Numbers can be regarded as the product of their factors.
#   For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its
# factors. You may return the answer in any order.
# Note that the factors should be in the range [2, n - 1].
# Constraints:
#   1 <= n <= 10^7
from typing import List
from functools import cache
from math import sqrt


# - Get prime factors first, then combine them
# - assume dp[i] is the list of factors meeting the criteria using the first
#   i number of factors.
# - dp[i+1] will iterate through dp[i] result list's item (which is list too),
#   append fac[i+1] to each list, or multiple to each item in the list.
# - e.g. for n = 32, fac = [2, 2, 2, 2, 2]
#       dp[0] = [[2]]
#       dp[1] = [[2, 2], [4]]
#       dp[2] = [[2, 2, 2], [4, 2], [2, 4], [4, 2], [8]], need sort unique to:
#               [[2, 2, 2], [2, 4], [8]]
#       dp[3] = [[2, 2, 2, 2], [4, 2, 2], [2, 4, 2], [2, 2, 4], 
#                [2, 4, 2], [4, 4], [2, 8], [16]]         need sort unique to:
#               [[2, 2, 2, 2], [2, 2, 4], [4, 4], [2, 8], [16]
#       ...
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dpFactors(pos: int):
            if pos == 0:
                return {(fac[0],)}
            factors = dpFactors(pos - 1)
            res = set()
            for f in factors:
                res.add(tuple(sorted(f + (fac[pos],))))
                if len(f) == 1 and pos == len(fac) - 1: continue # exclude n itself
                for i in range(len(f)):
                    f1 = list(f)
                    f1[i] *= fac[pos]
                    res.add(tuple(sorted(f1)))
            return res

        primes = [2]
        for i in range(3, int(sqrt(n)) + 1):
            for p in primes:
                if p * p > i:
                    primes.append(i)
                    break
                if i % p == 0:
                    break

        fac = []
        i, m = 0, n
        while m > 1 and i < len(primes):
            if m % primes[i] == 0:
                fac.append(primes[i])
                m = m // primes[i]
            else:
                i += 1
        if m > 1:
            fac.append(m)

        if len(fac) <= 1:   # exclude n itself (prime number)
            return []
        return [list(x) for x in dpFactors(len(fac) - 1)]


# DP + Recursion + Memo - O(n*sqrt(n)) - Time Limited Exceed
# TLE - factorize one number is enough, why factorize every factor???
# Analysis:
# - assume dp(n) is the list of factors meeting the criteria.
# - iterate through all factors of n, assume f1 is factor,
#   then f2 = n // f1, i.e., n = f1 * f2
# - dp(n) = for every f1, and f2 combination,
#       adding f1 to each item list in dp(f2), union with,
#       adding f2 to each item list in dp(f1)
class Solution1:
    def getFactors(self, n: int) -> List[List[int]]:
        @cache
        def dpFactors(n: int):
            res = set()
            d = 2
            while d * d <= n:
                if n % d == 0:
                    f1, f2 = d, n // d  # f1, f2 are factors (divisors)
                    for f1, f2 in ((f1, f2), (f2, f1)):
                        dp = dpFactors(f2)
                        dp.add((f2,))
                        res.update({tuple(sorted(x+(f1,))) for x in dp})
                d += 1
            return res

        primes = [2]
        i = 3
        while i <= n:
            for p in primes:
                if p * p > i:
                    primes.append(i)
                    break
                if i % p == 0:
                    break
            i += 1
        primeSet = set(primes)

        return [] if n in primeSet else [list(x) for x in dpFactors(n)]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.getFactors(1)
        print(r)
        assert sorted(r) == sorted([])

        r = sol.getFactors(1267697)
        print(r)
        assert sorted(r) == sorted([[167,7591]])

        r = sol.getFactors(32)
        print(r)
        assert sorted(r) == sorted([[2, 2, 2, 2, 2], [2, 2, 2, 4], 
                                    [2, 2, 8], [2, 4, 4], [2, 16], [4, 8]])

        r = sol.getFactors(12)
        print(r)
        assert sorted(r) == sorted([[2, 6], [3, 4], [2, 2, 3]])

        r = sol.getFactors(37)    # prime number
        print(r)
        assert r == []

    unitTest(Solution())
    # unitTest(Solution1())
