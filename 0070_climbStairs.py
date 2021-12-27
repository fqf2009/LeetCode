# You are climbing a staircase. It takes n steps to reach the top. Each time you 
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Actually this is Fibonacci problem in disguise.
# Dynamic Programming: time complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

 
    # How about different ways to reach the N’th stair with M different steps?
    # ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... + ways(n-m, m)
    # Time Complexity: O(n*m)
    def climbStairs2(self, n: int, m: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = sum(dp[max(0, i - m): i])

        return dp[n]


if __name__ == '__main__':
    r = Solution().climbStairs(2)
    print(r)
    assert(r == 2)

    r = Solution().climbStairs(3)
    print(r)
    assert(r == 3)

    r = Solution().climbStairs(5)
    print(r)
    assert(r == 8)

    r = Solution().climbStairs2(2, 2)
    print(r)
    assert(r == 2)

    r = Solution().climbStairs2(3, 2)
    print(r)
    assert(r == 3)

    r = Solution().climbStairs2(5, 2)
    print(r)
    assert(r == 8)

    r = Solution().climbStairs2(2, 3)
    print(r)
    assert(r == 2)

    r = Solution().climbStairs2(3, 3)
    print(r)
    assert(r == 4)

    r = Solution().climbStairs2(5, 3)
    print(r)
    assert(r == 13)
