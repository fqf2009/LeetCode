# You are given a 0-indexed array of strings words. Each string consists
# of lowercase English letters only. No letter occurs more than once in
# any string of words.

# Two strings s1 and s2 are said to be connected if the set of letters
# of s2 can be obtained from the set of letters of s1 by any one of
# the following operations:
#  - Adding exactly one letter to the set of the letters of s1.
#  - Deleting exactly one letter from the set of the letters of s1.
#  - Replacing exactly one letter from the set of the letters of s1
#    with any letter, including itself.

# The array words can be divided into one or more non-intersecting
# groups. A string belongs to a group if any one of the following is true:
#  - It is connected to at least one other string of the group.
#  - It is the only string present in the group.
# Note that the strings in words should be grouped in such a manner that a
# string belonging to a group cannot be connected to a string present in any
# other group. It can be proved that such an arrangement is always unique.

# Return an array ans of size 2 where:
#  - ans[0] is the total number of groups words can be divided into, and
#  - ans[1] is the size of the largest group.

from typing import List
from collections import Counter


# Graph + DFS: O(n)
#  - build a graph, nodes will be each word (set), plus literally remove each
#    single char from this word (set). e.g.:
#    from {c,d,e}, to derive: {d,e}, {c,e}, {c,d}
#  - the word node and its derived nodes are connected in graph.
#  - use a DFS search to group all connected nodes.
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def dfsVisit(x, grpWords = set()) -> int:
            grpSize = 0
            visited[x] = True
            for w in graph[x]:
                if w in wordSet and w not in grpWords:
                    grpWords.add(w)
                    grpSize += wordSet[w]
                if not visited[w]:
                    grpSize += dfsVisit(w, grpWords)
            return grpSize

        wordSet = Counter([frozenset(w) for w in words])
        graph = {}
        for w in wordSet:
            graph.setdefault(w, set()).add(w)
            for ch in w:
                w1 = w - {ch}
                graph.setdefault(w1, set()).add(w)
                graph[w].add(w1)

        visited = {x: False for x in graph}
        nGroup, maxSize = 0, 0
        for x in visited.keys():
            if not visited[x]:
                maxSize = max(maxSize, dfsVisit(x))
                nGroup += 1

        return [nGroup, maxSize]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.groupStrings(words=["web", "a", "te", "hsx", "v", "k", "a", "roh"])
        print(r)
        assert r == [5,4]

        r = sol.groupStrings(words=["ghnv", "uip", "tenv", "hvepx", "e", "ktc", "byjdt", "ulm", "cae", "ea"])
        print(r)
        assert r == [8, 3]

        r = sol.groupStrings(words=["a", "b", "ab", "cde"])
        print(r)
        assert r == [2, 3]

        r = sol.groupStrings(["a", "ab", "abc"])
        print(r)
        assert [1, 3]

    unitTest(Solution())
