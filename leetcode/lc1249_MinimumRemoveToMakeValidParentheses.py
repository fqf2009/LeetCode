# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses, ( '(' or ')', 
# in any positions), so that the resulting parentheses string is valid 
# and return any valid string.
# Formally, a parentheses string is valid if and only if:
# - It is the empty string, contains only lowercase characters, or
# - It can be written as "AB" (A concatenated with B), where "A" and "B"
#   are valid strings, or
# - It can be written as "(A)", where "A" is a valid string.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is either'(' , ')', or lowercase English letter.
from collections import deque
from difflib import ndiff
from typing import Iterable, List


# Counting: O(n), O(n)
# - simplify code
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def remove_unmatched(s: Iterable, pair: str) -> List[str]:
            diff = 0    # nLeft - nRight
            res = []
            for ch in s:
                if diff <= 0 and ch == pair[1]: continue    # skip unmatched right char in pair
                res.append(ch)
                if ch == pair[0]:
                    diff += 1
                elif ch == pair[1]:
                    diff -= 1
            return res

        temp = remove_unmatched(s, '()')
        return ''.join(reversed(remove_unmatched(reversed(temp), ')(')))


# Counting: O(n), O(n)
# - similar problems: 0032_longestValidParentheses
# - iterate over string, and count '(' and ')' as nLeft and nRight,
#   from left to right, any time nLeft < nRight, skip the ')',
#   from right to left, any time nLeft > nRight, skip the '('.
class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        diff = 0    # nLeft - nRight
        res1 = []
        for ch in s:
            if diff != 0 or ch != ')':
                res1.append(ch)
                if ch == '(':
                    diff += 1
                elif ch == ')':
                    diff -= 1

        diff = 0
        res2 = []
        for ch in reversed(res1):
            if diff != 0 or ch != '(':
                res2.append(ch)
                if ch == '(':
                    diff -= 1
                elif ch == ')':
                    diff += 1

        return ''. join(reversed(res2))


# Stack - T/S: O(n), O(n)
# - Algothrim:
#   - use a stack to track the unmatched '(', only to keep their index.
#   - if there is matched ')', pop up '(' from stack
#   - if there is unmatched ')', skip
#   - finally, remove the unmatched '(' from the collected items,
#     using those index from stack.
class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        res1 = []
        stk = []    # keep index of '('
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(len(res1))   # the index for '(' in res1, not s
            elif ch == ')':
                if not stk:
                    continue
                stk.pop()
            res1.append(ch)

        stk.append(len(res1))
        idx0 = 0
        res2 = []
        for idx1 in stk:
            res2.extend(res1[idx0:idx1])
            idx0 = idx1 + 1     # to skip resl[idx1]

        return ''. join(res2)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minRemoveToMakeValid("lee(t(c)o)de)")
        print(r)
        assert r == "lee(t(c)o)de" or r == "lee(t(c)ode)"

        r = sol.minRemoveToMakeValid("a)b(c)d")
        print(r)
        assert r == "ab(c)d"

        r = sol.minRemoveToMakeValid("))((")
        print(r)
        assert r == ""


    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
