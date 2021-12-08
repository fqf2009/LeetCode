from typing import List

# Given an m x n integers matrix, return the length of the longest increasing path
# in matrix. From each cell, you can either move in four directions: left, right, 
# up, or down. You may not move diagonally or move outside the boundary (i.e., 
# wrap-around is not allowed).

# DFS (Depth First Search) and DP (Dynamic Programming)
# Runtime: 416 ms, faster than 89.17% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 15 MB, less than 81.46% of Python3 online submissions for Longest Increasing Path in a Matrix.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findLongestPath(i, j, depth) -> int:
            if dp[i][j] > 0:
                return dp[i][j]
            m, n = len(matrix), len(matrix[0])
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x, y = i + di, j + dj
                if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] > matrix[i][j]:
                    # dfs, when next number is increasing
                    d = findLongestPath(x, y, 1)
                    depth = max(depth, d + 1)
            dp[i][j] = depth
            return depth

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxPath = 0
        for i in range(m):
            for j in range(n):
                maxPath = max(maxPath, findLongestPath(i, j, 1))

        return maxPath


if __name__ == "__main__":
    sol = Solution()

    r = sol.longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]])
    print(r)
    assert (r == 4)

    r = sol.longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]])
    print(r)
    assert (r == 4)


    