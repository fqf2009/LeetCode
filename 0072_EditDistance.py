# Given two strings word1 and word2, return the minimum number 
# of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
#  - Insert a character
#  - Delete a character
#  - Replace a character

# Example 1:
#  - Input: word1 = "horse", word2 = "ros"
#  - Output: 3
#  - Explanation: 
#       horse -> rorse (replace 'h' with 'r')
#       rorse -> rose (remove 'r')
#       rose -> ros (remove 'e')

# Constraints:
#   0 <= word1.length, word2.length <= 500
#   word1 and word2 consist of lowercase English letters.

# DP - T/S: O(m*n), where m, n is length of s1 and s2
# - assume dp[i, j] is the minimum distance (operations) between
#   first i characters in s1 and first j characters in s2
# - dp[i, j] only depends on dp[i-1, j], dp[i, j-1] and dp[i-1, j-1]
# - if s1[i] == s2[j] (i.e. i-th char and j-th char, 1-based index),
#   dp[i, j] = min(dp[i-1, j] + 1, dp[i, j-1] + 1, dp[i-1, j-1]),
#   i.e., from dp[i-1, j-1], both add the same char, in other two
#   scenarios, need one more operation (either add or remove one char)
# - if s1[i] != s2[j] (i.e. i-th char and j-th char, 1-based index),
#   dp[i, j] = min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1,
#   i.e., all need one more operation (add, remove, or replace one char)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i

        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[m][n]


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.minDistance(word1 = "horse", word2 = "ros")
        print(r)
        assert r == 3

        r = sol.minDistance(word1 = "intention", word2 = "execution")
        print(r)
        assert r == 5

    unitTest(Solution())
