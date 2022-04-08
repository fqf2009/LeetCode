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
