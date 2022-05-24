# Given an integer n, return the number of prime numbers that are 
# strictly less than n.
# Constraints:
#   0 <= n <= 5 * 10^6
import math


def countPrimes(n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False

        return isPrime[2:].count(True)

if __name__ == "__main__":
    r = countPrimes(10)
    print(r)
    assert(r == 4)

    r = countPrimes(20)
    print(r)
    assert(r == 8)

    r = countPrimes(5*10**6)
    print(r)
    assert(r == 348513)
