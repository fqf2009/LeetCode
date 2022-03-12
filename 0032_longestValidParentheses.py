# Given a string containing just the characters '(' and ')', find the
# length of the longest valid (well-formed) parentheses substring.


# Use a special stack, which can store '(', ')', and numbers (length of
#   valid parentheses ever matched), in other language, use special value,
#   such as -1, -2 to represent parentheses.
# for each char in s:
#  - if it is '(', push into stack, also keep the number of unmatched '('
#  - if it is ')': if nUnmatchedLeft > 0, pop item stack, if item is number,
#                      accumulate it, if '(', plus 2. until: second '(', or ')',
#                      or empty stack, push number into stack.
#                  else push ')'
# Time complexity: O(n); Space complexity O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        maxLen, nUnmatchedLeft = 0, 0
        for ch in s:
            if ch == '(':
                stk.append(ch)
                nUnmatchedLeft += 1
            elif nUnmatchedLeft == 0:
                stk.append(ch)
            else:
                nLen = 0
                foundMatch = False
                while len(stk) > 0:
                    topItem = stk[-1]
                    if topItem == ')':
                        break
                    elif topItem == '(':
                        if foundMatch:
                            break
                        else:
                            foundMatch = True
                            nUnmatchedLeft -= 1
                            nLen += 2
                    else:
                        nLen += topItem
                    stk.pop()

                stk.append(nLen)
                maxLen = max(maxLen, nLen)

        return maxLen


# From leetcode website: Count only when nLeft and nRight are the same.
# As long as do counting from both side, the result will be correct.
# Time complexity: O(n); Space complexity O(1)
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        def maxLenMatched(s: str, reversed: bool = False) -> int:
            maxLen, nLeft, nRight = 0, 0, 0
            for  ch in s:
                if ch == '(' and not reversed or ch == ')' and reversed:
                    nLeft += 1
                else:
                    nRight += 1
                
                if nLeft == nRight:
                    maxLen = max(maxLen, 2 * nLeft)
                elif nLeft < nRight:    # reset
                    nLeft = nRight = 0

            return maxLen

        return max(maxLenMatched(s), maxLenMatched(s[::-1], True))


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.longestValidParentheses("()(()")
        print(r)
        assert r == 2

        r = sol.longestValidParentheses("()((())")
        print(r)
        assert r == 4

        r = sol.longestValidParentheses("(()")
        print(r)
        assert r == 2

        r = sol.longestValidParentheses(")()())")
        print(r)
        assert r == 4

        r = sol.longestValidParentheses("")
        print(r)
        assert r == 0

        r = sol.longestValidParentheses(")()())))()(())((()))(())())")
        print(r)
        assert r == 18

    unitTest(Solution())
    unitTest(Solution1())
