# You are given an m x n grid where each cell can have one of three values:
#   0 representing an empty cell,
#   1 representing a fresh orange, or
#   2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a 
# rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a 
# fresh orange. If this is impossible, return -1.
from typing import List
from collections import deque

# BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j, 0))

        res = 0
        while len(dq) > 0:
            i, j, res = dq.popleft()
            for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
                i1, j1 = i + di, j + dj
                if i1 >= 0 and i1 < m and j1 >= 0 and j1 < n \
                    and grid[i1][j1] == 1:
                    grid[i1][j1] = -1
                    dq.append((i1, j1, res + 1))

        res = -1 if any(x == 1 for y in grid for x in y) else res
        # for i in range(m):            # restore original state if necessary
        #     for j in range(n):
        #         if grid[i][j] == -1:
        #             grid[i][j] = 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.orangesRotting([[2,1,1],
                                [1,1,0],
                                [0,1,1]])
        print(r)
        assert r == 4

        r = sol.orangesRotting([[2,1,1],
                                [0,1,1],
                                [1,0,1]])
        print(r)
        assert r == -1

    unitTest(Solution())
