# Given two strings text1 and text2, return the length of their
# longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original 
# string with some characters (can be none) deleted without changing 
# the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common 
# to both strings.

# Constraints:
#  - 1 <= text1.length, text2.length <= 1000
#  - text1 and text2 consist of only lowercase English characters.

from functools import cache

# DP + Recursion + Memo: O(M*N)
# - dp[i, j] is the longest common subsequence for text1[:i+1], text1[:j+1]
# - if the last letters of both strings are the same:
#       dp[i, j] = dp[i-1, j-1] + 1
# - if not:
#       dp[i, j] = max(dp[i, j-1], dp[i-1, j], dp[i-1, j-1])
#   however, dp[i-1, j-1] is covered by dp[i, j-1] and dp[i-1, j] scenario,
#   so, dp[i, j] = max(dp[i, j-1], dp[i-1, j])
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i, j-1), dp(i-1, j))

        return dp(len(text1)-1, len(text2)-1)


# DP + Iteration - T/S: O(M*N), O(M*N)
class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[m][n]


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace")
        print(r)
        assert r == 3

        r = sol.longestCommonSubsequence(text1 = "abc", text2 = "abc")
        print(r)
        assert r == 3

        r = sol.longestCommonSubsequence(text1 = "abc", text2 = "def")
        print(r)
        assert r == 0


    unitTest(Solution())
    unitTest(Solution1())
