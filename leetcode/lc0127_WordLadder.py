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
        for word in chain([beginWord], wordList):
            for wc in getWildcards(word):
                graph.setdefault(wc, set()).add(word)

        visited = {wc: False for wc in graph}
        dq = deque([(beginWord, 1)])
        while len(dq):
            word, depth = dq.popleft()
            for wc in getWildcards(word):
                if visited[wc]:
                    continue
                visited[wc] = True
                for w in graph[wc]:
                    if w == endWord:
                        return depth + 1
                    dq.append((w, depth + 1))  # type: ignore

        return 0


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ])
        def test_ladderLength(self, beginWord, endWord, wordList, expected):

            sol = self.solution()  # type:ignore
            r = sol.ladderLength(beginWord, endWord, wordList)
            self.assertEqual(r, expected)

    main()
