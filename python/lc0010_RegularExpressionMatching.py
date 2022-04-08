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
#   there will be a previous valid character to match.

# Code from LeetCode website
# Approach 1: Recursion

# Without a Kleene star (*), our solution would look like this:
# def match(text, pattern):
#     if not pattern: return not text
#     first_match = bool(text) and pattern[0] in {text[0], '.'}
#     return first_match and match(text[1:], pattern[1:])
#
# If a star is present in the pattern
class Solution1(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':                     # with '*'
            return (self.isMatch(text, pattern[2:]) or                  # '[any_char]*' match zero text[0]
                    first_match and self.isMatch(text[1:], pattern))    # (text[0] | '.') + '*' match 1 text[0], and continue...
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])  # without '*'


# Code from LeetCode website
# Approach 2: Dynamic Programming
# Top-Down Variation (still recursion)
class Solution2(object):
    def isMatch(self, text, pattern):
        def dp(i, j):
            if (i, j) not in memo:               # difference is here
                if j == len(pattern):
                    ans = i == len(text)         # i, j both point to the end of str
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        memo = {}
        return dp(0, 0)


# Code from LeetCode website
# Bottom-Up Variation
class Solution3(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.isMatch(text="aa", pattern="a")
        print(r)
        assert r == False

        r = sol.isMatch(text="aa", pattern="a*")
        print(r)
        assert r == True

        r = sol.isMatch("ab", pattern=".*")
        print(r)
        assert r == True

        r = sol.isMatch(text="aab", pattern="c*a*b")
        print(r)
        assert r == True

        r = sol.isMatch(text="mississippi", pattern="mis*is*p*.")
        print(r)
        assert r == False

        print('')

    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
