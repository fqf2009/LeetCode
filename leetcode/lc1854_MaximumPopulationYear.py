# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] 
# indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during that year. 
# The ith person is counted in year x's population if x is in the inclusive 
# range [birthi, deathi - 1]. Note that the person is not counted in the year 
# that they die.
# Return the earliest year with the maximum population.
# Constraints:
#   1 <= logs.length <= 100
#   1950 <= birthi < deathi <= 2050
from itertools import chain
from typing import List


# Sweep Line
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prev_pop, max_pop = 0, 0
        prev_year, min_year = 0, 0
        for curr_year, delta in sorted(chain(chain.from_iterable(
                ((x, 1), (y, -1)) for x, y in logs), [(9999, 0)])):
            if curr_year != prev_year:
                if max_pop < prev_pop or min_year == 0:
                    max_pop = prev_pop
                    min_year = prev_year
            prev_year = curr_year
            prev_pop += delta

        return min_year


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[1993,1999],[2000,2010]], 1993), 
            ([[1950,1961],[1960,1971],[1970,1981]], 1960), 
            ([[1900, 1900]], 1900)
        ])
        def test_maximumPopulation(self, logs, expected):
            sol = self.solution()  # type:ignore
            r = sol.maximumPopulation(logs)
            self.assertEqual(r, expected)

    main()
