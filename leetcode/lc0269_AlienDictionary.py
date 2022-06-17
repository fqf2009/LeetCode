# There is a new alien language that uses the English alphabet. However,
# the order among the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary,
# where the strings in words are sorted lexicographically by the rules of
# this new language.
# Return a string of the unique letters in the new alien language sorted in
# lexicographically increasing order by the new language's rules. If there is
# no solution, return "". If there are multiple solutions, return any of them.
# A string s is lexicographically smaller than a string t if at the first
# letter where they differ, the letter in s comes before the letter in t in
# the alien language. If the first min(s.length, t.length) letters are the
# same, then s is smaller if and only if s.length < t.length.
# Constraints:
#   1 <= words.length <= 100
#   1 <= words[i].length <= 100
#   words[i] consists of only lowercase English letters.
from collections import defaultdict, deque
from itertools import zip_longest
from typing import Counter, List


# Topology Sort + DFS (detect cycle in Directed Graph)
# - T/S: O(V+E), O(V+E), or O(C), O(C), where C = all characters in words
# - e.g.: ["wrt", "wrf", "er", "ett", "rftt"]
#   graph (adj list):   f -> t
#                       e -> w
#                       t -> r
#                       r -> e
#   DFS topology sort:  [w, e, r, t, f]  
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_lst = defaultdict(set)
        letters = set(ch for word in words for ch in word)

        for wd1, wd2 in zip(words, words[1:]):
            for ch1, ch2 in zip(wd1, wd2):
                if ch1 != ch2:
                    adj_lst[ch2].add(ch1)   # DFS has different direction from BFS
                    break  # word order determined
            else:  # check for ["aa", "a"] situation
                if len(wd1) > len(wd2):
                    return ""

        def dfs_visit(ch) -> bool:
            if ch not in visited or visited[ch] == 1:
                return True
            if visited[ch] == -1:
                return False    # cycle detected
            visited[ch] = -1    # mark for this DFS visit
            for ch2 in adj_lst[ch]:
                if not dfs_visit(ch2):
                    return False
            visited[ch] = 1     # mark visited at post-order
            ordered_letters.append(ch)
            return True

        visited = {ch: 0 for ch in adj_lst.keys()}
        ordered_letters = []
        for ch in visited.keys():
            if not dfs_visit(ch):
                return ""

        return "".join(list(letters - set(ordered_letters)) + ordered_letters)


# practice: DFS (topology sort + detect cycle)
class Solution0:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for w1, w2 in zip(words, words[1:]):
            for ch1, ch2 in zip_longest(w1, w2):
                if ch1 != ch2:
                    if ch1 == None: break
                    if ch2 == None: return ""
                    graph.setdefault(ch2, set()).add(ch1)
                    break
        
        def dfsDetectCircle(x):
            if visited[x] == -1: return True
            visited[x] = -1     # visiting
            for y in graph[x]:
                if y in visited and visited[y] != 1:
                    if dfsDetectCircle(y):
                        return True
            visited[x] = 1
            orderedLetters.append(x)
            return False
            
        visited = {x: 0 for x in graph} # not visited yet
        orderedLetters = []
        for x in graph:
            if visited[x] == 0 and dfsDetectCircle(x):
                return ""

        letters = set(ch for word in words for ch in word)
        return "".join(list(letters - set(orderedLetters)) + orderedLetters)


# Topology Sort + BFS (detect cycle in Directed Graph)
# - T/S: O(V+E), O(V+E), or O(C), O(C), where C = all characters in words
# - e.g.: ["wrt", "wrf", "er", "ett", "rftt"]
#   graph (adj list):   f <- t     (reversed direction)
#                       e <- w
#                       t <- r
#                       r <- e
#   BFS topology sort:  [w, e, r, t, f]
#   - starting from nodes with idegree == 0
#   - each time a edge is removed, reduce indegree
#   - when indegree reaches 0, add to deque.
class Solution1:
    def alienOrder(self, words: List[str]) -> str:
        adj_lst = defaultdict(set)
        # all letters are collected
        indegree = Counter({ch: 0 for word in words for ch in word})

        for wd1, wd2 in zip(words, words[1:]):
            for ch1, ch2 in zip(wd1, wd2):
                if ch1 != ch2:
                    if ch2 not in adj_lst[ch1]:  # add indegree only once!
                        adj_lst[ch1].add(ch2)    # BFS has different direction from DFS
                        indegree[ch2] += 1
                    break  # word order determined
            else:  # check for ["aa", "a"] situation !
                if len(wd1) > len(wd2):
                    return ""

        visiting = deque(c for c, freq in indegree.items() if freq == 0)
        res = []
        while visiting:
            ch1 = visiting.popleft()
            res.append(ch1)
            for ch2 in adj_lst[ch1]:
                indegree[ch2] -= 1
                if indegree[ch2] == 0:
                    visiting.append(ch2)

        # check all letters are collected, instead of clear indegree
        return "" if len(res) < len(indegree) else "".join(res)


if __name__ == "__main__":

    def unitTest(solution):
        print(solution.__name__)
        sol = solution()

        r = sol.alienOrder(["ac", "ab", "zc", "zb"])
        print(r)
        assert r in ("acbz", "azcb", "aczb", "cbaz", "cabz", "cazb")

        r = sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
        print(r)
        assert r == "wertf"

        r = sol.alienOrder(["z", "x"])
        print(r)
        assert r == "zx"

        r = sol.alienOrder(["z", "x", "z"])
        print(r)
        assert r == ""

        r = sol.alienOrder(["z", "z"])
        print(r)
        assert r == "z"

        r = sol.alienOrder(["zz", "z"])
        print(r)
        assert r == ""

    unitTest(Solution)
    unitTest(Solution0)
    unitTest(Solution1)
