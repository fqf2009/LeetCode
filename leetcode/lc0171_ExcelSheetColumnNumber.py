# Given a string columnTitle that represents the column title as appears
# in an Excel sheet, return its corresponding column number.
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
#   1 <= columnTitle.length <= 7
#   columnTitle consists only of uppercase English letters.
#   columnTitle is in the range ["A", "FXSHRXW"].
from functools import reduce


# - Base-26 encoding, however, the index is 1-based, not 0-based.
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            res = (res * 26) + ord(ch) - ord('A') + 1  # 1-based, so plus 1

        return res


# One-liner
class Solution1:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda a, b: a*26+b, (ord(ch) - ord('A') + 1 for ch in columnTitle))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ("A", 1),
                ("AB", 28),
                ("ZY", 701),
                ("FXSHRXW", 2147483647)
            ]
        )
        def test_titleToNumber(self, columnTitle, expected):
            sol = self.solution()  # type:ignore
            r = sol.titleToNumber(columnTitle)
            self.assertEqual(r, expected)

    main()
