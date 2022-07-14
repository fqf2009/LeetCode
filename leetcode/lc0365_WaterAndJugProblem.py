# You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
# There is an infinite amount of water supply available. Determine whether it
# is possible to measure exactly targetCapacity liters using these two jugs.
# If targetCapacity liters of water are measurable, you must have targetCapacity
# liters of water contained within one or both buckets by the end.
# Operations allowed:
# - Fill any of the jugs with water.
# - Empty any of the jugs.
# - Pour water from one jug into another till the other jug is completely full,
#   or the first jug itself is empty.
# Constraints:
#   1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
from collections import deque
import math


# Math
# Bézout's identity - https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
#                   - https://zh.wikipedia.org/wiki/%E8%B2%9D%E7%A5%96%E7%AD%89%E5%BC%8F
# Analysis:
# - let ax + by = m, in what condition of m, there exists integer solution of x, y?
# - the answer is: m % gcd(a, b) == 0
# - proof:
#       assume, g = gcd(a, b)
#       then,   a/g and b/g are both integer
#       then,   a/g*x and b/g*y are both integer
#       then,   a/g*x + b/g*y == m/g
#       so,     m/g is integer, so m % g == 0
# - proof (by contradiction):
#       assume,  there exists integer solution of x, y
#       assume,  g = gcd(a, b), m % g != 0
#       then,    m / g is not an integer
#       however, a/g*x + b/g*y is integer
#       so,      a/g*x + b/g*y != m/g
#       then,    a*x + b*y != m
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        a, b, m = jug1Capacity, jug2Capacity, targetCapacity
        return m <= a + b and m % math.gcd(a, b) == 0


# BFS
class Solution1:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        j1, j2, tg = jug1Capacity, jug2Capacity, targetCapacity
        if j1 > j2:
            j1, j2 = j2, j1

        if tg > j1 + j2:
            return False

        dq = deque([(0, 0)])
        visited = set([(0, 0)])     # !!! note: set((0, 0)) == {0} !!!
        while dq:
            x, y = dq.popleft()
            if x + y == tg:
                return True

            states = set()
            states.add((j1, y))  # fill jar 1
            states.add((x, j2))  # fill jar 2
            states.add((0, y))  # empty jar 1
            states.add((x, 0))  # empty jar 2
            states.add((min(j1, x + y), 0 if y < j1 - x else y - (j1 - x)))  # pour jar2 to jar1
            states.add((0 if x < j2 - y else x - (j2 - y), min(j2, x + y)))  # pour jar1 to jar2

            for state in states:
                if not state in visited:
                    dq.append(state)
                    visited.add(state)

        return False


# BFS
# - to get min steps and detailed steps
class Solution2:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        j1, j2, tg = jug1Capacity, jug2Capacity, targetCapacity
        if j1 > j2:
            j1, j2 = j2, j1

        if tg > j1 + j2:
            return False

        def printSteps(dq, i):
            x, y, parent, desc = dq[i]
            if parent != -1:
                printSteps(dq, parent)
            print(f"{desc:20}: ({x}, {y})")


        dq = [[0, 0, -1, "Initial State"]]  # x, y, parent_step, description
        idx = 0
        visited = set([(0, 0)])
        while idx < len(dq):
            x, y, _, _ = dq[idx]
            if x + y == tg or x == tg or y == tg:
                printSteps(dq, idx)
                return True

            states = []
            states.append([j1, y, "Fill jar 1"])
            states.append([x, j2, "Fill jar 2"])
            states.append([0, y, "Empty jar 1"])
            states.append([x, 0, "Empty jar 2"])
            states.append([min(j1, x + y), 0 if y < j1 - x else y - (j1 - x), "Pour jar 2 => 1"])
            states.append([0 if x < j2 - y else x - (j2 - y), min(j2, x + y), "Pour jar 1 => 2"])

            for x, y, desc in states:
                if not (x, y) in visited:
                    dq.append([x, y, idx, desc])
                    visited.add((x, y))

            idx += 1

        return False


if __name__ == "__main__":

    def unitTest(solution):
        print()
        print(solution.__name__)

        sol = solution()
        r = sol.canMeasureWater(3, 5, 4)
        print(r)
        assert r == True

        r = sol.canMeasureWater(2, 6, 5)
        print(r)
        assert r == False

        r = sol.canMeasureWater(1, 2, 3)
        print(r)
        assert r == True

    unitTest(Solution)
    unitTest(Solution1)
    unitTest(Solution2)
