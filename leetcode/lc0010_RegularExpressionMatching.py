# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#   '.' Matches any single character.​​​​
#   '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Constraints:
#   1 <= s.length <= 20
#   1 <= p.length <= 30
#   s contains only lowercase English letters.
#   p contains only lowercase English letters, '.', and '*'.
#   It is guaranteed for each appearance of the character '*',
#       there will be a previous valid character to match.
from functools import cache


# DP
# Top-Down Variation (still recursion)
class Solution():
    def isMatch(self, text, pattern):
        @cache
        def dp(i, j):
            if j == len(pattern): return i == len(text)

            first_char_match = i < len(text) and pattern[j] in (text[i], '.')
            if j+1 < len(pattern) and pattern[j+1] == '*':
                return dp(i, j+2) or first_char_match and dp(i+1, j)
            else:
                return first_char_match and dp(i+1, j+1)

        return dp(0, 0)


# Recursion
# - if pattern is empty, text has to be empty, otherwise not match;
# - check first char in text and pattern, match or not;
# - if next char in pattern is '*', two scenarios:
#   - assume '[ch]*' match 0 char in text, i.e., to match(text, pattern[2:]),
#     this way, '[ch]*' is skipped.
#   - assume '[ch]*' match 1 char in text, i.e., to match(text[1:], pattern),
#     this way, pattern can continue to match next 0 or 1 char (i.e. many char).
# - if next char in pattern is not '*', continue, ...
class Solution1():
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_char_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':     # second char is '*'
            return (self.isMatch(text, pattern[2:]) or  # '[ch]*' match zero char in text
                    first_char_match and self.isMatch(text[1:], pattern))   # '[ch]*' match text[0]
        else:   # second char is not '*'
            return first_char_match and self.isMatch(text[1:], pattern[1:])  


# DP
# Top-Down Variation (still recursion)
class Solution2():
    def isMatch(self, text, pattern):
        def dp(i, j):
            if (i, j) not in memo:               # difference is here
                if j == len(pattern):
                    ans = i == len(text)         # i, j both point to the end of str
                else:
                    first_char_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_char_match and dp(i+1, j)
                    else:
                        ans = first_char_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        memo = {}
        return dp(0, 0)


# Bottom-Up Variation
class Solution3():
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_char_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_char_match and dp[i+1][j]
                else:
                    dp[i][j] = first_char_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ == "__main__":
    from unittest import TestCase, main
    from unittest.mock import patch
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution2,), (Solution3,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("aa", "a", False),
            ("aa", "a*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("mississippi", "mis*is*p*.", False),
        ])
        def test_isMatch(self, text, pattern, expected):
            sol = self.solution()       # type:ignore
            r = sol.isMatch(text, pattern)
            self.assertEqual(r, expected)

    main()
