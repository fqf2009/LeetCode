from typing import List
from itertools import chain
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def bfsDepth(endWord) -> int:
            while len(que):
                word, depth = que.popleft()
                for wc in getWildcards(word):
                    if visited[wc]:
                        continue
                    visited[wc] = True
                    for w in graph[wc]:
                        if w == endWord:
                            return depth + 1
                        que.append((w, depth + 1))
            return 0

        def getWildcards(word):
            for i in range(len(word)):
                yield word[:i] + '*' + word[i + 1:]

        graph = {}
        for word in chain([beginWord], wordList):
            for wc in getWildcards(word):
                graph.setdefault(wc, set()).add(word)

        visited = {wc: False for wc in graph}
        que = deque()
        que.append((beginWord, 1))
        return bfsDepth(endWord)


if __name__ == '__main__':
    sol = Solution()

    r = sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
    print(r)
    assert(r == 5)

    r = sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"])
    print(r)
    assert(r == 0)