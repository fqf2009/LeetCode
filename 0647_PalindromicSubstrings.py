# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Expand around center: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPal(i: int, j: int) -> int:
            res = 0
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                res += 1
                i -= 1
                j += 1

            return res

        n, res = len(s), 0
        for i in range(n):
            res += countPal(i, i)
            if i < n - 1:
                res += countPal(i, i + 1)

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = Solution().countSubstrings('abc')
        print(r)
        assert r == 3

        r = Solution().countSubstrings('aaa')
        print(r)
        assert r == 6

        r = Solution().countSubstrings('abababba')
        print(r)
        assert r == 16

    unitTest(Solution())
