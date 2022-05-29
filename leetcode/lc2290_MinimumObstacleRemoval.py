# You are given a 0-indexed 2D integer array grid of size m x n.
# Each cell has one of two values:
# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.
# Return the minimum number of obstacles to remove so you can move
# from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 10^5
#   2 <= m * n <= 10^5
#   grid[i][j] is either 0 or 1.
#   grid[0][0] == grid[m - 1][n - 1] == 0
import heapq
from typing import List


# Dijkstra's algorithm - O(m*n*log(m*n))
# - Similar but different 1293_ShortestPathInGridWithObstaclesElimination (BFS)
# - treat entire grid as graph, with each cell as node, and
#   neighbor cells are connected.
# - cost of connecting to obstacle cell is 1, empty cell is 0
# - always starting from visited lowest cost cell to visit next
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hq = [[0, 0, 0]]  # cost, i, j
        grid[0][0] = 2  # visited
        heapq.heapify(hq)
        while hq:
            cost, i, j = heapq.heappop(hq)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 2:
                    if x == m - 1 and y == n - 1:
                        return cost
                    heapq.heappush(hq, [cost + grid[x][y], x, y])
                    grid[x][y] = 2

        return -1


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]])
        print(r)
        assert r == 2

        r = sol.minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]])
        print(r)
        assert r == 0

    unit_test(Solution())
