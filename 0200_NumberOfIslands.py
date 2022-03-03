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
        

# DFS - Not practical, it will actually be backtracking, very time consuming
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
            pass
            return 0


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
    grid = [['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']]
    r = Solution().numIslands(grid)
    print(r)
    assert(r == 1)

    grid = [['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']]
    r = Solution().numIslands(grid)
    print(r)
    assert(r == 3)

    grid = [['1','0','1'],
            ['0','1','0'],
            ['1','0','1']]
    r = Solution().numIslands(grid)
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
    r = Solution().numIslands(grid)
    print(r)
    # for x in grid:
    #     print(x)
    assert(r == 1)
