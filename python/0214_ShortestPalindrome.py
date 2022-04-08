# You are given a string s. You can convert s to a palindrome
# by adding characters in front of it.
# Return the shortest palindrome you can find by performing
# this transformation.

# KMP (Knuth–Morris–Pratt) algorithm: O(n)
#  - palindrome string means if it is reversed, it is the same as original.
#  - so we construct a new string: s + "#" + reversed(s),
#    if there is a palindrome prefix in s, then this palindrome is
#    the suffix in reversed(s).
#  - e.g.: "aacecaaa" has a palindrome prefix "aacecaa", the reversed(s),
#          i.e., "aaacecaa" has a palindrome suffix "aacecaa"
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        s1 = s + '#' + s[::-1]
        n = len(s1)
        lps = [0] * n
        for i in range(1, n):
            t = lps[i-1]
            while t > 0 and s1[t] != s1[i]:
                t = lps[t-1]
            if s1[t] == s1[i]:
                t += 1
            lps[i] = t

        t = lps[n-1]
        return s[t:][::-1] + s


# O(n^2) - Time exceeded!
# Analysis:
# - can only add char at front, not back.
# - if s is already palindrome, nothing to do.
# - so the problem is to find longest first portion in string,
#   and it is a palindrome.
class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[-1-i]:
                    return False
            return True

        n = len(s)
        if n == 0:
            return s
        palLen = 1
        for i in reversed(range(1, n)):
            if isPalindrome(s[:i+1]):
                palLen = i + 1
                break

        return s[palLen:][::-1] + s


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.shortestPalindrome(s="")
        print(r)
        assert r == ""

        r = sol.shortestPalindrome(s="aacecaaa")
        print(r)
        assert r == "aaacecaaa"

        r = sol.shortestPalindrome(s="abcd")
        print(r)
        assert r == "dcbabcd"

        s = "a" * 20000 + "cd" + "a" * 20000
        r = sol.shortestPalindrome(s)
        print(r)
        assert r == "a" * 20000 + "dc" + s

    unitTest(Solution())
    # unitTest(Solution1())     # too slow, take about 10s
