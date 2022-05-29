# You are given an m x n integer matrix grid where each cell is either
# 0 (empty) or 1 (obstacle). You can move up, down, left, or right
# from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner
# (0, 0) to the lower right corner (m - 1, n - 1) given that you can
# liminate at most k obstacles. If it is not possible to find such
# walk return -1.
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 40
#   1 <= k <= m * n
#   grid[i][j] is either 0 or 1.
#   grid[0][0] == grid[m - 1][n - 1] == 0
from collections import deque
from typing import List


# BFS - T/S: O(m*n*k), O(m*n*k)
# - allow re-visiting the cell, if its state (remaining quota) is different
# - similar but different to 2290_MinimumObstacleRemoval (Dijkstra's algorithm)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # enough quota to remove all obstacle in shortest path
        if k >= m + n - 3:
            return m + n - 2

        seen = set([(0, 0, k)])  # visited: i, j, quota
        dq = deque([[0, 0, 0, k]])  # i, j, steps, quota
        while dq:
            i, j, steps, quota = dq.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n:
                    if x == m - 1 and y == n - 1:
                        return steps + 1
                    q1 = quota - grid[x][y]
                    state = (x, y, q1)
                    if q1 >= 0 and not state in seen:
                        dq.append([x, y, steps + 1, q1])
                        seen.add(state)  # type: ignore

        return -1


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1)
        print(r)
        assert r == 6

        r = sol.shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1)
        print(r)
        assert r == -1

    unit_test(Solution())
