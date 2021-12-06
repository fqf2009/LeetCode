from typing import List
from collections import deque
import numpy as np

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#   - All the visited cells of the path are 0.
#   - All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Use numpy to simulate movement
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            if grid[0][0] == 0:
                return 1
            else:
                return -1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        mask = np.array(grid)
        arr = np.zeros_like(mask)
        arr[0, 0] = 1
        steps = 1
        while arr[n-1, n-1] == 0:
            steps += 1
            prev = arr.copy()
            arr[1:] += prev[:-1]
            arr[:-1] += prev[1:]
            arr[:, 1:] += prev[:, :-1]
            arr[:, :-1] += prev[:, 1:]
            arr[1:, 1:] += prev[:-1, :-1]
            arr[1:, :-1] += prev[:-1, 1:]
            arr[:-1, 1:] += prev[1:, :-1]
            arr[:-1, :-1] += prev[1:, 1:]
            arr[mask == 1] = 0
            if any(arr[prev == 0]):
                continue
            else:
                return -1

        return steps


# BFS (breadth first search) to get shortest path
class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            if grid[0][0] == 0:
                return 1
            else:
                return -1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        que = deque()
        que.append((0, 0))
        while len(que) > 0:
            i, j = que.popleft()
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    i1, j1 = i + di, j + dj
                    if i1 < 0 or i1 > n - 1 or j1 < 0 or j1 > n - 1:
                        continue
                    if grid[i1][j1] == 0:
                        grid[i1][j1] = grid[i][j] - 1
                        que.append((i1, j1))
                    if i1 == n - 1 and j1 == n - 1:
                        return -(grid[i1][j1] - 1)
        
        return -1


if __name__ == '__main__':
    sol = Solution()

    r = sol.shortestPathBinaryMatrix(grid= [[0,0,0,0,1],
                                            [1,0,0,0,0],
                                            [0,1,0,1,0],
                                            [0,0,0,1,1],
                                            [0,0,0,1,0]])
    print(r)
    assert(r == -1)

    r = sol.shortestPathBinaryMatrix(grid = [[0,1],[1,0]])
    print(r)
    assert(r == 2)

    r = sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]])
    print(r)
    assert(r == 4)

    r = sol.shortestPathBinaryMatrix(grid = [[1,0,0],
                                             [1,1,0],
                                             [1,1,0]])
    print(r)
    assert(r == -1)

    
    r = sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,1]])
    print(r)
    assert(r == -1)

    r = sol.shortestPathBinaryMatrix(grid = [[0]])
    print(r)
    assert(r == 1)