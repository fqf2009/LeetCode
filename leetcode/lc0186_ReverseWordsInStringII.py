# Given a character array s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by a single space.
# Your code must solve the problem in-place, i.e. without
# allocating extra space.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
#   There is at least one word in s.
#   s does not contain leading or trailing spaces.
#   All the words in s are guaranteed to be separated by a single space.
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse(i, j):
            if i < j:
                for k in range((j - i + 1) // 2):
                    s[i + k], s[j - k] = s[j - k], s[i + k]

        n = len(s)
        reverse(0, n - 1)

        i = 0
        for j in range(n):
            if j < n - 1 and s[j + 1] == " " or j == n - 1 and s[j] != " ":
                reverse(i, j)
                i = j + 2


class Solution1:
    def reverseWords(self, s: List[str]) -> None:
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        n = len(s)
        reverse(0, n - 1)

        i = 0
        for j in range(n):
            if s[j] == " ":
                reverse(i, j - 1)
                i = j + 1
            elif j == n - 1:
                reverse(i, j)


if __name__ == "__main__":

    def unit_test(sol):
        s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
        sol.reverseWords(s)
        print(s)
        assert s == ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]

        s = ["a"]
        r = sol.reverseWords(s)
        print(s)
        assert s == ["a"]

    unit_test(Solution())
    unit_test(Solution1())
