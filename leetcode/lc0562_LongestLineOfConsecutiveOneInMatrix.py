# Given an m x n binary matrix mat, return the length of
# the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal, or anti-diagonal.
# Constraints:
#   m == mat.length
#   n == mat[i].length
#   1 <= m, n <= 10^4
#   1 <= m * n <= 10^4
#   mat[i][j] is either 0 or 1.
from typing import List


# DP (Iteration): T/S: O(m*n), O(n), where m, n is row, col size of matrix
# - One solution is to travel 4 times: horizonal, vertical, diagonal, anti-diagonal
# - Better solution is to just travel row by row.
# - assume during the travel:
#   dp1[i, j] is the horizonal line length at the position i, j;
#   dp2[i, j] is the vertical ...
#   dp3[i, j] is the diagonal ...
#   dp4[i, j] is the anti-diagonal ...
# - the state transition formula (need to check index boundry):
#   dp1[i, j] = dp1[i, j-1] + 1 if mat[i, j] == 1 else 0
#   dp2[i, j] = dp1[i-1, j] + 1 if mat[i, j] == 1 else 0
#   dp3[i, j] = dp1[i-1, j-1] + 1 if mat[i, j] == 1 else 0
#   dp4[i, j] = dp1[i-1, j+1] + 1 if mat[i, j] == 1 else 0
# - dp only relies on the previous line's dp, the space can be optimized
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        dp = [[0]*n for _ in range(4)]      # (n item) * (4 counts) for each line
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[0][j] = dp[0][j-1] + 1 if j > 0 else 1       # horizonal
                    dp[1][j] = dp[1][j] + 1                         # vertical
                    dp[3][j] = dp[3][j+1] + 1 if j+1 < n else 1     # anti-diagonal
                else:
                    dp[0][j] = dp[1][j] = dp[3][j] = 0

                if mat[i][n-1-j] == 1:
                    # diagonal - iterate from right to left
                    dp[2][n-1-j] = dp[2][n-2-j] + 1 if n-1-j > 0 else 1
                else:
                    dp[2][n-1-j] = 0

            res = max(res, max(max(dp[k]) for k in range(4)))

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestLine([[0, 1, 0, 1, 1],
                             [1, 1, 0, 0, 1],
                             [0, 0, 0, 1, 0],
                             [1, 0, 1, 1, 1],
                             [1, 0, 0, 0, 1]])
        print(r)
        assert r == 3

        r = sol.longestLine([[0, 1, 1, 0],
                             [0, 1, 1, 0],
                             [0, 0, 0, 1]])
        print(r)
        assert r == 3

        r = sol.longestLine([[1, 1, 1, 1],
                             [0, 1, 1, 0],
                             [0, 0, 0, 1]])
        print(r)
        assert r == 4

    unitTest(Solution())
