# A transformation sequence from word beginWord to word endWord using a dictionary
# wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#  - Every adjacent pair of words differs by a single letter.
#  - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to 
#    be in wordList.
#  - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the 
# number of words in the shortest transformation sequence from beginWord to 
# endWord, or 0 if no such sequence exists.
# Constraints:
#   1 <= beginWord.length <= 10
#   endWord.length == beginWord.length
#   1 <= wordList.length <= 5000
#   wordList[i].length == beginWord.length
#   beginWord, endWord, and wordList[i] consist of lowercase English letters.
#   beginWord != endWord
#   All the words in wordList are unique.
from typing import List
from itertools import chain
from collections import deque


# BFS: O(n*m*26), where m = avg_len(word)
# - 10 times slower than wildcard and graph solution
# - similar to 0127_WordLadderII, just use function find all related words,
#   no need to build undirected graph.
# - layer by layer to remove visited words from word_set.
class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        def related_words(w1: str) -> List[str]:
            res = set()
            for i in range(len(w1)):
                for j in range(26):
                    w2 = w1[:i] + chr(ord('a') + j) + w1[i+1:]
                    if w1 != w2 and w2 in word_set:
                        res.add(w2)
            return list(res)

        dq = deque([beginWord])
        res = 1
        if beginWord in word_set:
            word_set.remove(beginWord)
        while dq:
            res += 1
            visited = set()
            for _ in range(len(dq)):    # pop entire layer
                w1 = dq.popleft()
                for w2 in related_words(w1):
                    visited.add(w2)
                    if w2 == endWord:
                        return res
                    dq.append(w2)

            word_set -= visited

        return 0


# BFS: O(n*m), where m = avg_len(word)
# Analysis:
# - how to build the graph? how to connect all words?
# - endWord in wordList? if not, return False. (this step is optional)
# - nodes in graph are all wildcards, edges are wildcards to words connections.
# - nodes in deque are all words, wildcards are not in deque, the reason is
#   we need the depth or distance between words, not including wildcards, i.e.,
#   jumping from one word to another.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getWildcards(word):
            for i in range(len(word)):
                yield word[:i] + '*' + word[i + 1:]     # generator

        graph = {}
        endWordInList = False
        for word in wordList:
            if word == endWord:
                endWordInList = True
            for wc in getWildcards(word):
                graph.setdefault(wc, list()).append(word)   # word is unique

        if not endWordInList:
            return 0

        visited = set() # save wildcard
        dq = deque()    # save word
        dq.append([beginWord, 1])
        while dq:
            w1, depth = dq.popleft()
            for wc in getWildcards(w1):
                if wc not in visited:
                    visited.add(wc)
                    for w2 in graph.get(wc, []):
                        if w2 == endWord:
                            return depth + 1
                        dq.append([w2, depth + 1])

        return 0


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("a", "c", ["a","b","c"], 2),
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ])
        def test_ladderLength(self, beginWord, endWord, wordList, expected):

            sol = self.solution()  # type:ignore
            r = sol.ladderLength(beginWord, endWord, wordList)
            self.assertEqual(r, expected)

    main()
