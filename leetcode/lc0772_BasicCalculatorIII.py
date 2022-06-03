# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers,
# '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
# Note: You are not allowed to use any built-in function which evaluates
#       strings as mathematical expressions, such as eval().
# Constraints:
#   1 <= s <= 10^4
#   s consists of digits, '+', '-', '*', '/', '(', and ')'.
#   s is a valid expression.


# Stack + Recursion
from itertools import chain


class Solution:
    def calculate(self, s: str) -> int:
        def calc(pos):
            def update_stack(op, v):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    # In python: -3 // 2 == -2, not -1 (also -3 % 2 == 1)
                    #            int(-3 / 2) == -1
                    # stack.append(stack.pop() // v)
                    stack.append(int(stack.pop() / v))

            stack = []
            v, op = 0, "+"
            while pos < len(s):
                ch = s[pos]
                if s[pos].isdigit():
                    v = v * 10 + int(ch)
                elif ch in "+-*/)":
                    update_stack(op, v)
                    if ch == ")":
                        return sum(stack), pos
                    else:
                        v, op = 0, ch
                elif ch == "(":
                    v, pos = calc(pos + 1)
                pos += 1

            update_stack(op, v)
            return sum(stack), pos

        return calc(0)[0]


# Stack + Recursion: T/S: O(n), O(1) - space is constant, not O(1)
# - general solution, support more operators
# - future improvement: ???
#   priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': 3, ')': 0} +
#              {'==': 0, '<': 0, '>': 0, '<=': 0, '>=': 0, '?': 0, ':': 0}
class Solution1:
    def calculate(self, s: str) -> int:
        priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, ')': 0}

        def calc(pos):
            stack = []
            def compress_stack(next_op = None):
                while len(stack) >= 2 and (
                        next_op is None or priority[stack[-2]] >= priority[next_op]):
                    v2, op = stack.pop(), stack.pop()
                    v1 = stack.pop() if stack else 0
                    if op == '+':
                        v1 += v2
                    elif op == '-':
                        v1 -= v2
                    elif op == '*':
                        v1 *= v2
                    elif op == '/':
                        # v1//v2 is wrong, because in Python:-3//4 == -1,
                        # but -(3//4) == 0, int(-3 / 4) == 0
                        v1 = int(v1 / v2)
                    elif op == '^':
                        v1 **= v2
                    stack.append(v1)

            v = 0
            while pos < len(s):
                ch = s[pos]
                if ch.isdigit():
                    v = v*10 + int(ch)
                elif ch == "(":
                    v, pos = calc(pos + 1)
                elif ch in priority:
                    stack.append(v)
                    compress_stack(ch)
                    if ch == ")":
                        return stack[0], pos
                    else:
                        stack.append(ch)
                        v = 0
                pos += 1

            stack.append(v)
            compress_stack('+')
            return stack[0], pos

        return calc(0)[0]


if __name__ == "__main__":

    def unit_test1(solution):
        print(solution.__name__)
        sol = solution()

        r = sol.calculate("(0-3)/4")
        print(r)
        assert r == 0

        r = sol.calculate(" 5 - 3 / 2")
        print(r)
        assert r == 4

        r = sol.calculate("1 + 1")
        print(r)
        assert r == 2

        r = sol.calculate("-3+2-2")
        print(r)
        assert r == -3

        r = sol.calculate(" 2-1 + 2 ")
        print(r)
        assert r == 3

        r = sol.calculate(" (1+(4+5+2) -3)+(6 +8) ")
        print(r)
        assert r == 23

        r = sol.calculate(" (1-(4+ 5+2)+3)+(6+8) ")
        print(r)
        assert r == 7

        r = sol.calculate(" 2*(5+5 *2)/3+( 6 /2+8) ")
        print(r)
        assert r == 21

    unit_test1(Solution)
    unit_test1(Solution1)
