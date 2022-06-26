# There is a street with n * 2 plots, where there are n plots on each 
# side of the street. The plots on each side are numbered from 1 to n. 
# On each plot, a house can be placed.
# Return the number of ways houses can be placed such that no two houses 
# are adjacent to each other on the same side of the street. Since the 
# answer may be very large, return it modulo 10^9 + 7.
# Note that if a house is placed on the ith plot on one side of the 
# street, a house can also be placed on the ith plot on the other 
# side of the street.
# Constraints:
#   1 <= n <= 10^4
from functools import cache


# fibonacci
class Solution:
    def countHousePlacements(self, n: int) -> int:
        modulo = 10**9 + 7
        @cache
        def dp(n):
            if n <= 0: return 1
            return (dp(n-1) + dp(n-2)) % modulo

        return (dp(n) * dp(n)) % modulo


class Solution1:
    def countHousePlacements(self, n: int) -> int:
        modulo = 10**9 + 7
        f1, f2, res = 1, 1, 0
        for _ in range(n):
            res = (f1 + f2) % modulo
            f2, f1 = res, f2

        return res * res % modulo


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.countHousePlacements(1)
        print(r)
        assert r == 4

        r = sol.countHousePlacements(2)
        print(r)
        assert r == 9

        r = sol.countHousePlacements(3)
        print(r)
        assert r == 25

    unit_test(Solution())
    unit_test(Solution1())
