# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent
# cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.

# Constraints:
#   m == board.length
#   n = board[i].length
#   1 <= m, n <= 6
#   1 <= word.length <= 15
#   board and word consists of only lowercase and uppercase English letters.
from typing import List


# Backtracking: T/S: O(m*n*3^L), O(L), where L = len(word)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, wp) -> bool:
            if board[i][j] != word[wp]:
                return False
            if wp == len(word) - 1:
                return True
            board[i][j] = '#'
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n:
                    if backtrack(i1, j1, wp + 1):
                        board[i][j] = word[wp]
                        return True
            board[i][j] = word[wp]
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.exist(board=[['a']], word='a')
        print(r)
        assert(r == True)

        r = sol.exist(board=[['A', 'B', 'C', 'E'],
                             ['S', 'F', 'C', 'S'],
                             ['A', 'D', 'E', 'E']],
                      word='ABCCED')
        print(r)
        assert(r == True)

        r = sol.exist(board=[['A', 'B', 'C', 'E'],
                             ['S', 'F', 'C', 'S'],
                             ['A', 'D', 'E', 'E']],
                      word='SEE')
        print(r)
        assert(r == True)

        r = sol.exist(board=[['A', 'B', 'C', 'E'],
                             ['S', 'F', 'C', 'S'],
                             ['A', 'D', 'E', 'E']],
                      word='ABCB')
        print(r)
        assert(r == False)

    unitTest(Solution())
