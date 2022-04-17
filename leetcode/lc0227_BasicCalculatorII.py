# Given a string s which represents an expression, evaluate this expression 
# and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate 
# results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval().
# Constraints:
#   1 <= s.length <= 3 * 10^5
#   s consists of integers and operators ('+', '-', '*', '/') separated by 
#       some number of spaces.
#   s represents a valid expression.
#   All the integers in the expression are non-negative integers in the range [0, 2^31-1].
#   The answer is guaranteed to fit in a 32-bit integer.
from itertools import chain


# Optimization - for only two priority levels (among operators)
# Algorithm:
# - scan through every char in s:
# - res is to accumulate results; !!!
# - v1, oper, v2 is the previous 3 items, when encountering a new operator; !!!
# - if new char is digit, calculate v2, continue the scan;
# - if new char is '+' or '-', accumulate v1 to res, and then
#   set v1 = v2, or v1 = -v2 accordingly;
# - if new char is '*' or '/', i.e., with higher priority,
#   set v1 = v1 * v2, or v1 = int(v1 / v2) accordingly;
# - after v1 is set, set v2 to 0, oper to new operator, continue the scan;
class Solution:
    def calculate(self, s: str) -> int:
        res, v1, oper, v2 = 0, 0, '+', 0
        for ch in chain(s, '+'):
            if ch == ' ':
                continue
            if ch.isdigit():
                v2 = v2*10 + int(ch)
                continue
            if oper == '+': # oper is the previous operator, ch is new operator
                res += v1
                v1 = v2
            elif oper == '-':
                res += v1
                v1 = -v2
            elif oper == '*':
                v1 = v1 * v2
            elif oper == '/':
                v1 = int(v1 / v2)   # v1//v2 is wrong, because: -(3//4) == 0, -3//4 == -1
            v2 = 0
            oper = ch

        return res + v1


# Stack: T/S: O(n), O(1) - space is constant, not O(1)
# - general implementation, support more operators
class Solution1:
    def calculate(self, s: str) -> int:
        op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
        stack = []

        def compress_stack(next_op = None):
            while len(stack) >= 2 and (
                    next_op is None or op_priority[stack[-2]] >= op_priority[next_op]):
                oprand2, operator = stack.pop(), stack.pop()
                oprand1 = stack.pop() if stack else 0
                if operator == '+':
                    res = oprand1 + oprand2
                elif operator == '-':
                    res = oprand1 - oprand2
                elif operator == '*':
                    res = oprand1 * oprand2
                elif operator == '/':
                    res = oprand1 // oprand2
                elif operator == '^':
                    res = oprand1 ** oprand2
                else:
                    raise Exception('Invalid Operator')
                stack.append(res)

        val = 0
        for ch in chain(s, '+'):    # append an operator with lowest priority
            if ch.isdigit():
                val = val*10 + int(ch)
            elif ch in op_priority:
                stack.append(val)
                compress_stack(ch)
                stack.append(ch)
                val = 0

        return stack[0]


if __name__ == '__main__':
    def unit_test1(sol):
        r = sol.calculate("1*2-3/4+5*6-7*8+9/10")
        print(r)
        assert r == -24

        r = sol.calculate("-3+2*2")
        print(r)
        assert r == 1

        r = sol.calculate("3+2*2")
        print(r)
        assert r == 7

        r = sol.calculate(" 3/2 ")
        print(r)
        assert r == 1

        r = sol.calculate(" 3+5 / 2 ")
        print(r)
        assert r == 5

    def unit_test2(sol):
        r = sol.calculate("- 3 - 2 * 3 ^ 2")
        print(r)
        assert r == -21

    unit_test1(Solution())
    unit_test1(Solution1())
    unit_test2(Solution1())
