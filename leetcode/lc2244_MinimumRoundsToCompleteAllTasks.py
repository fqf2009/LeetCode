# You are given a 0-indexed integer array tasks, where tasks[i] represents 
# the difficulty level of a task. In each round, you can complete either 
# 2 or 3 tasks of the same difficulty level.
# Return the minimum rounds required to complete all the tasks, 
# or -1 if it is not possible to complete all the tasks.
# Constraints:
#   1 <= tasks.length <= 10^5
#   1 <= tasks[i] <= 10^9
from typing import Counter, List


# Counter + Math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        res = 0
        for freq in counter.values():
            if freq == 1:
                return -1
            q, r = divmod(freq, 3)
            if r == 0:
                res += q
            else:
                res += q + 1

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
        print(r)
        assert r == 4

        r = sol.minimumRounds([2, 3, 3])
        print(r)
        assert r == -1

        r = sol.minimumRounds([4, 4, 4])
        print(r)
        assert r == 1

    unit_test(Solution())
