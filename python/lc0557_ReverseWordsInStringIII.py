# Given a string s, reverse the order of characters in each word within a 
# sentence while still preserving whitespace and initial word order.
# Constraints:
#   1 <= s.length <= 5 * 104
#   s contains printable ASCII characters.
#   s does not contain any leading or trailing spaces.
#   There is at least one word in s.
#   All the words in s are separated by a single space.

# Python's str is immutable
# split and join is much concise or pythonic than two pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        return ' '.join([x[::-1] for x in words])


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.reverseWords(s = "Let's take LeetCode contest")
        print(r)
        assert r == "s'teL ekat edoCteeL tsetnoc"

        r = sol.reverseWords(s = "God Ding")
        print(r)
        assert r == "doG gniD"

    unitTest(Solution())
