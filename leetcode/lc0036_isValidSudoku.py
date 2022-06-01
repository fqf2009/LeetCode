# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to 
# be validated according to the following rules:
#  - Each row must contain the digits 1-9 without repetition.
#  - Each column must contain the digits 1-9 without repetition.
#  - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#  - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#  - Only the filled cells need to be validated according to the mentioned rules.
# Constraints:
#   board.length == 9
#   board[i].length == 9
#   board[i][j] is a digit 1-9 or '.'.
from typing import List


# Simplify by encoding
class Solution0:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    row = f"R{i}={val}"
                    col = f"C{j}={val}"
                    grid = f"G{i//3}{j//3}={val}"
                    if row in seen or col in seen or grid in seen:
                        return False
                    seen |= {row, col, grid}
        return True


# Array
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_piece(piece: list[str]) -> bool:
            filled = [False] * 9
            for v in piece:
                if v != '.':
                    idx = int(v) - 1
                    if filled[idx]: return False
                    filled[idx] = True
            return True

        for r in board:
            if not is_valid_piece(r):
                return False
        
        for j in range(9):
            piece = [board[i][j] for i in range(9)]
            if not is_valid_piece(piece):
                return False

        for i in range(3):
            for j in range(3):
                piece = [board[i*3 + x][j*3 +y] for x in range(3) for y in range(3)]
                if not is_valid_piece(piece):
                    return False

        return True


# Hash Set
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_piece(piece: list[str]) -> bool:
            filled = [v for v in piece if v != '.']
            return len(set(filled)) == len(filled)

        for r in board:
            if not is_valid_piece(r):
                return False
        
        for j in range(9):
            piece = [board[i][j] for i in range(9)]
            if not is_valid_piece(piece):
                return False

        for i in range(3):
            for j in range(3):
                piece = [board[i*3 + x][j*3 +y] for x in range(3) for y in range(3)]
                if not is_valid_piece(piece):
                    return False
        
        return True


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution0,), (Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], True),
            ([["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], False),
        ])
        def test_isValidSudoku(self, board, expected):
            sol = self.solution()       # type:ignore
            r = sol.isValidSudoku(board)
            self.assertEqual(r, expected)

    main()
