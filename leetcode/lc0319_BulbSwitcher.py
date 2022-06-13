# There are n bulbs that are initially off. You first turn on 
# all the bulbs, then you turn off every second bulb.

# On the third round, you toggle every third bulb (turning on 
# if it's off or turning off if it's on). For the ith round,
# you toggle every i bulb. For the nth round, you only toggle 
# the last bulb.

# Return the number of bulbs that are on after n rounds.
# Constraints:
#   0 <= n <= 10^9
from math import isqrt, sqrt


# Math: O(1)
# Analysis
# - A bulb ends up on if it is switched an odd number of times.
# - Call them bulb 1 to bulb n. Bulb i is switched in round d
#   if and only if d divides i. So bulb i ends up on if and 
#   only if it has an odd number of divisors.
# - Divisors come in pairs, like i=12 has divisors 1 and 12, 
#   2 and 6, and 3 and 4.
# - Except when i is a square, like 36 has divisors 1 and 36, 
#   2 and 18, 3 and 12, 4 and 9, and double divisor 6.
# - So bulb i ends up on if and only if i is a square.
# - Solution - just count the square numbers.
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return isqrt(n)


class Solution1:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.bulbSwitch(3)
        print(r)
        assert r == 1

        r = sol.bulbSwitch(0)
        print(r)
        assert r == 0

        r = sol.bulbSwitch(1)
        print(r)
        assert r == 1


    unit_test(Solution())
    unit_test(Solution1())
