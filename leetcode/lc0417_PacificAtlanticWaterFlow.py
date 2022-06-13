# There is an m x n rectangular island that borders both the Pacific Ocean
# and Atlantic Ocean. The Pacific Ocean touches the island's left and top
# edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an
# m x n integer matrix heights where heights[r][c] represents the height
# above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to
# neighboring cells directly north, south, east, and west if the
# neighboring cell's height is less than or equal to the current
# cell's height. Water can flow from any cell adjacent to an ocean
# into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific
# and Atlantic oceans.
# Constraints:
#   m == heights.length
#   n == heights[r].length
#   1 <= m, n <= 200
#   0 <= heights[r][c] <= 10^5
from collections import deque
from typing import List


# BFS (Matrix): T/S: O(m*n), O(m*n)
# - from each ocean to visit other nodes, no need to return data,
#   only need to know reachable or not.
# - TLE
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pa_reachable, at_reachable = set(), set()
        pa_visited, at_visited = set(), set()
        pa_dq, at_dq = deque(), deque()

        def bfsVisit(dq: deque, reachable, visited):
            while dq:
                i, j = dq.popleft()
                # if (i, j) in visited: # why this cause error?
                #     return
                visited.add((i, j))
                reachable.add((i, j))
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and (not (x, y) in visited) and \
                            heights[x][y] >= heights[i][j]:
                        dq.append((x, y))

        for i in range(m):
            pa_dq.append((i, 0))
            bfsVisit(pa_dq, pa_reachable, pa_visited)
            at_dq.append((i, n - 1))
            bfsVisit(at_dq, at_reachable, at_visited)

        for j in range(n):
            pa_dq.append((0, j))
            bfsVisit(pa_dq, pa_reachable, pa_visited)
            at_dq.append((m - 1, j))
            bfsVisit(at_dq, at_reachable, at_visited)

        return [list(x) for x in pa_reachable & at_reachable]


# DFS (Matrix): T/S: O(m*n), O(m*n)
# - from each ocean to visit other nodes, no need to return data,
#   only need to know reachable or not.
class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pa_reachable, at_reachable = set(), set()
        pa_visited, at_visited = set(), set()

        def dfsVisit(i, j, reachable, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            reachable.add((i, j))
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    dfsVisit(x, y, reachable, visited)

        for i in range(m):
            dfsVisit(i, 0, pa_reachable, pa_visited)
            dfsVisit(i, n - 1, at_reachable, at_visited)

        for j in range(n):
            dfsVisit(0, j, pa_reachable, pa_visited)
            dfsVisit(m - 1, j, at_reachable, at_visited)

        return [list(x) for x in pa_reachable & at_reachable]


# DFS (Matrix): T/S: O(m*n), O(m*n)
# - Wrong!
# - From high to low, and, need the return value from lower nodes
#   However, when both nodes are in the same heights, either loop
#   endlessly, or set value prematurely.
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        grid = [[-1] * n for _ in range(m)]
        PACIFIC, ATLANTIC, BOTH_OCEANS = 1, 2, 3

        def dfsVisit(i, j) -> int:
            if grid[i][j] >= 0:  # to avoid endless recursion
                return grid[i][j]
            grid[i][j] = 0  # save value in grid, instead in other varialbe
            if i * j == 0:
                grid[i][j] |= PACIFIC
            if i == m - 1 or j == n - 1:
                grid[i][j] |= ATLANTIC
            if grid[i][j] != BOTH_OCEANS:
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and heights[x][y] <= heights[i][j]:
                        grid[i][j] |= dfsVisit(x, y)
            return grid[i][j]

        res = []
        for i in range(m):
            for j in range(n):
                if dfsVisit(i, j) == BOTH_OCEANS:
                    res.append([i, j])

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
        print(r)
        assert sorted(r) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

        r = sol.pacificAtlantic([[2, 1], [1, 2]])
        print(r)
        assert sorted(r) == [[0, 0], [0, 1], [1, 0], [1, 1]]

        heights = [[1,  2, 3, 4,5],
                   [16,17,18,19,6],
                   [15,24,25,20,7],
                   [14,23,22,21,8],
                   [13,12,11,10,9]]
        r = sol.pacificAtlantic(heights)
        print(r)
        assert sorted(r) == [[0,4],
                             [1,0],[1,1],[1,2],[1,3],[1,4],
                             [2,0],[2,1],[2,2],[2,3],[2,4],
                             [3,0],[3,1],[3,2],[3,3],[3,4],
                             [4,0],[4,1],[4,2],[4,3],[4,4]]

        heights = [
            [11, 3,  2,  4, 14,  6, 13, 18, 1, 4,  12, 2,  4,  1, 16],
            [5,  11, 18, 0, 15, 14, 6,  17, 2, 17, 19, 15, 12, 3, 14],
            [10, 2, 5, 13, 11, 11, 13, 19, 11, 17, 14, 18, 14, 3, 11],
            [14, 2, 10, 7, 5, 11, 6, 11, 15, 11, 6, 11, 12, 3, 11],
            [13, 1, 16, 15, 8, 2, 16, 10, 9, 9, 10, 14, 7, 15, 13],
            [17, 12, 4, 17, 16, 5, 0, 4, 10, 15, 15, 15, 14, 5, 18],
            [9, 13, 18, 4, 14, 6, 7, 8, 5, 5, 6, 16, 13, 7, 2],
            [19, 9, 16, 19, 16, 6, 1, 11, 7, 2, 12, 10, 9, 18, 19],
            [19, 5, 19, 10, 7, 18, 6, 10, 7, 12, 14, 8, 4, 11, 16],
            [13, 3, 18, 9, 16, 12, 1, 0, 1, 14, 2, 6, 1, 16, 6],
            [14, 1, 12, 16, 7, 15, 9, 19, 14, 4, 16, 6, 11, 15, 7],
            [6, 15, 19, 13, 3, 2, 13, 7, 19, 11, 13, 16, 0, 16, 16],
            [1, 5, 9, 7, 12, 9, 2, 18, 6, 12, 1, 8, 1, 10, 19],
            [10, 11, 10, 11, 3, 5, 12, 0, 0, 8, 15, 7, 5, 13, 19],
            [8, 1, 17, 18, 3, 6, 8, 15, 0, 9, 8, 8, 12, 5, 18],
            [8, 3, 6, 12, 18, 15, 10, 10, 12, 19, 16, 7, 17, 17, 1],
            [12, 13, 6, 4, 12, 18, 18, 9, 4, 9, 13, 11, 5, 3, 14],
            [8, 4, 12, 11, 2, 2, 10, 3, 11, 17, 14, 2, 17, 4, 7],
            [8, 0, 14, 0, 13, 17, 11, 0, 16, 13, 15, 17, 4, 8, 3],
            [18, 15, 8, 11, 18, 3, 10, 18, 3, 3, 15, 9, 11, 15, 15],
        ]
        r = sol.pacificAtlantic(heights)
        print(r)
        assert sorted(r) == [[0, 14], [1, 14], [2, 14], [3, 14], [4, 13], [4, 14], [5, 14], [19, 0]]


    unitTest(Solution())
    unitTest(Solution1())
