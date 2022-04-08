# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example 1:
#   Input: board = [["X","X","X","X"],
#                   ["X","O","O","X"],
#                   ["X","X","O","X"],
#                   ["X","O","X","X"]]
#   Output: [["X","X","X","X"],
#            ["X","X","X","X"],
#            ["X","X","X","X"],
#            ["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means
#              that any 'O' on the border of the board are not flipped to 'X'.
#              Any 'O' that is not on the border and it is not connected to
#              an 'O' on the border will be flipped to 'X'. Two cells are
#              connected if they are adjacent cells connected horizontally
#              or vertically.
#
# Note: Do not return anything, modify board in-place instead.
#
# Constraints:
#   m == board.length
#   n == board[i].length
#   1 <= m, n <= 200
#   board[i][j] is 'X' or 'O'.
from typing import List, Optional


# DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfsNotSurrounded(i, j):
            board[i][j] = 'N'
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                i1, j1 = i+di, j+dj
                if 0 <= i1 < m and 0 <= j1 < n and board[i1][j1] == 'O':
                    dfsNotSurrounded(i1, j1)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    dfsNotSurrounded(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'


if __name__ == '__main__':
    def unitTest(sol):
        board = [["X", "X", "X", "X"],
                 ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"],
                 ["X", "O", "X", "X"]]
        expected = [["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"]]
        sol.solve(board)
        print(board)
        assert board == expected

        board = [["X"]]
        expected = [["X"]]
        sol.solve(board)
        print(board)
        assert board == expected

        board = [["O"]]
        expected = [["O"]]
        sol.solve(board)
        print(board)
        assert board == expected

    unitTest(Solution())
