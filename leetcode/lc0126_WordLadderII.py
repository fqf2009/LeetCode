# A transformation sequence from word beginWord to word endWord using a dictionary
# wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#  - Every adjacent pair of words differs by a single letter.
#  - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to 
#    be in wordList.
#  - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all 
# the shortest transformation sequences from beginWord to endWord, or an empty 
# list if no such sequence exists. Each sequence should be returned as a list 
# of the words [beginWord, s1, s2, ..., sk].
# Constraints:
#   1 <= beginWord.length <= 5
#   endWord.length == beginWord.length
#   1 <= wordList.length <= 1000
#   wordList[i].length == beginWord.length
#   beginWord, endWord, and wordList[i] consist of lowercase English letters.
#   beginWord != endWord
#   All the words in wordList are unique.
from typing import List
from collections import defaultdict, deque


# BFS + Backtracking
# - Optimize: (works)
#   1. no need to build undirected graph, just use function to find neighbours
#   2. when to remove visited item during BFS?
#      (1) when poping-up from left of deque: note each layer (level) has many
#          items, some will be visited and removed earlier than others, those
#          being removed too late will create extra pathes (not the shortest),
#          so that the backtracking step has to take care of it - difficult!!!
#      (2) when adding edge to directed graph: This is wrong!!!
#          because there will be other nodes at same level later to point to this
#          being deleted node, so we cannot find all pathes.
#      (3) after visiting one layer of nodes: so next layer of nodes can never
#          point back to previous layers, and all pathes will have the same 
#          shortest length.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)  # import to avoid endless loop
        if endWord not in word_set: return []

        def related_words(w1: str) -> List[str]:
            res = set()
            for i in range(len(w1)):
                for j in range(26):
                    w2 = w1[:i] + chr(ord('a') + j) + w1[i+1:]
                    if w1 != w2 and w2 in word_set:
                        res.add(w2)
            return list(res)

        # build directed graph
        dq = deque([beginWord])
        graph = defaultdict(set)    # directed graph, use set to eliminate duplicate pathes!!!
        reach_end = False
        while dq:                       # BFS
            visited = set()
            for _ in range(len(dq)):    # visit entire layer
                w1 = dq.popleft()
                for w2 in related_words(w1):
                    if w2 in word_set:
                        visited.add(w2)
                        graph[w1].add(w2)
                        dq.append(w2)
                        if w2 == endWord:
                            reach_end = True

            if reach_end: break
            word_set -= visited     # visited words need to be removed

        # backtrack to get all shortest pathes
        res = []
        path = [beginWord]
        def back_track(w1):
            if w1 == endWord:
                res.append(path.copy())
            else:
                for w2 in graph[w1]:
                    path.append(w2)
                    back_track(w2)
                    path.pop()

        back_track(beginWord)
        return res


# BFS + Backtracking
# Time Limit Exceeded - 19 / 32 test cases passed.
# Analysis:
# - first, build an undirected graph and use BFS to find shortest path
# - during BFS, create a directed graph until finding the end word
# - backtrack the directed graph to get all pathes
class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        word_set.add(beginWord)
        if endWord not in word_set: return []
        
        graph1 = defaultdict(set)  # undirected graph
        for w1 in word_set:             
            for i in range(len(w1)):
                for j in range(26):
                    w2 = w1[:i] + chr(ord('a') + j) + w1[i+1:]
                    if w1 != w2 and w2 in word_set:
                        graph1[w1].add(w2)
                        graph1[w2].add(w1)

        dq = deque()
        dq.append([beginWord, 0])
        graph2 = defaultdict(list)  # directed graph
        end_depth = 2**9
        while dq:                   # BFS
            w1, depth = dq.popleft()
            if depth >= end_depth: break
            if w1 not in word_set: continue     # already visited
            word_set.remove(w1)     # avoid cyclic graph
            for w2 in graph1[w1]:
                if w2 == endWord:
                    end_depth = depth + 1
                if w2 in word_set:
                    graph2[w1].append(w2)
                    dq.append([w2, depth+1])

        res = []
        path = [beginWord]
        def back_track(w1):
            if len(path) == end_depth + 1:  # to avoid "Time Limit Exceeded"
                if w1 == endWord:           # but still: 21 / 32 test cases passed.
                    res.append(path.copy())
            else:
                for w2 in graph2[w1]:
                    path.append(w2)
                    back_track(w2)
                    path.pop()

        back_track(beginWord)
        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("qa", "sq", ['lt', 'fa', 'to', 'kr', 'se', 'ti', 'so', 'au', 'sr', 'cm', 'ur', 
                          'ci', 'si', 'ow', 'ba', 'mb', 'ya', 'ma', 'rh', 'rn', 'cr', 'po', 
                          'lo', 'br', 'sn', 'tm', 'fe', 're', 'be', 'sm', 'sq', 'qa', 'ho', 
                          'or', 'go', 'av', 'mt', 'db', 'ca', 'ln', 'sb', 'ph'],
                            [['qa', 'ma', 'mb', 'sb', 'sq'], 
                             ['qa', 'ca', 'cm', 'sm', 'sq'], 
                             ['qa', 'ca', 'cr', 'sr', 'sq'], 
                             ['qa', 'ca', 'ci', 'si', 'sq'], 
                             ['qa', 'ba', 'be', 'se', 'sq'], 
                             ['qa', 'ba', 'br', 'sr', 'sq'], 
                             ['qa', 'fa', 'fe', 'se', 'sq']]),
            ("hot", "dog", ["hot","dog","dot"], [["hot","dot","dog"]]),
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]),
            ("hit", "cog", ["hot","dot","dog","lot","log"], []),
        ])
        def test_findLadders(self, beginWord, endWord, wordList, expected):
            sol = self.solution()  # type:ignore
            r = sol.findLadders(beginWord, endWord, wordList)
            self.assertEqual(sorted(r), sorted(expected))

    main()
