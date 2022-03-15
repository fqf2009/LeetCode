# A message containing letters from A-Z can be encoded into numbers
# using the following mapping:
#   'A' -> "1"
#   'B' -> "2"
#   ...
#   'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then
# mapped back into letters using the reverse of the mapping above
# (there may be multiple ways). For example, "11106" can be mapped into:
#   "AAJF" with the grouping (1 1 10 6)
#   "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be
# mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways
# to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.
# Constraints:
#   1 <= s.length <= 100
#   s contains only digits and may contain leading zero(s).
from functools import cache


# DP - T/S: O(n), O(n)
# - use int type as cache key is better than str
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(pos: int):
            if pos == n:
                return 1
            if s[pos] == '0':
                return 0
            if pos == n - 1:
                return 1
            return dp(pos+1) + (dp(pos+2) if int(s[pos:pos+2]) <= 26 else 0)

        return dp(0)


if __name__ == '__main__':
    def numDecodings(sol):
        r = sol.numDecodings("12")
        print(r)
        assert r == 2

        r = sol.numDecodings("226")
        print(r)
        assert r == 3

        r = sol.numDecodings("06")
        print(r)
        assert r == 0

    numDecodings(Solution())
