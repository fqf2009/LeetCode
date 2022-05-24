# Given an integer columnNumber, return its corresponding column
#  title as it appears in an Excel sheet.
# For example:
#   A -> 1
#   B -> 2
#   C -> 3
#   ...
#   Z -> 26
#   AA -> 27
#   AB -> 28 
#   ...
# Constraints:
#     1 <= columnNumber <= 2^31 - 1


# - Base-26 encoding, but the index is 1-based, not 0-based.
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber
        res = []
        while c > 0:
            c, r = divmod(c - 1, 26)
            res.append(chr(ord('A') + r))
            
        return ''.join(reversed(res))


class Solution1:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber
        res = []
        while c > 0:
            c -= 1
            res.append(chr(ord('A') + c % 26 ))
            c //= 26

        return ''.join(reversed(res))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                (1, "A"),
                (28, "AB"),
                (701, "ZY"),
                (2147483647, "FXSHRXW")
            ]
        )
        def test_convertToTitle(self, columnTitle, expected):
            sol = self.solution()  # type:ignore
            r = sol.convertToTitle(columnTitle)
            self.assertEqual(r, expected)

    main()
