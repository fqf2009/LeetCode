# Given two strings s1 and s2, return the lowest ASCII sum 
# of deleted characters to make two strings equal.
# Constraints:
#   1 <= s1.length, s2.length <= 1000
#   s1 and s2 consist of lowercase English letters.
from functools import cache

# DP + Recursion + Memo: O(M*N)
# This problem is similar to 1143 Longest Common Subsequence
# Analysis:
# - dp[i, j] is the minimum ascii del sum of s1[:i+1], s2[:j+1]
# - if the last characters of both strings are the same:
#       dp[i, j] = dp[i-1, j-1]
# - if not:
#       dp[i, j] = min(dp[i, j-1] + ord(s2[j]), dp[i-1, j] + ord(s1[i]), 
#                      dp[i-1, j-1] + ord(s1[i]) + ord(s2[j]))
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return dp(i, j-1) + ord(s2[j])
            if j < 0:
                return dp(i-1, j) + ord(s1[i])
            if s1[i] == s2[j]:
                return dp(i-1, j-1)
            return min(dp(i, j-1) + ord(s2[j]), dp(i-1, j) + ord(s1[i]),
                       dp(i-1, j-1) + ord(s1[i]) + ord(s2[j]))

        return dp(len(s1)-1, len(s2)-1)
        

if __name__ == "__main__":
    def unitTest(sol):
        r = sol.minimumDeleteSum(s1 = "sea", s2 = "eat")
        print(r)
        assert r == 231

        r = sol.minimumDeleteSum(s1 = "delete", s2 = "leet")
        print(r)
        assert r == 403

    unitTest(Solution())
