# Given a string s, find the longest palindromic 
# subsequence's length in s.
# A subsequence is a sequence that can be derived from 
# another sequence by deleting some or no elements without 
# changing the order of the remaining elements.

# Constraints:
#   1 <= s.length <= 1000
#   s consists only of lowercase English letters.
from functools import cache

# DP + Memo
# - Palindrome and String
# - Time complexity: Best scenario: O(n), Worst: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i > j: return 0
            if s[i] == s[j]:
                return dp(i+1, j-1) + 1 if i == j else dp(i+1, j-1) + 2
            else:
                return max(dp(i+1, j), dp(i, j-1), dp(i+1, j-1))
            
        return dp(0, len(s)-1)
        
        
if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestPalindromeSubseq("bbbab")
        print(r)
        assert r == 4

        r = sol.longestPalindromeSubseq("cbbd")
        print(r)
        assert r == 2

    unitTest(Solution())
