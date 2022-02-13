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
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i, j-1), dp(i-1, j), dp(i-1, j-1))

        return dp(len(text1)-1, len(text2)-1)


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
