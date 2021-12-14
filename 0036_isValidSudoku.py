from typing import List


# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to 
# be validated according to the following rules:
#  - Each row must contain the digits 1-9 without repetition.
#  - Each column must contain the digits 1-9 without repetition.
#  - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#  - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#  - Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidPiece(piece: list[str]) -> bool:
            sud = [x for x in piece if x != '.']
            return len(set(sud)) == len(sud)

        for r in board:
            if not isValidPiece(r):
                return False
        
        for j in range(9):
            piece = [board[i][j] for i in range(9)]
            if not isValidPiece(piece):
                return False

        for i in range(3):
            for j in range(3):
                piece = [board[i*3 + x][j*3 +y] for x in range(3) for y in range(3)]
                if not isValidPiece(piece):
                    return False
        
        return True
        

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    r = Solution().isValidSudoku(board)
    print(r)
    assert(r == True)

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    r = Solution().isValidSudoku(board)
    print(r)
    assert(r == False)
