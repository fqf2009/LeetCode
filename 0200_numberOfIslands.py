from typing import List
from collections import deque

# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands. An island is surrounded by 
# water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# BFS search, time complexity: O(m*n), space complexity: O(m+n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        bfs = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1': continue
                # Update it immediately, otherwise performance will suffer.
                # If the change is deferred until the moment of popup from bfs,
                # there will be too many duplicates in bfs.
                grid[i][j] = str(-res - 1) # '-1' 
                bfs.append((i, j))
                while len(bfs) > 0:
                    a, b = bfs.popleft()
                    for c, d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        p, q = a + c, b + d
                        if p >= 0 and p < m and q >= 0 and q < n:
                            if grid[p][q] == '1':
                                grid[p][q] = str(-res - 1) # '-1' # update it immediately
                                bfs.append((p, q))
                res += 1
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] != '0'
        #             grid[i][j] = '1'

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