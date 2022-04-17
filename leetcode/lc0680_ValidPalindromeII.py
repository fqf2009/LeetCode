# Given a string s, return true if the s can be palindrome after deleting
# at most one character from it.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of lowercase English letters.

from xmlrpc.client import Boolean

# T/S: O(n), O(1), even in worst case, because only one char can be deleted
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(lo: int, hi: int, can_delete: bool) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return (can_delete and 
                            (is_valid(lo + 1, hi, False) or 
                            is_valid(lo, hi - 1, False)))
                lo += 1
                hi -= 1
            return True

        return is_valid(0, len(s) - 1, True)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.validPalindrome('aba')
        print(r)
        assert r == True

        r = sol.validPalindrome("abca")
        print(r)
        assert r == True

        r = sol.validPalindrome("abc")
        print(r)
        assert r == False

    unitTest(Solution())
