# Given a string s and a dictionary of strings wordDict, return true if s can 
# be segmented into a space-separated sequence of one or more dictionary words.
# Note that same word in dictionary may be reused multiple times in segmentation.
# Constraints:
#   1 <= s.length <= 300
#   1 <= wordDict.length <= 1000
#   1 <= wordDict[i].length <= 20
#   s and wordDict[i] consist of only lowercase English letters.
#   All the strings of wordDict are unique.

from typing import DefaultDict, List
from functools import cache


# DFS or Backtrack? similar to both templates
# - Time:  O(n*w), where n = len(s), w = len(wordDict)
# - Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def backtrack(pos: int) -> bool:
            if pos == n:
                return True
            for w in wordDict:
                if s.startswith(w, pos) and backtrack(pos + len(w)):
                    return True
            return False

        return backtrack(0)


# DFS + DP + Memorization
# dp[i]: from position i, whether it is possible to break word using wordDict
#        value could be: -1 unknown yet, 0 No, 1 yes
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfsWordBreak(pos: int) -> bool:
            if len(s[pos:]) == 0:
                return True
            if dp[pos] >= 0:
                return bool(dp[pos])
            for w in initialToWords[s[pos: pos + 1]]:
                if s.startswith(w, pos):
                    if dfsWordBreak(pos + len(w)):
                        dp[pos] = 1
                        return True
            dp[pos] = 0
            return False

        initialToWords = DefaultDict(set)
        for w in wordDict:
            initialToWords[w[0]].add(w)

        dp = [-1] * len(s)
        return dfsWordBreak(0)


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.wordBreak(s="leetcode", wordDict=["leet", "code"])
        print(r)
        assert r == True

        r = sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
        print(r)
        assert r == True

        r = sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
