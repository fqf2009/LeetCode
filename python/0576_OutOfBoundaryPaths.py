# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
# You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of 
# the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move 
# the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
# Constraints:
#   1 <= m, n <= 50
#   0 <= maxMove <= 50
#   0 <= startRow < m
#   0 <= startColumn < n
import numpy as np


# DP: O(k*m*n), where k is maxMove
# - Note to use two arrays to avoid duplicate counting.
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = [[0]*n for _ in range(m)]
        mod = 10**9 + 7
        grid[startRow][startColumn] = 1
        prevInGrid, res = 1, 0
        for _ in range(maxMove):
            dp = [[0]*n for _ in range(m)]  # new array each time
            inGrid = 0
            for i in range(m):
                for j in range(n):
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        i1, j1 = i + di, j + dj
                        if 0 <= i1 < m and 0 <= j1 < n:
                            dp[i][j] += grid[i1][j1]
                    inGrid += dp[i][j]
            res += prevInGrid*4 - inGrid
            prevInGrid = inGrid
            grid = dp

        return res % mod


# Use numpy to simulate the move: O(k*m*n), where k is maxMove
# - In essense, this is the same as BFS/DP approach
class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = np.zeros((m, n), dtype=np.int64)
        mod = 10**9 + 7
        grid[startRow, startColumn] = 1
        res = 0
        for _ in range(maxMove):
            prev = grid % mod
            grid = prev - prev
            grid[1:] += prev[:-1]
            grid[:-1] += prev[1:]
            grid[:, 1:] += prev[:, :-1]
            grid[:, :-1] += prev[:, 1:]
            res += np.sum(prev) * 4 - np.sum(grid)
            res %= mod

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0)
        print(r)
        assert r == 6

        r = sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1)
        print(r)
        assert r == 12
        
        r = sol.findPaths(m=8, n=50, maxMove=23, startRow=5, startColumn=26)
        print(r)
        assert r == 914783380

    unitTest(Solution())
    unitTest(Solution1())

    
