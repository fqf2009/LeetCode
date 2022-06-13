# You are given a map of a server center, represented as a m * n
# integer matrix grid, where 1 means that on that cell there is a
# server and 0 means that it is no server. Two servers are said to
# communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m <= 250
#   1 <= n <= 250
#   grid[i][j] == 0 or 1
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    res += 1

        return res


class Solution1:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        R = list(map(sum, grid))
        C = list(map(sum, zip(*grid)))
        return sum(R[i] + C[j] > 2 for i in range(m) for j in range(n)
                    if grid[i][j] == 1 )


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.countServers([[1, 0], [0, 1]])
        print(r)
        assert r == 0

        r = sol.countServers([[1, 0], [1, 1]])
        print(r)
        assert r == 3

        r = sol.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        print(r)
        assert r == 4

    unit_test(Solution())
    unit_test(Solution1())
