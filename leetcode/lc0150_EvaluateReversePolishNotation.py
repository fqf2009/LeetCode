# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or 
# another expression.
# Note that division between two integers should truncate toward zero.
# It is guaranteed that the given RPN expression is always valid. That
# means the expression would always evaluate to a result, and there will 
# not be any division by zero operation.
# Constraints:
#   1 <= tokens.length <= 10^4
#   tokens[i] is either an operator: "+", "-", "*", or "/", or an integer 
#   in the range [-200, 200].
from typing import List


# Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok[-1].isdigit():   # could be negative number
                stack.append(int(tok))
            else:
                op2= stack.pop()
                op1= stack.pop()
                if tok == '+':
                    val = op1 + op2
                elif tok == '-':
                    val = op1 - op2
                elif tok == '*':
                    val = op1 * op2
                else:   # tok == '/':
                    val = int(op1 / op2)    # 6 // -132 == -1, int(6/-132) == 0
                stack.append(val)
            
        return stack[0]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
            (["2","1","+","3","*"], 9),
            (["4","13","5","/","+"], 6),
        ])
        def test_evalRPN(self, tokens, expected):
            sol = self.solution()       # type:ignore
            r = sol.evalRPN(tokens)
            self.assertEqual(r, expected)

    main()
