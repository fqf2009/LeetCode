# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
# s consists of parentheses only '()[]{}'

# Stack
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for x in s:
            if x in pairs:
                stack.append(x)
            elif len(stack) == 0 or pairs[stack.pop()] != x:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.isValid('[')
        print(r)
        assert(not r)

        r = sol.isValid('()')
        print(r)
        assert(r)

        r = sol.isValid('()[]{}')
        print(r)
        assert(r)

        r = sol.isValid('(]')
        print(r)
        assert(not r)

        r = sol.isValid('([)]')
        print(r)
        assert(not r)

        r = sol.isValid('{[]}')
        print(r)
        assert(r)

    unitTest(Solution())
