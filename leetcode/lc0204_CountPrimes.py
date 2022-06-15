# Given an integer n, return the number of prime numbers that are
# strictly less than n.
# Constraints:
#   0 <= n <= 5 * 10^6
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False

        return isPrime[2:].count(True)


def allPrimes(n) -> list[int]:
    isPrime = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
                j += 1

    return [i for i in range(2, n + 1) if isPrime[i]]


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.countPrimes(10)
        print(r)
        assert r == 4

        r = sol.countPrimes(20)
        print(r)
        assert r == 8

        # r = sol.countPrimes(5*10**6)
        # print(r)
        # assert(r == 348513)

    unit_test(Solution())

    print(allPrimes(100))
