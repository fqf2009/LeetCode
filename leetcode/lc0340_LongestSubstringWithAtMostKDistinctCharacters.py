# Given a string s and an integer k, return the length of 
# the longest substring of s that contains at most k
# distinct characters.
#   Constraints:
#   1 <= s.length <= 5 * 10^4
#   0 <= k <= 50
from collections import Counter


# Sliding window - T/S: O(n), O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        cntr = Counter()
        j, nDistinct, res = 0, 0, 0
        for i, ch in enumerate(s):
            if cntr[ch] == 0:
                nDistinct += 1
            cntr[ch] += 1

            while nDistinct > k:
                cntr[s[j]] -= 1
                if cntr[s[j]] == 0:
                    nDistinct -= 1
                j += 1

            res = max(res, i - j + 1)

        return res


# Sliding window - T/S: O(n), O(k)
class Solution1:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        cntr = Counter()
        j, res = 0, 0
        for i, ch in enumerate(s):
            cntr[ch] += 1
            while len(cntr) > k:
                if cntr[s[j]] == 1:
                    del cntr[s[j]]
                else:
                    cntr[s[j]] -= 1
                j += 1

            res = max(res, i - j + 1)

        return res


# Sliding window
# - faster, only when k is much smaller than n!
# - worst case: O(n*k)
# - refer to: 0159_LongestSubstringWithAtMostTwoDistinctCharacters
class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        charPos = {}
        left, res = -1, 0
        for i, ch in enumerate(s):
            charPos[ch] = i
            if len(charPos) == k + 1:
                left, ch1 = min((pos, ch) for ch, pos in charPos.items())
                del charPos[ch1]
            res = max(res, i - left)

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.lengthOfLongestSubstringKDistinct("eceba", k = 2)
        print(r)
        assert r == 3

        r = sol.lengthOfLongestSubstringKDistinct("ecceeeba", k = 2)
        print(r)
        assert r == 6

        r = sol.lengthOfLongestSubstringKDistinct("aa", k = 1)
        print(r)
        assert r == 2

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
