# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated
# by a single space.
# Note that s may contain leading or trailing spaces or multiple
# spaces between two words. The returned string should only have a
# single space separating the words. Do not include any extra spaces.
# Constraints:
#   1 <= s.length <= 10^4
#   s contains English letters (upper-case and lower-case), digits,
#   and spaces ' '.
#   There is at least one word in s.
# Follow-up: If the string data type is mutable in your language,
# can you solve it in-place with O(1) extra space?


# O(n), O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


# simulate for some language with mutalbe string to achieve O(1) space
class Solution1:
    def reverseWords(self, s: str) -> str:
        def reverse_list(lst: list, l: int, r: int):
            for i in range((r + 1 - l) // 2):
                lst[l+i], lst[r-i] = lst[r-i], lst[l+i]

        lst = list(s)
        n = len(lst)
        reverse_list(lst, 0, n-1)

        i = 0
        while True:
            while i < n and lst[i] == ' ':
                i += 1
            if i == n: break
            p1 = i
            while i < n and lst[i] != ' ':
                i += 1
            p2 = i - 1
            reverse_list(lst, p1, p2)
            if i == n: break

        i, j = 0, 0
        while j < n:
            while j < n and lst[j] == ' ': j += 1   # skip spaces
            while j < n and lst[j] != ' ':          # keep non-space
                lst[i] = lst[j]
                i += 1
                j += 1
            while j < n and lst[j] == ' ': j += 1   # skip spaces
            if j < n:
                lst[i] = ' '                        # keep one space in between
                i += 1

        return "".join(lst[:i])


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.reverseWords("the sky is blue")
        print(r)
        assert r == "blue is sky the"

        r = sol.reverseWords("  hello world  ")
        print(r)
        assert r == "world hello"

        r = sol.reverseWords("a good   example")
        print(r)
        assert r == "example good a"

    unit_test(Solution())
    unit_test(Solution1())
