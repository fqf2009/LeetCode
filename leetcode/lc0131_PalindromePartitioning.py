# Given a string s, partition s such that every substring of the
# partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.
# Constraints:
#   1 <= s.length <= 16
#   s contains only lowercase English letters.
from functools import cache
from typing import List


# Backtracking + DP (Memo)
# - more cache
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def backtrack(s) -> List[List[str]]:
            @cache
            def is_palindrome(s):
                return s1 == s1[::-1]

            if len(s) == 0: return [[]]
            part1 = []
            for i in range(len(s)):
                s1, s2 = s[:i+1], s[i+1:]
                if is_palindrome(s1):
                    part2 = backtrack(s2)
                    part1.extend([[s1] + x for x in part2]) # use + instead of extend!
            return part1

        return backtrack(s) 


# Backtracking + DP (Memo)
class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def backtrack(s) -> List[List[str]]:
            if len(s) == 0: return [[]]
            part1 = []
            for i in range(len(s)):
                s1, s2 = s[:i+1], s[i+1:]
                if s1 == s1[::-1]:
                    part2 = backtrack(s2)
                    part1.extend([[s1] + x for x in part2]) # use + instead of extend!
            return part1

        return backtrack(s) 


# Backtracking
# O(n*(2^n)) in worse case scenario, e.g. "aaaaaa", i.e. every substr is palindrome,
# - every position can be used to split string, so 2^n possibility;
# - each possibility take n time to verify palindrome.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(s):
            if len(s) == 0:
                res.append(part.copy())
            for i in range(len(s)):
                s1 = s[: i + 1]
                if s1 == s1[::-1]:
                    part.append(s1)
                    backtrack(s[i + 1 :])
                    part.pop()

        backtrack(s)
        return res


if __name__ == "__main__":

    def unit_test(solution):
        print()
        print(solution.__name__)
        sol = solution()

        r = sol.partition("aab")
        print(r)
        assert r == [["a", "a", "b"], ["aa", "b"]]

        r = sol.partition("a")
        print(r)
        assert r == [["a"]]

        r = sol.partition("bb")
        print(r)
        assert r == [["b", "b"],["bb"]]

    unit_test(Solution)
    unit_test(Solution1)
    unit_test(Solution2)
