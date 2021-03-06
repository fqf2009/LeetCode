# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands. An island is surrounded by 
# water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# Constraints
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 300
#   grid[i][j] is '0' or '1'.

from typing import List
from collections import deque


# Union Find - T/S: O(m*n), O(m*n)
# - good part is no need to mark grid for visited
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = {}
        def find(key):
            if key != uf.setdefault(key, key):
                uf[key] = find(uf[key])
            return uf[key]
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        x1, y1 = x + dx, y + dy
                        if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == '1':
                            uf[find((x1, y1))] = find((x, y))

        return len(set(find((x, y)) for x in range(m) for y in range(n) if grid[x][y] == '1'))


# DFS - T/S: O(m*n), O(k) where k is the size (area) of biggest island
# - the recursion level is k, therefore it is possible to cause stack overflow.
# - as long as the visited item can be marked, BFS/DFS will both work.
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfsVisit(i, j):
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "2"
                    dfsVisit(x, y)
        
        res = 0
        for i in range(m):        
            for j in range(n):
                if grid[i][j] == "1":
                    dfsVisit(i, j)
                    res += 1

        # restore grid if necessary
        return res


# BFS search, time complexity: O(m*n), space complexity: O(m+n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        que = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1': continue
                # Update it immediately, otherwise performance will suffer.
                # If the change is deferred until the moment of popup from bfs,
                # there will be too many duplicates in queue.
                grid[i][j] = str(-res - 1) # '-1', '-2', etc
                que.append((i, j))
                while len(que) > 0:
                    x, y = que.popleft()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        x1, y1 = x + dx, y + dy
                        if 0 <= x1 < m and 0 <= y1 < n:
                            if grid[x1][y1] == '1':
                                grid[x1][y1] = str(-res - 1) # update it immediately
                                que.append((x1, y1))
                res += 1

        for i in range(m):    # restore grid
            for j in range(n):
                if grid[i][j] != '0':
                    grid[i][j] = '1'
        return res


if __name__ == '__main__':
    def unitTest(solution):
        print(solution.__name__)
        sol = solution()

        grid = [['1','1','1','1','0'],
                ['1','1','0','1','0'],
                ['1','1','0','0','0'],
                ['0','0','0','0','0']]
        r = sol.numIslands(grid)
        print(r)
        assert(r == 1)

        grid = [['1','1','0','0','0'],
                ['1','1','0','0','0'],
                ['0','0','1','0','0'],
                ['0','0','0','1','1']]
        r = sol.numIslands(grid)
        print(r)
        assert(r == 3)

        grid = [['1','0','1'],
                ['0','1','0'],
                ['1','0','1']]
        r = sol.numIslands(grid)
        print(r)
        assert(r == 5)

        grid = [['1','1','1','1','1','0','1','1','1','1','1','1','1','1','1','0','1','0','1','1'],
                ['0','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','0'],
                ['1','0','1','1','1','0','0','1','1','0','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','0','1','1','1','1','1','1','0','1','1','1','0','1','1','1','0','1','1','1'],
                ['0','1','1','1','1','1','1','1','1','1','1','1','0','1','1','0','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','0','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['0','1','1','1','1','1','1','1','0','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','0','1','1','1','1','1','1','1','0','1','1','1','1','1','1'],
                ['1','0','1','1','1','1','1','0','1','1','1','0','1','1','1','1','0','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','1','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]
        r = sol.numIslands(grid)
        print(r)
        assert(r == 1)

    unitTest(Solution)
    unitTest(Solution1)
    unitTest(Solution2)
