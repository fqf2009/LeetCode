# Given an m x n integers matrix, return the length of the longest increasing path
# in matrix. From each cell, you can either move in four directions: left, right,
# up, or down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
from typing import List
from functools import cache


# Use cache decorator to simplify the code
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def findLongestPath(i, j) -> int:
            depth = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    depth = max(depth, findLongestPath(x, y) + 1)
            return depth

        m, n = len(matrix), len(matrix[0])
        maxPath = 0
        for i in range(m):
            for j in range(n):
                maxPath = max(maxPath, findLongestPath(i, j))

        return maxPath


# DFS + DP + Memo
class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findLongestPath(i, j) -> int:
            if dp[i][j] > 0:
                return dp[i][j]
            depth = 1
            m, n = len(matrix), len(matrix[0])
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    d = findLongestPath(x, y)
                    depth = max(depth, d + 1)
            dp[i][j] = depth
            return depth

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxPath = 0
        for i in range(m):
            for j in range(n):
                maxPath = max(maxPath, findLongestPath(i, j))

        return maxPath


if __name__ == "__main__":
    def unit_test(sol):
        r = sol.longestIncreasingPath(matrix=[[9, 9, 4], 
                                              [6, 6, 8], 
                                              [2, 1, 1]])
        print(r)
        assert (r == 4)

        r = sol.longestIncreasingPath(matrix=[[3, 4, 5], 
                                              [3, 2, 6], 
                                              [2, 2, 1]])
        print(r)
        assert (r == 4)

    unit_test(Solution())
    unit_test(Solution1())
