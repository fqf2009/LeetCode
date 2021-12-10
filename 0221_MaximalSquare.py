from typing import List

# Given an m x n binary matrix filled with 0's and 1's, find 
# the largest square containing only 1's and return its area.

# DP (Dynamic Programing): O(m*n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(m)]
        maxEdge = 0
        for i in range(m):
            for j in range(n):
                v = int(matrix[i][j])
                if i == 0 or j == 0 or v == 0:
                    dp[i][j] = v
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + v
                maxEdge = max(maxEdge, dp[i][j])

        return maxEdge*maxEdge


if __name__ == '__main__':
    sol = Solution()

    matrix = [["1","0","1","1","0","1"],
              ["1","1","1","1","1","1"],
              ["0","1","1","0","1","1"],
              ["1","1","1","0","1","0"],
              ["0","1","1","1","1","1"],
              ["1","1","0","1","1","1"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 4)

    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], 
              ["1", "0", "0", "1", "0"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 4)

    matrix = matrix = [["0","1"],["1","0"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 1)

    matrix = [["0"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 0)

    matrix = [["1"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 1)

    matrix = [["0", "0"]]
    r = sol.maximalSquare(matrix)
    print(r)
    assert(r == 0)
