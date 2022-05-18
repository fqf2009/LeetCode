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
from itertools import accumulate, chain
from typing import List


# Sweep Line - T/S: O(n*log(n)), O(n)
# - oneliner solution
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        return -max(accumulate(([d, y] for _, d, y in sorted(
                    chain.from_iterable(((s, 1, -s), (e, -1, -e)) for s, e in logs))),
                    func = lambda a1, a2: [a1[0] + a2[0], a2[1]]))[1]


# Sweep Line - T/S: O(n*log(n)), O(n)
class Solution1:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop, max_pop = 0, 0
        prev_year, min_year = 0, 0
        for year, delta in sorted(chain(chain.from_iterable(
                ((x, 1), (y, -1)) for x, y in logs), [(9999, 0)])):
            if year != prev_year:
                if max_pop < pop or min_year == 0:
                    max_pop = pop
                    min_year = prev_year
            prev_year = year
            pop += delta

        return min_year


# Two sorted array, two poiners - T/S: O(n*log(n)), O(n)
class Solution2:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth = sorted(x for x, _ in logs)
        death = sorted(y for _, y in logs)
        i, j, pop, max_pop, res = 0, 0, 0, 0, 0
        while i < len(logs):
            if j >= len(logs) or birth[i] < death[j]:
                pop += 1
                if max_pop < pop or res == 0:
                    max_pop = pop
                    res = birth[i]
                i += 1
            else:
                pop -= 1
                j += 1

        return res


# Priority Queue??? Not working
# - similar to 0056_MeetingRoomII, however, 
#   this problem need to find out not just the max population,
#   but the earliest year of max population.
# class Solution3:
#     def maximumPopulation(self, logs: List[List[int]]) -> int:
#         pass


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,), (Solution2,)])
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
