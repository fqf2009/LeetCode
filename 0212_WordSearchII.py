# Given an m x n board of characters and a list of strings words,
# return all words on the board.
# Each word must be constructed from letters of sequentially adjacent
# cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

# Constraints:
#   m == board.length
#   n == board[i].length
#   1 <= m, n <= 12
#   board[i][j] is a lowercase English letter.
#   1 <= words.length <= 3 * 104
#   1 <= words[i].length <= 10
#   words[i] consists of lowercase English letters.
#   All the strings of words are unique.
from typing import List
from itertools import product


# Backtracking + Trie
# - To improve performace: remove word from trie when it is found
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = {}
        board_words = set()

        def addWords(word: str):
            branch = trie
            for ch in word:
                branch = branch.setdefault(ch, {})
            branch['*'] = None
        
        def dfsFind(i, j, root, prefix):
            ch = board[i][j]
            if ch in root:
                branch = root[ch]
                if '*' in branch:
                    board_words.add(prefix + ch)
                    if len(branch) == 1:    # leaf node
                        del root[ch]
                        return
                board[i][j] = '.'
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < m and 0 <= j1 < n:
                        dfsFind(i1, j1, branch, prefix + ch)
                board[i][j] = ch            # delete leaf in path after visiting
                if not branch or len(branch) == 1 and '*' in branch:
                    del root[ch]

        for word in words:
            addWords(word)

        for i in range (m):
            for j in range(n):
                dfsFind(i, j, trie, '')

        return list(board_words)


# Backtracking + Trie - 42 / 62 test cases passed, then TLE (Time Limit Exceeded)
# - Time:  O(L) + O(m*n*k) in worst case scenario, k is average length of words
# - Space: O(L), where L is the number of all letters of words
class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = {}
        board_words = set()

        def addWords(word: str):
            branch = trie
            for ch in word:
                branch = branch.setdefault(ch, {})
            branch['*'] = None
        
        def dfsFind(i, j, root, prefix):
            ch = board[i][j]
            if ch in root:
                branch = root[ch]
                if '*' in branch:
                    board_words.add(prefix + ch)
                board[i][j] = '.'
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < m and 0 <= j1 < n:
                        dfsFind(i1, j1, branch, prefix + ch)
                board[i][j] = ch

        for word in words:
            addWords(word)

        for i in range (m):
            for j in range(n):
                dfsFind(i, j, trie, '')

        return list(board_words)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findWords(board=[["o", "a", "a", "n"], 
                                 ["e", "t", "a", "e"], 
                                 ["i", "h", "k", "r"], 
                                 ["i", "f", "l", "v"]], 
                          words=["oath", "pea", "eat", "rain"])
        print(r)
        assert sorted(r) == sorted(["eat", "oath"])

        r = sol.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"])
        print(r)
        assert r == []

        r = sol.findWords(board=[["a"]], words=["a"])
        print(r)
        assert r == ['a']

        r = sol.findWords(
           [["b","a","b","a","b","a","b","a","b","a"],
            ["a","b","a","b","a","b","a","b","a","b"],
            ["b","a","b","a","b","a","b","a","b","a"],
            ["a","b","a","b","a","b","a","b","a","b"],
            ["b","a","b","a","b","a","b","a","b","a"],
            ["a","b","a","b","a","b","a","b","a","b"],
            ["b","a","b","a","b","a","b","a","b","a"],
            ["a","b","a","b","a","b","a","b","a","b"],
            ["b","a","b","a","b","a","b","a","b","a"],
            ["a","b","a","b","a","b","a","b","a","b"]],
            ['abababab' + x + y for x, y in (product((chr(ord('a')+i) for i in range(26)), repeat = 2))])
        print(r)
        assert r == ['ababababab']

    unitTest(Solution())
    unitTest(Solution1())
