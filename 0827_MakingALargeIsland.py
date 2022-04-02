# You are given an n x n binary matrix grid. You are allowed to change
# at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.
# Constraints:
#   n == grid.length
#   n == grid[i].length
#   1 <= n <= 500
#   grid[i][j] is either 0 or 1.
from typing import List


# DFS - T/S: O(m*n), O(m*n)
# Analysis:
# - dfs to visit 1's cell, define islands, map every cell to island id,
#   also map island id to island size;
# - visit each 0's, check it's neighbouring islands, to see if it can
#   make some island larger or even connect more islands.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island_size = [0]
        island_id = 0
        island_map = [[-1]*n for _ in range(m)]

        def dfs_build_map(i, j):
            if grid[i][j] == 1 and island_map[i][j] == -1:
                island_map[i][j] = island_id
                island_size[island_id] += 1
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < m and 0 <= j1 < n:
                        dfs_build_map(i1, j1)
        
        for i in range(m):
            for j in range(n):
                if island_size[-1] > 0:
                    island_size.append(0)
                    island_id = len(island_size) - 1
                dfs_build_map(i, j)

        res = max(island_size)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    islands_to_connect = set()
                    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        i1, j1 = i + di, j + dj
                        if 0 <= i1 < m and 0 <= j1 < n and grid[i1][j1] == 1:
                            islands_to_connect.add(island_map[i1][j1])
                    res = max(res, sum(island_size[id] for id in islands_to_connect) + 1)
        
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.largestIsland([[1, 0], [0, 1]])
        print(r)
        assert r == 3

        r = sol.largestIsland([[1, 1], [1, 0]])
        print(r)
        assert r == 4

        r = sol.largestIsland([[1, 1], [1, 1]])
        print(r)
        assert r == 4

    unit_test(Solution())
