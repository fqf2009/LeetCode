# Given a string s representing a valid expression, implement a basic 
# calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates 
#       strings as mathematical expressions, such as eval().
# Constraints:
#   1 <= s.length <= 3 * 10^5
#   s consists of digits, '+', '-', '(', ')', and ' '.
#   s represents a valid expression.
#   '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#   '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#   There will be no two consecutive operators in the input.
#   Every number and running calculation will fit in a signed 32-bit integer.


# Stack + Recursion
class Solution:
    def calculate(self, s: str) -> int:
        def calc(pos):
            stack = []
            v, op = 0, "+"
            while pos < len(s):
                ch = s[pos]
                if s[pos].isdigit():
                    v = v*10 + int(ch)
                elif ch in "+-)":
                    stack.append(v if op == "+" else -v)
                    if ch == ")":
                        return sum(stack), pos
                    else:
                        v, op = 0, ch
                elif ch == '(':
                    v, pos = calc(pos + 1)
                pos += 1

            stack.append(v if op == "+" else -v)
            return sum(stack), pos

        return calc(0)[0]


if __name__ == '__main__':
    def unit_test1(sol):
        r = sol.calculate("1 + 1")
        print(r)
        assert r == 2

        r = sol.calculate("-3+2-2")
        print(r)
        assert r == -3

        r = sol.calculate( " 2-1 + 2 ")
        print(r)
        assert r == 3

        r = sol.calculate(" (1+(4+5+2)-3)+(6+8) ")
        print(r)
        assert r == 23

        r = sol.calculate(" (1-(4+5+2)+3)+(6+8) ")
        print(r)
        assert r == 7


    unit_test1(Solution())
