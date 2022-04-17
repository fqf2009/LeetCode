# Given an n x n binary matrix grid, return the length of the shortest clear path
# in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) 
# to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#  - All the visited cells of the path are 0.
#  - All the adjacent cells of the path are 8-directionally connected (i.e., they 
#    are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
from typing import List
from collections import deque
import numpy as np


# Use numpy to simulate movement
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        mask = np.array(grid)
        arr = np.zeros_like(mask)
        arr[0, 0] = 1
        steps = 1           # the length of path
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
            if any(arr[prev == 0]): # any cell previously is zero, now is not
                continue
            else:                   # not cell changes from zero to non-zero
                return -1

        return steps


# BFS (breadth first search) to get shortest path
class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        que = deque([[0, 0]])
        while que:
            i, j = que.popleft()
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0: continue
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < n:
                        if grid[i1][j1] == 0:
                            grid[i1][j1] = grid[i][j] - 1
                            que.append([i1, j1])
                        if i1 == j1 == n - 1: return -(grid[i1][j1] - 1)  # the length of path, not steps

        return -1


if __name__ == '__main__':
    def unitTest(sol):
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

    unitTest(Solution())
    unitTest(Solution1())
