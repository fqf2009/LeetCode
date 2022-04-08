# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many 
# unique paths would there be?
# An obstacle and space is marked as 1 and 0 respectively in the grid.
# Constraints:
#   1 <= m, n <= 100
#   obstacleGrid[i][j] is 0 or 1.
from typing import List
import numpy as np
from collections import deque
from functools import cache


# DP + Recursion + Memo
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0: return 0
            if i == 0 and j == 0: return 1
            if grid[i][j] == 1: return 0
            return dp(i-1, j) + dp(i, j-1)

        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1: return 0
        if m*n == 1: return 1
        return dp(m-1, n-1)


# DP (Dynamic Programming) - T/S: O(m*n), O(1)
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        if m*n == 1:
            return 1
        grid[0][0] = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                if i > 0 and grid[i-1][j] < 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0 and grid[i][j-1] < 0:
                    grid[i][j] += grid[i][j-1]

        res = -grid[m-1][n-1]
        # restore grid if necessary
        return res


# BFS using NumPy
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        if m*n == 1:
            return 1
        grid = np.zeros((m, n), dtype=object)
        mask = np.array(obstacleGrid, dtype=object)
        grid[0, 0] = 1
        res = 0
        while True:
            prev = grid.copy()
            grid = prev - prev
            grid[1:] += prev[:-1]
            grid[:, 1:] += prev[:, :-1]
            grid[mask == 1] = 0
            res += grid[m - 1, n - 1]
            if np.any(grid):
                continue

            return res


# BFS - save path number in grid
class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        if m*n == 1:
            return 1
        que = deque()
        que.append((0,0))
        grid[0][0] = -1
        res = 0
        while len(que) > 0:
            i, j = que.popleft()
            if grid[i][j] == 0:
                continue
            if i + 1 < m and grid[i + 1][j] != 1:
                grid[i + 1][j] += grid[i][j]
                que.append((i + 1, j))
            if j + 1 < n and grid[i][j + 1] != 1:
                grid[i][j + 1] += grid[i][j]
                que.append((i, j + 1))
            grid[i][j] = 0
            if grid[m-1][n-1] != 0:
                res -= grid[m-1][n-1]
                grid[m-1][n-1] = 0

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0,0,0],
                                                        [0,0,1,0,0],
                                                        [0,0,0,0,0],
                                                        [0,0,0,0,0]])
        print(r)
        assert (r == 17)

        r = sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]])
        print(r)
        assert (r == 2)

        r = sol.uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]])
        print(r)
        assert (r == 1)

        r = sol.uniquePathsWithObstacles(obstacleGrid = [[1,0]])
        print(r)
        assert (r == 0)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
