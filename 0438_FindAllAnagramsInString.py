# Given two strings s and p, return an array of all the start indices 
# of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase, typically using all the original letters
# exactly once.

from typing import List

# moving window + counter: O(n)
class Solution:
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
