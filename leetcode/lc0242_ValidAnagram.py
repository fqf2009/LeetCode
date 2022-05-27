# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original 
# letters exactly once.
# Constraints:
#   1 <= s.length, t.length <= 5 * 10^4
#   s and t consist of lowercase English letters.
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("anagram", "nagaram", True),
            ("rat", "car", False),
        ])
        def test_isAnagram(self, s, t, expected):
            sol = self.solution()       # type:ignore
            r = sol.isAnagram(s, t)
            self.assertEqual(r, expected)

    main()
