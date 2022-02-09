# Given a string s, return the longest palindromic substring in s

# There are much efficient way: Manacher's algorithm: O(n)
# https://en.wikipedia.org/wiki/Longest_palindromic_substring


# use two pointers to point to the center of palindrome, this works for
# both odd or even length of palindrome strings.
# Time complexity: O(n^2)

# slight change: just use poiner, defer string manipulation until return
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def maxPallindromeAt(p1: int, p2: int):
            pdLen = 0
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                pdLen = p2 - p1 + 1
                p1 -= 1
                p2 += 1
            return pdLen
    
        maxLen = 1
        pdStart = 0
        for i in range(len(s) - 1):
            pdLen = max(maxPallindromeAt(i, i), maxPallindromeAt(i, i + 1))
            if pdLen > maxLen:
                maxLen = pdLen
                pdStart = i - (pdLen - 1) // 2
                
        return s[pdStart: pdStart + maxLen]


# Expand around the center: T/S: O(n^2), O(1)
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        # p1, p2 pointing to the center of palindrome
        def palindromeLength(p1: int, p2: int) -> int:
            size = 0
            while p1 >= 0 and p2 < len(s):
                if s[p1] != s[p2]:
                    return size
                size = p2 - p1 + 1
                p1 -= 1
                p2 += 1
            return size

        res = s[0]
        for i in range(len(s)):
            sz = palindromeLength(i, i)
            if sz > len(res):
                res = s[i - sz // 2: i - sz // 2 + sz]
            if i + 1 < len(s):
                sz = palindromeLength(i, i + 1)
                if sz > len(res):
                    res = s[i + 1 - sz // 2: i + 1 - sz // 2 + sz]
        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = Solution().longestPalindrome('babad')
        print(r)
        assert(r == 'bab' or r == 'aba')

        r = Solution().longestPalindrome('cbbd')
        print(r)
        assert(r == 'bb')

        r = Solution().longestPalindrome('a')
        print(r)
        assert(r == 'a')

        r = Solution().longestPalindrome('ac')
        print(r)
        assert(r == 'a' or r == 'c')

    unitTest(Solution())
    unitTest(Solution1())
