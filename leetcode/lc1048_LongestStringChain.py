# You are given an array of words where each word 
# consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert
# exactly one letter anywhere in wordA without changing the 
# order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" 
# is not a predecessor of "bcad". A word chain is a sequence of 
# words [word1, word2, ..., wordk] with k >= 1, where word1 is 
# a predecessor of word2, word2 is a predecessor of word3, 
# and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with 
# words chosen from the given list of words.

# Constraints:
#   1 <= words.length <= 1000
#   1 <= words[i].length <= 16
#   words[i] only consists of lowercase English letters.
from typing import List
from functools import cache
from collections import defaultdict

# Graph, DFS, Recursion, DP, Memo: O(n*log(n))
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def chainable(s1: str, s2: str) -> bool:
            m, n = len(s1), len(s2)
            if m + 1 != n: return False
            i, j = 0, 0
            while i < m and j < n:
                if s1[i] != s2[j]:
                    if i != j:
                        return False
                else:
                    i += 1
                j += 1
            return True

        @cache
        def dfs(w: str) -> int:
            res = 0
            if w in graph:  # avoid insert dummy word (bad behavior for default dict)
                for w1 in graph[w]:
                    res = max(res, dfs(w1))
            return res + 1

        wgrp = defaultdict(list)     # words group by length
        for w in words:
            wgrp[len(w)].append(w)

        graph = defaultdict(set)
        wlen = sorted(wgrp.keys())  # words length list
        for i in range(1, len(wlen)):
            l1, l2 = wlen[i-1], wlen[i]
            if l1 + 1 != l2: continue
            for w1 in wgrp[l1]:
                for w2 in wgrp[l2]:
                    if chainable(w1, w2):
                        graph[w1].add(w2)

        if len(graph) == 0:
            return 1 
        else:
            return max(dfs(w) for w in graph)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestStrChain(["a","b","ba","bca","bda","bdca"])
        print(r)
        assert r == 4

        r = sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])
        print(r)
        assert r == 5

        r = sol.longestStrChain(["abcd","dbqca"])
        print(r)
        assert r == 1

    unitTest(Solution())
