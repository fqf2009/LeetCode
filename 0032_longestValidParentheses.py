# Given a string containing just the characters '(' and ')', find the
# length of the longest valid (well-formed) parentheses substring.


# Counting - T/S: O(n), O(1)
# Analysis:
# - first, from left to right:
#   scan through string, count the number of '(' and ')' using nLeft, nRight.
#   Any time nLeft < nRight, i.e. substring like ")" or "())" appear, which
#   can never become valid again, so we reset the counter to 0.
#   therefore, if nLeft == nRight, current substring is valid.
# - Why need to do it again from right to left?
#   take this example: "()((())", at the end, nLeft == 3, nRight == 2.
#   if from right to left, at middle, there is nLeft == 2, nRight == 2,
#   so we can record the maxLen as 2.
# - Can we just count one time from left to right? No!!!
#   e.g.: "()(()", there is no chance to reset counter, so at the end,
#   when nLeft == 3, nRight == 2, if the 2*nRight is not the max length
#   for valid substring.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def maxLenMatched(s: str, reversed: bool = False) -> int:
            maxLen, nLeft, nRight = 0, 0, 0
            for ch in s:
                if (ch == '(' and not reversed) or (ch == ')' and reversed):
                    nLeft += 1
                else:
                    nRight += 1

                if nLeft == nRight:
                    maxLen = max(maxLen, 2 * nLeft)
                elif nLeft < nRight:    # reset
                    nLeft = nRight = 0

            return maxLen

        return max(maxLenMatched(s), maxLenMatched(s[::-1], True))


# Stack - T/S: O(n), O(n)
# - Clear stack if more ')' encountered than '('
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        maxLen, unmatchedLeft = 0, 0
        for ch in s:
            if ch == '(':
                stk.append(ch)
                unmatchedLeft += 1
            elif unmatchedLeft == 0:
                stk.clear()
            else:
                nLen = 0
                foundMatch = False
                while stk and (not foundMatch or stk[-1] != '('):
                    topItem = stk.pop()
                    if topItem == '(':
                        foundMatch = True
                        unmatchedLeft -= 1
                        nLen += 2
                    else:
                        nLen += topItem

                stk.append(nLen)
                maxLen = max(maxLen, nLen)

        return maxLen


# Use a special stack, which can store '(', ')', and numbers (length of
#   valid parentheses ever matched), in other language, use special value,
#   such as -1, -2 to represent parentheses.
# for each char in s:
#  - if it is '(', push into stack, also keep the number of unmatched '('
#  - if it is ')': if nUnmatchedLeft > 0, peek item stack:
#                      if ')', skip;
#                      else pop item from stack:
#                          if item is number, accumulate it,
#                          if '(', accumulate 2,
#                          repeat until the second '(', or ')' or
#                          empty stack, push number into stack.
#                  else push ')', i.e., break the connection between items
#                       in stack and future items, clear stack is another
#                       option, may be better.
# Time complexity: O(n); Space complexity O(n)
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        maxLen, unmatchedLeft = 0, 0
        for ch in s:
            if ch == '(':
                stk.append(ch)
                unmatchedLeft += 1
            elif unmatchedLeft == 0:
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
                            unmatchedLeft -= 1
                            nLen += 2
                    else:
                        nLen += topItem
                    stk.pop()

                stk.append(nLen)
                maxLen = max(maxLen, nLen)

        return maxLen


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
    unitTest(Solution2())
