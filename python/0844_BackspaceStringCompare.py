# Given two strings s and t, return true if they are equal when both
# are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Constraints:
#   1 <= s.length, t.length <= 200
#   s and t only contain lowercase letters and '#' characters.
# Follow up: Can you solve it in O(n) time and O(1) space?
from itertools import zip_longest


# T/S: O(n), O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reverseIter(s: str):
            skip = 0
            for ch in reversed(s):
                if ch == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield ch
        
        return all(x == y for x, y in zip_longest(reverseIter(s), reverseIter(t)))


# T/S: O(n), O(n)
class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            res = []
            for ch in s:
                if ch == '#':
                    if res:
                        res.pop()
                else:
                    res.append(ch)
            return ''.join(res)

        return build(s) == build(t)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.backspaceCompare(s="y#fo##f", t="y#f#o##f")
        print(r)
        assert r == True

        r = sol.backspaceCompare(s="ab#c", t="ad#c")
        print(r)
        assert r == True

        r = sol.backspaceCompare(s="ab##", t="c#d#")
        print(r)
        assert r == True

        r = sol.backspaceCompare(s = "a#c", t = "b")
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
