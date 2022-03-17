# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.
# Constraints:
#   2 <= asteroids.length <= 10^4
#   -1000 <= asteroids[i] <= 1000
#   asteroids[i] != 0
from typing import List


# Stack: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for v in asteroids:
            while stk and stk[-1] > 0 and v < 0: # be careful: stk[-1]*v < 0 is not correct
                if abs(v) == abs(stk[-1]):
                    stk.pop()
                    break
                elif abs(v) > abs(stk[-1]):
                    stk.pop()
                else:
                    break
            else:
                stk.append(v)

        return stk


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.asteroidCollision([-2, -1, 1, 2])
        print(r)
        assert r == [-2, -1, 1, 2]

        r = sol.asteroidCollision([5, 10, -5])
        print(r)
        assert r == [5, 10]

        r = sol.asteroidCollision([8, -8])
        print(r)
        assert r == []

        r = sol.asteroidCollision([10, 2, -5])
        print(r)
        assert r == [10]

    unitTest(Solution())
