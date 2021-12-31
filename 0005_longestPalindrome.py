# Given a string s, return the longest palindromic substring in s

# There are much efficient way: Manacher's algorithm: O(n)
# https://en.wikipedia.org/wiki/Longest_palindromic_substring


# use two pointers to point to the center of palindrome, this works for
# both odd or even length of palindrome strings.
# Time complexity: O(n^2)
class Solution:
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
