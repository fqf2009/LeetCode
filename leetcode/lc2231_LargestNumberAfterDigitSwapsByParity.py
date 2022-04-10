# You are given a positive integer num. You may swap any two digits of num that
# have the same parity (i.e. both odd digits or both even digits).
# Return the largest possible value of num after any number of swaps.
# Constraints:
#   1 <= num <= 10^9


class Solution:
    def largestInteger(self, num: int) -> int:
        odds = sorted([x for x in str(num) if int(x) % 2 == 1], reverse=True)
        evens = sorted([x for x in str(num) if int(x) % 2 == 0], reverse=True)
        i, j = 0, 0
        res = []
        for ch in str(num):
            if int(ch) % 2 == 1:
                res.append(odds[i])
                i += 1
            else:
                res.append(evens[j])
                j += 1

        return int("".join(res))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            (1234, 3412), 
            (65875, 87655),
        ])
        def test_largestInteger(self, num, expected):
            sol = self.solution()  # type:ignore
            r = sol.largestInteger(num)
            self.assertEqual(r, expected)

    main()
