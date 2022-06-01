# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#   "123"
#   "132"
#   "213"
#   "231"
#   "312"
#   "321"
# Given n and k, return the kth permutation sequence.
# Constraints:
#   1 <= n <= 9
#   1 <= k <= n!
from functools import reduce
import math


# https://en.wikipedia.org/wiki/Factorial_number_system
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        # factorial = math.factorial(n)
        factorial = reduce(lambda x, y: x * y, range(1, n + 1))  # n!

        # compute factorial representation of k
        v = k - 1
        res = []
        for i in reversed(range(1, n + 1)):
            factorial //= i  # from (n-1)! to (0)!
            idx = v // factorial
            v -= idx * factorial
            res.append(nums[idx])
            del nums[idx]

        return "".join(str(x) for x in res)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.getPermutation(3, 3)
        print(r)
        assert r == "213"

        r = sol.getPermutation(4, 9)
        print(r)
        assert r == "2314"

        r = sol.getPermutation(3, 1)
        print(r)
        assert r == "123"

    unitTest(Solution())
