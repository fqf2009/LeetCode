# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
# (i.e., return the area of the largest island.)
from typing import List

# BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        maxArea = 0
        que = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1     # mark visited before enqueue
                    que.append((i, j))
                area = 0
                while len(que) > 0:
                    r, c = que.pop()
                    area += 1
                    for dx, dy in delta:
                        r1, c1 = r + dy, c + dx
                        if (r1 >= 0 and r1 < m and c1 >= 0 and c1 < n and 
                            grid[r1][c1] == 1):
                            grid[r1][c1] = -1   # mark visited before enqueue
                            que.append((r1, c1))
                maxArea = max(maxArea, area)

        for i in range(m):
            for j in range(n):
                grid[i][j] = -grid[i][j]

        return maxArea


# DFS
class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfsArea(r: int, c: int, area: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return area
            grid[r][c] = -1
            area += 1
            delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
            for dx, dy in delta:
                r1, c1 = r + dy, c + dx
                area = dfsArea(r1, c1, area)
            return area

        maxArea = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, dfsArea(i, j, 0))

        for i in range(m):
            for j in range(n):
                grid[i][j] = -grid[i][j]

        return maxArea


if __name__ == "__main__":
    def unitTest(sol):
        grid = [[1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,0,1,1],
                [0,0,0,1,1]]
        r = sol.maxAreaOfIsland(grid)
        print(r)
        assert r == 4

        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        r = sol.maxAreaOfIsland(grid)
        print(r)
        assert r == 6

        grid = [[0,0,0,0,0,0,0,0]]
        r = sol.maxAreaOfIsland(grid)
        print(r)
        assert r == 0


    unitTest(Solution())
    unitTest(Solution1())
