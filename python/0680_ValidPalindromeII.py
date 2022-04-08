# Given a string s, return true if the s can be palindrome after deleting
# at most one character from it.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of lowercase English letters.

from xmlrpc.client import Boolean

# T/S: O(n), O(1), even in worst case, because only one char can be deleted
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeWithDelete(left: int, right: int, canDeleteChar: bool) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return (canDeleteChar and 
                            (validPalindromeWithDelete(left + 1, right, False) or 
                            validPalindromeWithDelete(left, right - 1, False)))
                left += 1
                right -= 1
            return True

        return validPalindromeWithDelete(0, len(s) - 1, True)


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
