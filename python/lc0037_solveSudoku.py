from typing import List
from pprint import pprint

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#  - Each of the digits 1-9 must occur exactly once in each row.
#  - Each of the digits 1-9 must occur exactly once in each column.
#  - Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Backtracking
# Note: - to further improve performance, the number of backtracking should be reduced.
#         first, compute all available digits for each cell, and sort by the number of
#         available digits, then start from the cell with fewer number of available digits.
## Performance:
## %%timeit
## %run 0037_solveSudoku.py
## 8.52 ms ± 493 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def availableDigits(i):
            block = ( board[i//9] + 
                      [board[x][i % 9] for x in range(9)] + 
                      [board[((i//9)//3)*3 + x][((i%9)//3)*3 + y] for x in range(3) for y in range(3)]
                    )
            return set(range(1, 10)) - set([int(x) for x in block if x != '.'])

        fillablePos = sorted([(len(availableDigits(i)), i) for i in range(81) if board[i // 9][i % 9] == '.'])
        j = 0
        while j >= 0 and j < len(fillablePos):
            i = fillablePos[j][1]
            k = (1 if board[i // 9][i % 9] == '.'
                   else int(board[i // 9][i % 9]) + 1
                )
            available = availableDigits(i)
            for v in range(k, 10):
                if v in available:
                    board[i // 9][i % 9] = '0' + str(v)
                    j += 1
                    break
            else:
                board[i // 9][i % 9] = '.'
                j -= 1

        for i in range(81):
            if board[i // 9][i % 9][:1] == '0':
                board[i // 9][i % 9] = str(int(board[i // 9][i % 9]))



# Backtracking
# Note: - to improve performance, only try digits available for a cell and avoid valiation
## Performance:
## %%timeit
## %run 0037_solveSudoku.py
## 160 ms ± 4.07 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def nextPos(p):
            for i in range(p, 81):
                if board[i // 9][i % 9] == '.':
                    return i
            return -1

        def prevPos(p):
            for i in reversed(range(0, p)):
                if board[i // 9][i % 9][0] == '0':
                    return i
            return -1

        i = nextPos(0)
        while i >= 0:
            k = (1 if board[i // 9][i % 9] == '.'
                   else int(board[i // 9][i % 9]) + 1
                )
            block = ( board[i//9] + 
                      [board[x][i % 9] for x in range(9)] + 
                      [board[((i//9)//3)*3 + x][((i%9)//3)*3 + y] for x in range(3) for y in range(3)]
                    )
            available = set(range(1, 10)) - set([int(x) for x in block if x != '.'])
            for v in range(k, 10):
                if v in available:
                    board[i // 9][i % 9] = '0' + str(v)
                    i = nextPos(i)
                    break
            else:
                board[i // 9][i % 9] = '.'
                i = prevPos(i)

        for i in range(81):
            if board[i // 9][i % 9] != '.':
                board[i // 9][i % 9] = str(int(board[i // 9][i % 9]))


# Backtracking
# Note: - pos in board is from 0 to 81, then cordinate will be (pos // 9, pos % 9)
#       - quit condition: either nextPos or prevPos will return -1 whether solved or not
#       - during computing, the cell be filled with '0d' format, where d is digit
## Performance:
## %%timeit
## %run 0037_solveSudoku.py
## 311 ms ± 18.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidPiece(piece: list[str]) -> bool:
            sud = [int(x) for x in piece if x != '.']
            return len(set(sud)) == len(sud)

        def validatePoint(p) -> bool:
            i, j = divmod(p, 9)
            if not isValidPiece(board[i]):
                return False
            if not isValidPiece([board[y][j] for y in range(9)]):
                return False
            i //= 3
            j //= 3
            if not isValidPiece([board[i*3 + x][j*3 + y] for x in range(3) for y in range(3)]):
                return False
            return True

        def nextPos(p):
            for i in range(p, 81):
                if board[i // 9][i % 9] == '.':
                    return i
            return -1

        def prevPos(p):
            for i in reversed(range(0, p)):
                if board[i // 9][i % 9][0] == '0':
                    return i
            return -1

        i = nextPos(0)
        while i >= 0:
            k = (1 if board[i // 9][i % 9] == '.'
                   else int(board[i // 9][i % 9]) + 1
                )
            for v in range(k, 10):
                board[i // 9][i % 9] = '0' + str(v)
                if validatePoint(i):
                    i = nextPos(i)
                    break
            else:
                board[i // 9][i % 9] = '.'
                i = prevPos(i)

        for i in range(81):
            if board[i // 9][i % 9] != '.':
                board[i // 9][i % 9] = str(int(board[i // 9][i % 9]))


if __name__ == "__main__":
    sol = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], 
             ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
             [".", "9", "8", ".", ".", ".", ".", "6", "."], 
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
             [".", "6", ".", ".", ".", ".", "2", "8", "."], 
             [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(board)
    pprint(board)
    assert(board == [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                     ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])
