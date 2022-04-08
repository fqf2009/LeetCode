# Given a string s, return true if a permutation of the string could form a palindrome.
# Constraints:
#   1 <= s.length <= 5000
#   s consists of only lowercase English letters.
from typing import Counter


# Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(x % 2 for x in Counter(s).values()) < 2


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.canPermutePalindrome("code")
        print(r)
        assert r == False

        r = sol.canPermutePalindrome("aab")
        print(r)
        assert r == True

        r = sol.canPermutePalindrome("carerac")
        print(r)
        assert r == True

    unit_test(Solution())
