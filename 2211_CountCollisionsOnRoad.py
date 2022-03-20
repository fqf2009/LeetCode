# There are n cars on an infinitely long road. The cars are numbered from
# 0 to n - 1 from left to right and each car is present at a unique point.
# You are given a 0-indexed string directions of length n. directions[i]
# can be either 'L', 'R', or 'S' denoting whether the ith car is moving
# towards the left, towards the right, or staying at its current point
# respectively. Each moving car has the same speed.
# The number of collisions can be calculated as follows:
# - When two cars moving in opposite directions collide with each other,
#   the number of collisions increases by 2.
# - When a moving car collides with a stationary car, the number of
#   collisions increases by 1.
# After a collision, the cars involved can no longer move and will stay at
# the point where they collided. Other than that, cars cannot change their
# state or direction of motion.
# Return the total number of collisions that will happen on the road.
from typing import List


class Solution:
    def countCollisions(self, directions: str) -> int:
        car1 = directions[0]
        res = 0
        nRight = 0  # count of 'R' left of car1, will continue to collide to the future 'S'
        for car2 in directions[1:]:
            twoCars = car1 + car2
            if twoCars == 'RL':
                res += 2 + nRight
                nRight = 0
                car1 = 'S'
            elif twoCars in ('SL', 'RS'):
                res += 1 + nRight
                nRight = 0
                car1 = 'S'
            else:
                if car1 == 'R':
                    nRight += 1
                car1 = car2

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")
        print(r)
        assert r == 20

        r = sol.countCollisions("LLSRSSRSSLLSLLLRSLSRL")
        print(r)
        assert r == 11

        r = sol.countCollisions("RLRSLL")
        print(r)
        assert r == 5

        r = sol.countCollisions("LLRR")
        print(r)
        assert r == 0

    unitTest(Solution())
