# Given two strings s and p, return an array of all the start indices 
# of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase, typically using all the original letters
# exactly once.

# Constraints:
#   1 <= s.length, p.length <= 3 * 10^4
#   s and p consist of lowercase English letters.
from typing import List
from collections import defaultdict


# moving window + counter
# - to simplify the code
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def update_counter(ch: str, add_remove: int) -> int:
            diff_delta = 1 if counter[ch] == 0 else 0   # diff increased
            counter[ch] += 1 * add_remove
            if counter[ch] == 0: diff_delta = -1        # diff reduced
            return diff_delta

        counter = defaultdict(int)
        for ch in p:
            counter[ch] += 1    # ch in p use positive count
        diff = len(counter)     # diff is about the number of unique letters

        m = len(p)
        res = []
        for i, ch in enumerate(s):
            diff += update_counter(ch, -1)  # ch in s use negtive count
            if i >= m:
                diff += update_counter(s[i-m], 1)   # when removing ch, use positive count
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

        r = sol.findAnagrams(s = "cbaebabacd", p = "aabc")
        print(r)
        assert r == [5]

        r = sol.findAnagrams(s = "abab", p = "ab")
        print(r)
        assert r == [0,1,2]

    unitTest(Solution())
    unitTest(Solution1())
