# There is an n x n 0-indexed grid with some artifacts buried in it. You are given the 
# integer n and a 0-indexed 2D integer array artifacts describing the positions of the 
# rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith 
# artifact is buried in the subgrid where:
#   (r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
#   (r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
# You will excavate some cells of the grid and remove all the mud from them. If the cell 
# has a part of an artifact buried underneath, it will be uncovered. If all the parts of 
# an artifact are uncovered, you can extract it.
#
# Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will 
# excavate the cell (ri, ci), return the number of artifacts that you can extract.
# The test cases are generated such that:
#   No two artifacts overlap.
#   Each artifact only covers at most 4 cells.
#   The entries of dig are unique.
#
# Constraints:
#   1 <= n <= 1000
#   1 <= artifacts.length, dig.length <= min(n2, 105)
#   artifacts[i].length == 4
#   dig[i].length == 2
#   0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1
#   r1i <= r2i
#   c1i <= c2i
#   No two artifacts will overlap.
#   The number of cells covered by an artifact is at most 4.
#   The entries of dig are unique.
from typing import List


# Time:  O(N+A) where N is number of cells with artifact, N <= n^2
# Space: O(A)   where A is number of artifact
# Set is enough!!!
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        digSet = {tuple(d)  for d in dig}
        res = 0
        for x1, y1, x2, y2 in artifacts:
            digged = True
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) not in digSet:
                        digged = False
                        break
                if not digged:
                    break
            res += 1 if digged else 0

        return res


# DFS - T/S: O(n^2), O(n^2)
# To make code more clear, use several 2D array, instead 3D array
class Solution1:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)]      # store artifactid
        digged = [[0] * n for _ in range(n)]  
        visited = [[0] * n for _ in range(n)]

        aid = 0
        for x1, y1, x2, y2 in artifacts:
            aid += 1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] = aid

        for x, y in dig:
            digged[x][y] = 1

        def dfsCount(x, y):
            res = digged[x][y]
            visited[x][y] = 1
            aid = grid[x][y]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n and 0 <= y1 < n:
                    if grid[x1][y1] == aid and visited[x1][y1] == 0:
                        res *= dfsCount(x1, y1)    # if any cell is not digged, will make res to 0
            return res

        res = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] > 0 and visited[x][y] == 0:
                    res += dfsCount(x, y)

        return res


# DFS - T/S: O(n^2), O(n^2)
class Solution2:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]  # [artifactid, digged, visited]
        aid = 0
        for x1, y1, x2, y2 in artifacts:
            aid += 1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y][0] = aid

        for x, y in dig:
            grid[x][y][1] = 1

        def dfsCount(x, y):
            res = grid[x][y][1]
            grid[x][y][2] = 1
            aid = grid[x][y][0]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n and 0 <= y1 < n:
                    if grid[x1][y1][0] == aid and grid[x1][y1][2] == 0:
                        res *= dfsCount(x1, y1)
            return res

        res = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y][0] > 0 and grid[x][y][2] == 0:
                    res += dfsCount(x, y)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.digArtifacts(6, [[0, 2, 0, 5], [0, 1, 1, 1], [3, 0, 3, 3], [4, 4, 4, 4], [2, 1, 2, 4]],
                             [[0, 2], [0, 3], [0, 4], [2, 0], [2, 1], [2, 2], [2, 5], [3, 0], [3, 1],
                              [3, 3], [3, 4], [4, 0], [4, 3], [4, 5], [5, 0], [5, 1], [5, 2], [5, 4], [5, 5]])
        print(r)
        assert r == 0

        r = sol.digArtifacts(5, [[3, 1, 4, 1], [1, 1, 2, 2], [1, 0, 2, 0], [4, 3, 4, 4],
                                 [0, 3, 1, 4], [2, 3, 3, 4]],
                             [[0, 0], [2, 1], [2, 0], [2, 3], [4, 3], [2, 4], [4, 1], [0, 2],
                              [4, 0], [3, 1], [1, 2], [1, 3], [3, 2]])
        print(r)
        assert r == 1

        r = sol.digArtifacts(n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1]])
        print(r)
        assert r == 1

        r = sol.digArtifacts(n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1], [1, 1]])
        print(r)
        assert r == 2

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
