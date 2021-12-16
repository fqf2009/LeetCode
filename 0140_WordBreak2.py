from typing import DefaultDict, List

# Given a string s and a dictionary of strings wordDict, add spaces in s to 
# construct a sentence where each word is a valid dictionary word. Return 
# all such possible sentences in any order. Note that the same word in the 
# dictionary may be reused multiple times in the segmentation.

# DFS, DP, Memorization
# dp[i]: each item will have value [flag, ['sentence1', 'sentence2', ...]] meaning,
#        from position i, is it possible to break word using wordDict, flag could
#        be: -1 unknown yet, 0 No, 1 yes
# Runtime: 28 ms, faster than 86.39% of Python3 online submissions for Word Break II.
# Memory Usage: 14.4 MB, less than 38.06% of Python3 online submissions for Word Break II.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfsWordBreak(pos: int) -> bool:
            if len(s[pos:]) == 0:
                return True
            if dp[pos][0] != -1:
                return bool(dp[pos][0])
            for w in initialToWords[s[pos: pos + 1]]:
                if not s.startswith(w, pos):
                    continue
                nextPos = pos + len(w)
                if dfsWordBreak(nextPos):
                    dp[pos][0] = 1
                    if nextPos < len(s):
                        for sentence in dp[nextPos][1]:
                            dp[pos][1].append(w + ' ' + sentence)
                    else:
                        dp[pos][1].append(w)
            if dp[pos] == -1:
                dp[pos] == 0
            return bool(dp[pos])

        initialToWords = DefaultDict(set)
        for w in wordDict:
            initialToWords[w[0]].add(w)

        dp = [[-1, []] for _ in range(len(s))]
        dfsWordBreak(0)
        return dp[0][1]


# DFS without memorization
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfsWordBreak(pos: int):
            if len(s[pos:]) == 0:
                res.append(' '.join(sentence))
                return
            for w in wd[s[pos: pos + 1]]:
                if s.startswith(w, pos):
                    sentence.append(w)
                    dfsWordBreak(pos + len(w))
                    sentence.pop()
            return

        sentence = []
        res = []
        wd = DefaultDict(set)
        for w in wordDict:
            wd[w[0]].add(w)
        dfsWordBreak(0)

        return res


if __name__ == "__main__":
    sol = Solution1()

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    expected = ["cats and dog", "cat sand dog"]
    r = sol.wordBreak(s, wordDict)
    print(r)
    assert (sorted(r) == sorted(expected))

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    r = sol.wordBreak(s, wordDict)
    print(r)
    r.sort()
    assert (sorted(r) == sorted(expected))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    expected = []
    r = sol.wordBreak(s, wordDict)
    print(r)
    assert (sorted(r) == sorted(expected))
