# According to Wikipedia's article: "The Game of Life, also known simply
# as Life, is a cellular automaton devised by the British mathematician 
# John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has 
# an initial state: live (represented by a 1) or dead (represented by a 0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, 
# diagonal) using the following four rules (taken from the above
# Wikipedia article):
#  - Any live cell with fewer than two live neighbors dies as if 
#    caused by under-population.
#  - Any live cell with two or three live neighbors lives on to 
#    the next generation.
#  - Any live cell with more than three live neighbors dies, as 
#    if by over-population.
#  - Any dead cell with exactly three live neighbors becomes a 
#    live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously 
# to every cell in the current state, where births and deaths occur 
# simultaneously. Given the current state of the m x n grid board, 
# return the next state.
# Constraints:
#   m == board.length
#   n == board[i].length
#   1 <= m, n <= 25
#   board[i][j] is 0 or 1.
# Follow up:
#  - Could you solve it in-place? Remember that the board needs to 
#    be updated simultaneously: You cannot update some cells first 
#    and then use their updated values to update other cells.
#  - In this question, we represent the board using a 2D array. In 
#    principle, the board is infinite, which would cause problems
#    when the active area encroaches upon the border of the array
#    (i.e., live cells reach the border). How would you address 
#    these problems? (A: use dict or map)
from copy import deepcopy
from typing import List


# T/S: O(m*n), O(1)
# - solve it in-place, use some special values to represent new states:
#   -1: previous live cell, now dead;
#   2: previous dead, now alive (reproduction);
# - change all negative to 0 and 2 to 1 at the end.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbours = sum(int(abs(board[x][y]) == 1)
                    for x in range(i-1, i+2) for y in range(j-1, j+2)
                    if 0 <= x < m and 0 <= y < n and not (x==i and y==j))
                if board[i][j] == 0:
                    if neighbours == 3:
                        board[i][j] = 2
                else:
                    if neighbours < 2 or neighbours > 3:
                        board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]),
            ([[1,1],[1,0]], [[1,1],[1,1]]),
        ])
        def test_gameOfLife(self, board, expected):
            sol = self.solution()       # type:ignore
            board1 = deepcopy(board)
            sol.gameOfLife(board1)
            self.assertEqual(board1, expected)

    main()
