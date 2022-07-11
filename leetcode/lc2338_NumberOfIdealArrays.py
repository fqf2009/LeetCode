# You are given two integers n and maxValue, which are used to describe
# an ideal array.
# A 0-indexed integer array arr of length n is considered ideal if
# the following conditions hold:
#  - Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
#  - Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the
# answer may be very large, return it modulo 10^9 + 7.
# Constraints:
#   2 <= n <= 10^4
#   1 <= maxValue <= 10^4
from collections import Counter
from functools import cache
import math


# Math - T/S: O(V*(sqrt(V))), O(V), where V = maxValue
# Analysis
# - let v be the value in ideal array, 1 <= v <= maxValue
# - let PF[] be all the prime factors of v
# - now the problem become how to distribute PF[i] in the array
#   - each pos could be distributed of more than one PF
#   - if a cell is not distributed of PF, it is filled with 1
#   - let FV[i] be the filled factors at pos i
#   - the array[i]'s value is the product of FV up to pos i:
#         array[i] = FV[0] * FV[1] * ... * FV[i]
#   - e.g.:  n = 5, end_value = 10 = 2 * 5
#     distribute PF:                array values:
#     1, 1, 1, 2, 5                 1, 1, 1, 2,  10
#     1, 1, 2, 1, 5                 1, 1, 2, 2,  10
#     1, 2, 1, 1, 5                 1, 2, 2, 2,  10
#     1, 2, 1, 5, 1                 1, 2, 2, 10, 10
#     1, 10, 1, 1, 1                1, 10, 10, 10, 10
#     ...
# - How many distributions for n cells and m distinct factors?
#   each distinct factors can in put in any cell, total ways: n^m
# - How to handle multiple occurrence of the same factors?
#   https://baike.baidu.com/item/%E6%94%BE%E7%90%83%E9%97%AE%E9%A2%98/12740706
#   假设m个球和n-1个板放到n+m-1个位置，第1个板前的放进第一个盒子，第i-1个版和第i个版
#   之间的球放进第i个盒子，则共有C(m+n-1,m)种放法。
# - https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
# - https://zh.wikipedia.org/wiki/%E9%9A%94%E6%9D%BF%E6%B3%95
# - To put m identical balls into n numbered boxes:
#   imagine there are n-1 identical separators and m identical balls, put them
#   into total m+n-1 places, the balls with pos relative to separators will go
#   to different box. there are comb(n+m-1, m) ways to place them.
#   - e.g. 8 = 2^3, how to put 3 2's into 6 cells: comb(6+3-1, 3) = comb(8, 3)
#            2 | 2 | 2 |   |   |
#     cells: ^   ^   ^   ^   ^   ^
#            2 2 |   | 2 |   |   |
#     cells: ^     ^   ^   ^   ^   ^
# - let pf_cntr be the Counter() of prime factors of v (last value in array),
#   for each pf in pf_cntr: ways *= Comb(n+m-1, m)
#   note: when m == 1, Comb(n, 1) == n
class Solution:
    def all_primes(self, n: int) -> list[int]:
        is_prime = [True] * (n + 1)
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, n + 1) if is_prime[i]]

    @cache
    def comb(self, n: int, m: int) -> int:
        mod = 10**9 + 7
        return math.comb(n, m) % mod

    def idealArrays(self, n: int, maxValue: int) -> int:
        primes = self.all_primes(maxValue)

        def count_prime_factors(v: int) -> Counter:
            cntr = Counter()
            for p in primes:
                if v == 1:
                    break
                while v % p == 0:
                    v //= p
                    cntr[p] += 1
            return cntr

        res, mod = 0, 10**9 + 7
        for v in range(1, maxValue + 1):
            cmb = 1
            cntr = count_prime_factors(v)
            for freq in cntr.values():
                cmb = (cmb * self.comb(n + freq - 1, freq)) % mod
            res = (res + cmb) % mod

        return res


# DP (Bottom-up) - T/S: O(n*V^2), O(V), where V = maxValue
# - TLE (Time Limited Exceeded)
class Solution1:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        dp = [1] * (maxValue + 1)
        for _ in range(1, n):
            dp2 = [0] * (maxValue + 1)
            for j in range(1, maxValue + 1):
                dp2[j] = sum(dp[k] for k in range(j, maxValue + 1, j)) % mod
            dp = dp2

        return sum(dp) % mod


# DP (Top-down) - T/S: O(n*V^2), O(n*V), where V = maxValue
# - TLE (Time Limited Exceeded)
# - RecursionError: maximum recursion depth exceeded
class Solution2:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp_count(start, pos) -> int:
            if pos == n - 1:
                return maxValue // start
            res = 0
            for i in range(start, maxValue + 1, start):
                res = (res + dp_count(i, pos + 1)) % mod
            return res % mod

        return dp_count(1, 0) % mod


# DP + Backtracking (Top-down)
# - improved, no performance issue!
# - start from first item in array, the value (v[0]) could be 1..maxValue
# - move to next item in array, set the value (v[1]) to be multiple of v[0],
#   i.e., 2*v[0], 3*v[0], ..., x*v[0] <= maxValue
# - continue ...
# - in this process, for any intermediate value v[p], it comes
#   from all distinct values: v[0], v[1], ..., v[p];
# - if we stop multiply them and let them to be spreaded out, and let the
#   last v[n-1] be the value of current v[p], how many ways are there?
#   e.g.: prefix is [1,2,6,12,...], and, n = 10, if we want v[9] = 12:
#   possible way to spread: [1, 1, 1, 2, 2, 6, 6, 6, 12, 12]
#                                     ^     ^        ^
#                           [1, 1, 2, 2, 2, 6, 6, 6, 12, 12]
#                                  ^        ^        ^
#                           [1, 2, 2, 2, 2, 2, 6, 6, 12, 12]
#                               ^              ^     ^
#                           ...
# - here v[0] cannot move, p == 3, we can move (pick) the first pos
#   for p (3) items in the remaining n-1 (9) places, the possible ways:
#   combination(n-1, p) = comb(9, 3) = 84
# - since all the values keep increasing, so no duplicate counting
class Solution3:
    @cache
    def comb(self, n: int, m: int) -> int:
        mod = 10**9 + 7
        return math.comb(n, m) % mod

    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(v, pos) -> int:
            res = self.comb(n-1, pos)
            if pos == n-1 or v * 2 > maxValue:
                return res
            for v1 in range(v * 2, maxValue + 1, v):
                res += dp(v1, pos + 1)
            return res % mod

        return sum(dp(i, 0) for i in range(1, maxValue + 1)) % mod


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.idealArrays(n=5, maxValue=9)
        print(r)
        assert r == 111

        r = sol.idealArrays(n=2, maxValue=5)
        print(r)
        assert r == 10

        r = sol.idealArrays(n=5, maxValue=3)
        print(r)
        assert r == 11

        r = sol.idealArrays(n=58, maxValue=29)
        print(r)
        assert r == 3001269

        r = sol.idealArrays(n=5878, maxValue=2900)
        print(r)
        assert r == 465040898

        r = sol.idealArrays(9767, 9557)
        print(r)
        assert r == 1998089

    unit_test(Solution())
    # unit_test(Solution1())
    # unit_test(Solution2())
    unit_test(Solution3())
