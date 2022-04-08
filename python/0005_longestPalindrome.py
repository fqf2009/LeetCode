# Given a string s, return the longest palindromic substring in s
# Constraints:
#   1 <= s.length <= 1000
#   s consist of only digits and English letters.

# There are much efficient way: Manacher's algorithm: O(n)
# https://en.wikipedia.org/wiki/Longest_palindromic_substring


# - simplify code, i.e., let python do string comparison
# - Time Limited Exceeded - guess python did extra work during string slicing
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        p1 = p2 = 0
        maxLen = 1
        for i in range(n-1):
            for j in range(i + maxLen, n):
                k = (j - i) // 2
                if s[i:i+k+1] == s[j:j-k-1:-1]:
                    maxLen = j - i + 1
                    p1, p2 = i, j

        return s[p1: p2+1]


# Time complexity: O(n^2)
# slight change: just use poiner, defer string manipulation until return
class Solution1:
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

# use two pointers to point to the center of palindrome, this works for
# both odd or even length of palindrome strings.
# Expand around the center: T/S: O(n^2), O(1)
class Solution2:
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
        r = Solution().longestPalindrome("eabcb")
        print(r)
        assert(r == 'bcb')

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
    unitTest(Solution2())
