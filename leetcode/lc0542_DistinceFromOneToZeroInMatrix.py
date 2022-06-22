# Given an m x n binary matrix mat, return the distance
# of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Constraints:
#   m == mat.length
#   n == mat[i].length
#   1 <= m, n <= 10^4
#   1 <= m * n <= 10^4
#   mat[i][j] is either 0 or 1.
#   There is at least one 0 in mat.

from typing import List
from collections import deque

# BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dis = [[0]*n for _ in range(m)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0: continue
                for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
                    i1, j1 = i + di, j + dj
                    if i1 >= 0 and i1 < m and j1 >= 0 and j1 < n and mat[i1][j1] == 1:
                        dis[i1][j1] = 1
                        dq.append((i1, j1))
                        
        while len(dq) > 0:
            i, j = dq.popleft()
            for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
                i1, j1 = i + di, j + dj
                d = dis[i][j]
                if i1 >= 0 and i1 < m and j1 >= 0 and j1 < n \
                    and mat[i1][j1] == 1 and dis[i1][j1] == 0:
                    dis[i1][j1] = d + 1
                    dq.append((i1, j1))

        return dis


# BFS
class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1]*n for _ in range(m)]    # also act as visited[][]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append([i, j, 0])
        
        while dq:
            i, j, dist = dq.popleft()
            if res[i][j] >= 0: continue # visited
            res[i][j] = dist
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and res[x][y] < 0:
                    dq.append([x, y, dist+1])
        
        return res


# BFS
# - slightly different, actually faster
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1]*n for _ in range(m)]    # also act as visited[][]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append([i, j])
                    res[i][j] = 0

        while dq:
            i, j = dq.popleft()
            dist = res[i][j]
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and res[x][y] < 0:
                    res[x][y] = dist + 1
                    dq.append([x, y])
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.updateMatrix([[0,0,0],
                              [0,1,0],
                              [0,0,0]])
        print(r)
        assert r == [[0,0,0],
                     [0,1,0],
                     [0,0,0]]

        r = sol.updateMatrix([[0,0,0],
                              [0,1,0],
                              [1,1,1]])
        print(r)
        assert r == [[0,0,0],
                     [0,1,0],
                     [1,2,1]]

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
