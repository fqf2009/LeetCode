# You are given an n x n integer matrix grid where each value grid[i][j]
# represents the elevation at that point (i, j).
# The rain starts to fall. At time t, the depth of the water everywhere
# is t. You can swim from a square to another 4-directionally adjacent
# square if and only if the elevation of both squares individually are
# at most t. You can swim infinite distances in zero time. Of course,
# you must stay within the boundaries of the grid during your swim.
# Return the least time until you can reach the bottom right square
# (n - 1,  n - 1) if you start at the top left square (0, 0).
# Constraints:
#   n == grid.length
#   n == grid[i].length
#   1 <= n <= 50
#   0 <= grid[i][j] < n^2
#   Each value grid[i][j] is unique.
import heapq
from typing import List


# BFS + PriorityQueue (heapq)
# - T/S: O(n^2*log(n)), O(n^2)
#   why log(n) not log(n^2), think about items in queue as perimeter
#   of the visited items (area), not the items themself (area).
#   also, log(n^2) = 2*log(n)
# - BFS need a queue, but this time use PriorityQueue, i.e.,
#   always visit next cell with min elevation.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(grid[0][0], 0, 0)]
        grid[0][0] = - grid[0][0] - 1
        heapq.heapify(queue)
        res = 0
        while queue:
            time, i, j = heapq.heappop(queue)
            res = max(res, time)
            if i == n-1 and j == n-1: break
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and grid[x][y] >= 0:
                    heapq.heappush(queue, (grid[x][y], x, y))  # type: ignore
                    grid[x][y] = - grid[x][y] -1

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.swimInWater([[0, 2], [1, 3]])
        print(r)
        assert r == 3

        r = sol.swimInWater(
            [[0, 1, 2, 3, 4], 
            [24, 23, 22, 21, 5], 
            [12, 13, 14, 15, 16], 
            [11, 17, 18, 19, 20], 
            [10, 9, 8, 7, 6]]
        )
        print(r)
        assert r == 16

    unit_test(Solution())
