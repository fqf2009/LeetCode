# Given an m x n matrix grid where each cell is either a wall 'W', 
# an enemy 'E' or empty '0', return the maximum enemies you can kill 
# using one bomb. You can only place the bomb in an empty cell.

# The bomb kills all the enemies in the same row and column from the 
# planted point until it hits the wall since it is too strong to be 
# destroyed.

# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 500
#   grid[i][j] is either 'W', 'E', or '0'.
from typing import List


# DP - T/S: O(m*n), O(m*n)
# the code can be optimized to reduce code duplicate
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp1 = [[0]*n for _ in range(m)]     # left to right
        dp2 = [[0]*n for _ in range(m)]     # right to left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W': continue
                if grid[i][j] == 'E':
                    dp1[i][j] = 1
                if j - 1 >= 0:
                    dp1[i][j] += dp1[i][j-1]
            for j in reversed(range(n)):
                if grid[i][j] == 'W': continue
                if grid[i][j] == 'E':
                    dp2[i][j] = 1
                if j + 1 < n:
                    dp2[i][j] += dp2[i][j+1]

        dp3 = [[0]*n for _ in range(m)]     # top to bottom
        dp4 = [[0]*n for _ in range(m)]     # bottom to top
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 'W': continue
                if grid[i][j] == 'E':
                    dp3[i][j] = 1
                if i - 1 >= 0:
                    dp3[i][j] += dp3[i-1][j]
            for i in reversed(range(m)):
                if grid[i][j] == 'W': continue
                if grid[i][j] == 'E':
                    dp4[i][j] = 1
                if i + 1 < m:
                    dp4[i][j] += dp4[i+1][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, dp1[i][j] + dp2[i][j] + dp3[i][j] + dp4[i][j])
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxKilledEnemies([["0","E","0","0"],
                                  ["E","0","W","E"],
                                  ["0","E","0","0"]])
        print(r)
        assert r == 3

        r = sol.maxKilledEnemies([["W","W","W"],
                                  ["0","0","0"],
                                  ["E","E","E"]])
        print(r)
        assert r == 1

    unitTest(Solution())        
