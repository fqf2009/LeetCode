# You have some coins.  The i-th coin has a probability prob[i] of 
# facing heads when tossed.
# Return the probability that the number of coins facing heads 
# equals target if you toss every coin exactly once.

# Constraints:
#  - 1 <= prob.length <= 1000
#  - 0 <= prob[i] <= 1
#  - 0 <= target <= prob.length
#  - Answers will be accepted as correct if they are within 10^-5 of the correct answer.
from functools import cache
from typing import List

# DP + Iteration
# Time: O((n-m)*m), Space: O(n) (could be O(n-m), but too complex)
# Note the j < 0 situation. In recursion version, it is automatically handled by cache.
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        for i in range(1, n + 1):   # i-th toss
            dp1 = [0.0] * (n + 1)
            # j: the number coins facing heads.
            # (n-i): remaining toss
            # target - (n-i): least coins facing heads already to reach target
            # min(i + 1, target + 1): upper bound (non-inclusive) coins facing heads
            #                         by far it can reach, or it matters.
            for j in range(max(0, target - (n-i)), min(i + 1, target + 1)):
                if j == 0:
                    dp1[j] = dp[j]*(1-prob[i-1])
                else:
                    dp1[j] = dp[j-1]*prob[i-1] + dp[j]*(1-prob[i-1])
            dp = dp1

        return dp[target]


# LeetCode: Memory Limit Exceeded (28 / 28 test cases passed, but took too much memory)
# DP + Recursion + Memo
# Time:  O(n*m), where n is len(prob), m is target
# Space: O(n*m)
# - assume dp[i, j]: probability after i-th coins are tolled, j coins are facing heads
# - dp[0, 0] = 1
# - dp[0, j] = 0, where j != 0 (note here j < 0 is possible in function call)
# - dp[i, j] = dp[i-1, j-1]*prob[i-1] + dp[i-1, j]*(1-prob[i-1])
#   note dp is 1-based for i-th coin, prob use 0-based index for coins
class Solution1:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        @cache
        def dp(i, j) -> float:
            if i == 0:
                if j == 0:
                    return 1.0
                else:
                    return 0.0
            return dp(i-1, j-1)*prob[i-1] + dp(i-1, j)*(1-prob[i-1])

        return dp(len(prob), target)


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.probabilityOfHeads(prob = [0.4], target = 0)
        print(r)
        assert abs(r - 0.6) < 10**-5

        r = sol.probabilityOfHeads(prob = [0.4], target = 1)
        print(r)
        assert abs(r - 0.4) < 10**-5

        r = sol.probabilityOfHeads(prob = [0.5,0.5,0.5,0.5,0.5], target = 0)
        print(r)
        assert (r - 0.03125) < 10**-5

    unitTest(Solution())
    unitTest(Solution1())
