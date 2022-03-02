# Given two strings s and p, return an array of all the start indices 
# of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase, typically using all the original letters
# exactly once.

# Constraints:
#   1 <= s.length, p.length <= 3 * 104
#   s and p consist of lowercase English letters.
from typing import List
from collections import defaultdict


# moving window + counter
# - to simplify the code
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def updateCmp(ch: str, add_remove: int) -> int:   # return diff delta
            res = 0
            if cmp[ch] == 0: res += 1
            cmp[ch] += 1 * add_remove
            if cmp[ch] == 0: res = -1
            return res

        cmp = defaultdict(int)
        for ch in p:
            cmp[ch] += 1
        diff = len(cmp)

        m = len(p)
        res = []
        for i, ch in enumerate(s):
            diff += updateCmp(ch, -1)
            if i >= m:
                diff += updateCmp(s[i-m], 1)
            if diff == 0:
                res.append(i-m+1)

        return res            
        

# moving window + counter: O(n)
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        comparer = {}
        for i in range(len(p)):
            if p[i] not in comparer:
                comparer[p[i]] = [1, 0]
            else:
                comparer[p[i]][0] += 1
        nDiff = len(comparer)

        res = []
        for i in range(len(s)):
            if s[i] not in comparer:
                comparer[s[i]] = [0, 1]
                nDiff += 1
            else:
                cmp = comparer[s[i]]
                cmp[1] += 1
                if cmp[0] == cmp[1]:
                    nDiff -= 1
                elif cmp[0] == cmp[1] - 1: # was the same before
                    nDiff += 1

            if i >= len(p):
                cmp = comparer[s[i-len(p)]]
                cmp[1] -= 1
                if cmp[0] == cmp[1]:
                    nDiff -= 1
                elif cmp[0] == cmp[1] + 1: # was the same before
                    nDiff += 1

            if nDiff == 0:
                res.append(i-len(p)+1)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        sol = Solution()

        r = sol.findAnagrams(s = "cbaebabacd", p = "abc")
        print(r)
        assert r == [0,6]

        r = sol.findAnagrams(s = "abab", p = "ab")
        print(r)
        assert r == [0,1,2]

    unitTest(Solution())
    unitTest(Solution1())
