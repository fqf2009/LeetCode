# You are given an m x n integer matrix grid, where you can move from a cell
# to any adjacent cell in all 4 directions.
# Return the number of strictly increasing paths in the grid such that you can
# start from any cell and end at any cell. Since the answer may be very large,
# return it modulo 109 + 7.
# Two paths are considered different if they do not have exactly the same 
# sequence of visited cells.
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 1000
#   1 <= m * n <= 10^5
#   1 <= grid[i][j] <= 10^5
from functools import cache
from typing import List


# DFS + DP - T/S: O(m*n), O(m*n)
# - let dp[i][j] be the number of strictly increasing pathes starting
#   from cell grid[i][j].
# - Set initial dp[i][j] to be 0, also means not visited.
# - State transition formula:
#       dp[i][j] = 1 + sum(dp[x][y]),
#           where dp[x][y] are pathes of 4 neighbour cells.
# - when dp[i][j] > 0, it also means visited + memo, to avoid re-calculation
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7
        dp = [[0] * n for _ in range(m)]

        def dfs_count(i, j):
            if dp[i][j] > 0:        # memo + visited
                return dp[i][j]
            dp[i][j] = 1
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    dp[i][j] += dfs_count(x, y)
            return dp[i][j] % mod

        for i in range(m):
            for j in range(n):
                dfs_count(i, j)

        return sum(sum(x) for x in dp) % mod


# DFS + DP - T/S: O(m*n), O(m*n)
# - to simplify code
class Solution1:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7

        @cache
        def dfs_count(i, j):
            res = 1
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res += dfs_count(x, y)
            return res % mod

        return sum(dfs_count(i, j) for i in range(m) for j in range(n)) % mod


# !!! Wrong - because the formula is not about pathes "starting form certain cell";
#             it is about pathes "starting form any cell in the path";
#             it is possible that part of the path will be re-used by other path, 
#             and leads to duplicate counting.
# DFS traversal always from smallest value to highest value,
# - pathes = (n_cells_in_path - 1) * n_cells_in_path // 2
class Solution2:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7

        def dfs_count(i, j, cnt):
            res = 0
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res += dfs_count(x, y, cnt + 1)
            if res == 0 and cnt > 0:
                res = (cnt + 1) * cnt // 2
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                        break
                else:
                    res += dfs_count(i, j, 0)

        return (res + m * n) % mod


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.countPaths([[1, 1, 1], [3, 2, 5], [4, 3, 4]])
        print(r)
        assert r == 32

        r = sol.countPaths([[1, 1], [3, 4]])
        print(r)
        assert r == 8

        r = sol.countPaths([[1], [2]])
        print(r)
        assert r == 3

        grid = [
            [73884, 15322, 92124, 16515, 54702, 88526, 61879, 14125, 21161, 42701, 35686, 75932, 8696],
            [59537, 80396, 65708, 32310, 46753, 39759, 4746, 71413, 84723, 13233, 23640, 62230, 11825],
            [6414, 96122, 64501, 32523, 55259, 2935, 44772, 48912, 26516, 56256, 69201, 21079, 52979],
            [50951, 1748, 42645, 73435, 81511, 21445, 26066, 27605, 40388, 43702, 47233, 15333, 86291],
            [87914, 90237, 95947, 97341, 93670, 79822, 32591, 44096, 55112, 89104, 36097, 82759, 15504],
            [3604, 74013, 74414, 68295, 58798, 7050, 71657, 33463, 38040, 46180, 61730, 82754, 57179],
            [86867, 1972, 13704, 11581, 99042, 24825, 77747, 38671, 40628, 38626, 54719, 7366, 36309],
            [69272, 98273, 16474, 15204, 40263, 99956, 36072, 68173, 77076, 18094, 97439, 61968, 7435],
            [95263, 39616, 37983, 61376, 256, 7169, 45149, 94957, 66151, 13256, 37776, 25331, 29659],
            [90001, 12571, 31093, 46714, 52347, 44882, 76055, 53662, 69928, 37486, 44020, 2211, 67466],
        ]
        r = sol.countPaths(grid)
        print(r)
        assert r == 925

    unit_test(Solution())
    unit_test(Solution1())
