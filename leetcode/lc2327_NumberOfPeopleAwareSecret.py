# On day 1, one person discovers a secret.
# You are given an integer delay, which means that each person will share 
# the secret with a new person every day, starting from delay days after 
# discovering the secret. You are also given an integer forget, which 
# means that each person will forget the secret forget days after 
# discovering it. A person cannot share the secret on the same day they 
# forgot it, or on any day afterwards.
# Given an integer n, return the number of people who know the secret at the 
# end of day n. Since the answer may be very large, return it modulo 10^9 + 7.
# Constraints:
#   2 <= n <= 1000
#   1 <= delay < forget <= n
from collections import deque


# DP - T/S: O(n*(forget - delay)), O(n)
# - let dp[i] be the number of people starting to know the secret at i-th day:
#       dp[i] = dp[i - forget + 1] + dp[i - forget + 2] + ... + dp[i - delay]
# - let aware[i] to be the total people knowing the secret at i-th day
#       aware[i] = sum(dp[i - forget + 1], dp[i - forget + 2], ..., dp[i]), i.e.,
#       aware[i] = aware[i-1] + dp[i] - dp[i - forget]
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * n  # first day people know secret
        dp[0] = 1
        aware = 1
        for i in range(1, n):
            for j in range(i - forget + 1, i - delay + 1):
                if j >= 0:
                    dp[i] += dp[j]
            aware += dp[i]
            if i - forget >= 0:
                aware -= dp[i - forget]

        return aware % mod


# DP - T/S: O(n), O(n)
class Solution0:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * (n - 1)    # at i-th day, new people starting to know secret
        share = 0
        for i in range(1, n):       # it is ok if i - shre < 0, i - forget < 0
            dp[i] = share = (share + dp[i-delay] - dp[i - forget]) % mod

        return sum(dp[-forget:]) % mod


# DP: T/S: O(n), O(m), where m = forget
# Optimize:
# - let dp[] be deque[forget], 
# - each day, append the number of people starting to know secret
#             popleft the number of people starting to forget secret
# - the sum(dp[]) is the people aware of secret at certain day
# - let "sharable" be the number of people who can share:
#       sharable = sum(dp[0 : forget-delay]), i.e.,
#       sharable = prev_sharable - dp[0] + dp[forget-delay]
class Solution1:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = deque([1])
        sharable = 0
        for _ in range(1, n):
            if len(dp) >= delay:
                sharable += dp[-delay]
            if len(dp) >= forget:
                sharable -= dp[0]
                dp.popleft()
            dp.append(sharable)

        return sum(dp) % mod


# - without deque, use array in circular way
class Solution2:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * (forget - 1)
        sharable = 0
        for i in range(1, n):
            sharable = (sharable + dp[(i-delay)%forget] - dp[i%forget]) % mod
            dp[i%forget] = sharable

        return sum(dp) % mod


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.peopleAwareOfSecret(6, delay=2, forget=4)
        print(r)
        assert r == 5

        r = sol.peopleAwareOfSecret(4, delay=1, forget=3)
        print(r)
        assert r == 6

        r = sol.peopleAwareOfSecret(891, 474, 526)
        print(r)
        assert r == 52

    unit_test(Solution())
    unit_test(Solution0())
    unit_test(Solution1())
    unit_test(Solution2())
