# Given two strings s and t of lengths m and n respectively, return 
# the minimum window substring of s such that every character in t
# (including duplicates) is included in the window. If there is no 
# such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
# Constraints:
#   m == s.length
#   n == t.length
#   1 <= m, n <= 10^5
#   s and t consist of uppercase and lowercase English letters.
from collections import Counter


# Counter + Sliding Window
class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        cnt_not_met = len(target_counter)  # number of unique chars not satisfied yet
        j = -1
        min_len = len(s) + 1
        min_str = ''
        for i, ch in enumerate(s):
            if ch in target_counter:
                target_counter[ch] -= 1
                if target_counter[ch] == 0:
                    cnt_not_met -= 1
                while j < i:
                    ch1 = s[j+1]
                    if ch1 in target_counter:
                        if target_counter[ch1] >= 0: break
                        target_counter[ch1] += 1
                    j += 1
                if cnt_not_met == 0 and i - j < min_len:
                    min_len = i - j
                    min_str = s[j+1: i+1]

        return min_str


# practise
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntr = Counter(t)
        minLen = len(s) + 1
        res = ""
        left = 0
        for i, ch in enumerate(s):
            if ch in cntr:
                cntr[ch] -= 1
                if max(cntr.values()) <= 0:
                    while True:
                        if s[left] not in cntr:
                            left += 1
                        elif cntr[s[left]] < 0:
                            cntr[s[left]] += 1
                            left += 1
                        else:
                            break
                    if i - left + 1 < minLen:
                        minLen = i - left + 1
                        res = s[left: i+1]

        return res
        

if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
        ])
        def test_minWindow(self, parent, s, expected):
            sol = self.solution()       # type:ignore
            r = sol.minWindow(parent, s)
            self.assertEqual(r, expected)

    main()
