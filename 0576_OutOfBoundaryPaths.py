import numpy as np

# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
# You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of 
# the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move 
# the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

# Use numpy to simulate the move. In essense, this is the same as DP (dynamic programming) approach
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = np.zeros((m, n), dtype=np.int64)
        mod = 10**9 + 7
        grid[startRow, startColumn] = 1
        res = 0
        for _ in range(maxMove):
            prev = grid % mod
            grid = prev - prev
            grid[1:] += prev[:-1]
            grid[:-1] += prev[1:]
            grid[:, 1:] += prev[:, :-1]
            grid[:, :-1] += prev[:, 1:]
            res += np.sum(prev) * 4 - np.sum(grid)
            res %= mod

        return res


if __name__ == '__main__':
    sol = Solution()

    r = sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0)
    print(r)
    assert(r == 6)

    r = sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1)
    print(r)
    assert(r == 12)
