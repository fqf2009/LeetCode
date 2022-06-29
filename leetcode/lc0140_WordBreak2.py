# Given a string s and a dictionary of strings wordDict, add spaces in s to 
# construct a sentence where each word is a valid dictionary word. Return 
# all such possible sentences in any order. Note that the same word in the 
# dictionary may be reused multiple times in the segmentation.
# Constraints:
#   1 <= s.length <= 20
#   1 <= wordDict.length <= 1000
#   1 <= wordDict[i].length <= 10
#   s and wordDict[i] consist of only lowercase English letters.
#   All the strings of wordDict are unique.

from functools import cache
from typing import DefaultDict, List


# Backtrack + DFS + DP + Memo
# Time Complexity: O(W + w^n) on average
# - where W = len(wordDict), N = len(s),
#         w = on average the number of words for each initial letter
#         n = on average the number of words which s is split into
# - However, in some edge cases, the time complexity could be
#   much worse: O(N^2 + 2^N + W), e.g.:
#       s = "aaaaaa", wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        initial_to_words = DefaultDict(list)
        for word in wordDict:
            initial_to_words[word[0]].append(word)

        @cache
        def dp_break(pos: int):
            if pos == len(s): return (True, [[]])
            sentences = []
            for word in initial_to_words[s[pos]]:
                if s[pos:].startswith(word):
                    success, sntn = dp_break(pos + len(word))
                    if success:
                        sentences.extend([word] + x for x in sntn)  # extend(Iterable)
                        # for x in sntn:                            # equivalence
                        #   sentences.append([word] + x)
            if len(sentences) > 0:
                return (True, sentences)
            else:
                return (False, [])

        success, sntn = dp_break(0)
        if success:
            return [' '.join(x) for x in sntn]
        else:
            return []


# backtrack template
class Solution00:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = []
        res = []

        def backtrack(pos):
            if pos == len(s):
                res.append(' '.join(words))
            for word in wordDict:
                if s[pos:].startswith(word):
                    words.append(word)
                    backtrack(pos + len(word))
                    words.pop()

        backtrack(0)
        return res


# backtrack + dp + memo
class Solution01:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def backtrack(pos):
            if (pos == len(s)):
                return [[]]             # success, reutnrn [[]]
            sentences = []              # not success, return []
            for word in wordDict:
                if s[pos:].startswith(word):
                    stnts = backtrack(pos + len(word))
                    for x in stnts:
                        sentences.append([word] + x)

            return sentences
        
        return [' '.join(x) for x in backtrack(0)]


# DFS, DP, Memorization
# dp[i]: each item will have value [flag, ['sentence1', 'sentence2', ...]] meaning,
#        from position i, is it possible to break word using wordDict, flag could
#        be: -1 unknown yet, 0 No, 1 yes
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfsWordBreak(pos: int) -> bool:
            if len(s[pos:]) == 0:
                return True
            if dp[pos][0] != -1:
                return bool(dp[pos][0])
            dp[pos][0] = 0
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
            return bool(dp[pos])

        initialToWords = DefaultDict(set)
        for w in wordDict:
            initialToWords[w[0]].add(w)

        dp = [[-1, []] for _ in range(len(s))]
        dfsWordBreak(0)
        return dp[0][1]


# Backtracking + DFS, without memorization
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(pos: int):
            if pos == len(s):
                res.append(' '.join(sentence))
                return
            for w in wd[s[pos: pos + 1]]:
                if s.startswith(w, pos):
                    sentence.append(w)
                    backtrack(pos + len(w))
                    sentence.pop()
            return

        sentence = []
        res = []
        wd = DefaultDict(list)
        for w in wordDict:
            wd[w[0]].append(w)
        backtrack(0)

        return res


if __name__ == "__main__":
    def unit_test(sol):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cats and dog", "cat sand dog"]
        r = sol.wordBreak(s, wordDict)
        print(r)
        assert sorted(r) == sorted(expected)

        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        r = sol.wordBreak(s, wordDict)
        print(r)
        r.sort()
        assert sorted(r) == sorted(expected)

        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = []
        r = sol.wordBreak(s, wordDict)
        print(r)
        assert sorted(r) == sorted(expected)

    unit_test(Solution())
    unit_test(Solution00())
    unit_test(Solution01())
    unit_test(Solution1())
    unit_test(Solution2())
