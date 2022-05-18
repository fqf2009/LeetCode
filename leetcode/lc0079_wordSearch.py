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
from functools import cache, reduce
from typing import Counter, List


# Backtracking/DFS: T/S: O(m*n*3^L), O(L), where L = len(word)
# - pruning + memo?
# - Error - the parameters (i, j, p) do not uniquely determine the result,
#           because the previous steps in the path (mark by '#') is part
#           of the solution, and also influence the future steps.
class Solution3:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        @cache
        def backtrack(i, j, p) -> bool:
            if board[i][j] != word[p]:
                return False
            if p == len(word) - 1:
                return True
            board[i][j] = '#'
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n:
                    if backtrack(i1, j1, p + 1):
                        board[i][j] = word[p]
                        return True
            board[i][j] = word[p]
            return False

        # pruning
        board_counter = reduce(lambda x, y: x+y, (Counter(x) for x in board))
        word_counter = Counter(word)
        if any(board_counter[ch] < freq for ch, freq in word_counter.items()):
            return False
        if word_counter[word[0]] < word_counter[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


# Backtracking/DFS: T/S: O(m*n*3^L), O(L), where L = len(word)
# - simplify backtracking code
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, p) -> bool:
            if p == len(word): return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[p]:
                return False
            board[i][j] = '#'       # mark path
            res = (backtrack(i+1, j, p + 1) or backtrack(i-1, j, p + 1) or
                   backtrack(i, j+1, p + 1) or backtrack(i, j-1, p + 1))
            board[i][j] = word[p]   # restore
            return res

        # pruning
        board_counter = reduce(lambda x, y: x+y, (Counter(x) for x in board))
        word_counter = Counter(word)
        if any(board_counter[ch] < freq for ch, freq in word_counter.items()):
            return False
        if word_counter[word[0]] < word_counter[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


# Backtracking/DFS: T/S: O(m*n*3^L), O(L), where L = len(word)
# - pruning to improve performance
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, p) -> bool:
            if board[i][j] != word[p]:
                return False
            if p == len(word) - 1:
                return True
            board[i][j] = '#'
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n:
                    if backtrack(i1, j1, p + 1):
                        board[i][j] = word[p]
                        return True
            board[i][j] = word[p]
            return False

        # pruning
        board_counter = reduce(lambda x, y: x+y, (Counter(x) for x in board))
        word_counter = Counter(word)
        if any(board_counter[ch] < freq for ch, freq in word_counter.items()):
            return False
        if word_counter[word[0]] < word_counter[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


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
    def unitTest(Sol):
        print(Sol.__name__)
        sol = Sol()

        r = sol.exist(board=[["Z","Z","Z","Z","Z"],
                             ["Z","C","B","A","B"],
                             ["A","D","E","D","C"],
                             ["B","E","Z","Z","Z"]],
                      word="ABEDCBA")
        print(r)
        assert(r == True)

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

    unitTest(Solution)
    unitTest(Solution1)
    unitTest(Solution2)
