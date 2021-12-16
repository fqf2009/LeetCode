from typing import DefaultDict, List

# Given a string s and a dictionary of strings wordDict, return true if s can 
# be segmented into a space-separated sequence of one or more dictionary words.
# Note that same word in dictionary may be reused multiple times in segmentation.

# DFS + DP + Memorization
# dp[i]: from position i, whether it is possible to break word using wordDict
#        value could be: -1 unknown yet, 0 No, 1 yes
# Runtime: 32 ms, faster than 94.92% of Python3 online submissions for Word Break.
# Memory Usage: 14.3 MB, less than 71.98% of Python3 online submissions for Word Break.
class Solution:
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
    sol = Solution()

    r = sol.wordBreak(s="leetcode", wordDict=["leet", "code"])
    print(r)
    assert (r == True)

    r = sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    print(r)
    assert (r == True)

    r = sol.wordBreak(s="catsandog", wordDict=[
                      "cats", "dog", "sand", "and", "cat"])
    print(r)
    assert (r == False)
