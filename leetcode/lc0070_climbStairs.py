# You are climbing a staircase. It takes n steps to reach the top. Each time you 
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

from functools import cache

# Recursion, DP, Memo
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# DP + Interative: T/S: O(n), O(1)
class Solution1:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 1
        res = 1     # if n <= 1
        for _ in range(2, n+1):
            res = dp0 + dp1
            dp1, dp0 = res, dp1
        return res


# Actually this is Fibonacci problem in disguise.
# Iteration, DP (Dynamic Programming): time complexity: O(n)
class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# How about different ways to reach the N’th stair with M different steps?
# ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... + ways(n-m, m)
# Time Complexity: O(n*m)
class Solution3:
    def climbStairsM(self, n: int, m: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = sum(dp[max(0, i - m): i])

        return dp[n]


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.climbStairs(1)
        print(r)
        assert r == 1

        r = sol.climbStairs(2)
        print(r)
        assert r == 2

        r = sol.climbStairs(3)
        print(r)
        assert r == 3

        r = sol.climbStairs(5)
        print(r)
        assert r == 8

    def unit_test2(sol):
        r = sol.climbStairsM(2, 2)
        print(r)
        assert r == 2

        r = sol.climbStairsM(3, 2)
        print(r)
        assert r == 3

        r = sol.climbStairsM(5, 2)
        print(r)
        assert r == 8

        r = sol.climbStairsM(2, 3)
        print(r)
        assert r == 2

        r = sol.climbStairsM(3, 3)
        print(r)
        assert r == 4

        r = sol.climbStairsM(5, 3)
        print(r)
        assert r == 13

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
    unit_test2(Solution3())
