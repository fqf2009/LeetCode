# You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1>
# and <num2> represent positive integers.
# Add a pair of parentheses to expression such that after the addition of parentheses,
# expression is a valid mathematical expression and evaluates to the smallest possible
# value. The left parenthesis must be added to the left of '+' and the right parenthesis
# must be added to the right of '+'.
# Return expression after adding a pair of parentheses such that expression evaluates
# to the smallest possible value. If there are multiple answers that yield the same
# result, return any of them.
# The input has been generated such that the original value of expression, and the
# value of expression after adding any pair of parentheses that meets the
# requirements fits within a signed 32-bit integer.
# Constraints:
#   3 <= expression.length <= 10
#   expression consists of digits from '1' to '9' and '+'.
#   expression starts and ends with digits.
#   expression contains exactly one '+'.
#   The original value of expression, and the value of expression after adding any
#   pair of parentheses that meets the requirements fits within a signed 32-bit integer.


class Solution:
    def minimizeResult(self, expression: str) -> str:
        s1, s2 = expression.split("+")
        res = ""
        maxval = 2**31
        for i in range(len(s1)):
            s11, s12 = s1[:i], s1[i:]
            v1 = 1 if s11 == "" else int(s11)
            v2 = int(s12)
            for j in range(len(s2)):
                s21, s22 = s2[: j + 1], s2[j + 1 :]
                v3 = int(s21)
                v4 = 1 if s22 == "" else int(s22)
                val = v1 * (v2 + v3) * v4
                if val < maxval:
                    maxval = val
                    res = s11 + "(" + s12 + "+" + s21 + ")" + s22

        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ("247+38", "2(47+38)"), 
            ("12+34", "1(2+3)4"), 
            ("999+999", "(999+999)")
        ])
        def test_minimizeResult(self, expression, expected):

            sol = self.solution()  # type:ignore
            r = sol.minimizeResult(expression)
            self.assertEqual(r, expected)

    main()
