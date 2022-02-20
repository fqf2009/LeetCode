from typing import List
from math import sqrt


def getPrimes(n: int) -> List[int]:
    primes = [2]
    for i in range(3, n + 1):
        for p in primes:
            if p * p > i:
                primes.append(i)
                break
            if i % p == 0:
                break
    return primes


def getFactors(n: int) -> List[int]:
    fac = []
    primes = getPrimes(int(sqrt(n)))
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            fac.append(primes[i])
            n = n // primes[i]
        else:
            i += 1
    return fac


def getDivisors(n: int) -> List[int]:
    div = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            div.append(i)
        if i * i < n:
            div.append(n // i)
        i += 1
    return div


if __name__ == '__main__':
    r = getPrimes(100)
    print(r)
    assert r == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    r = getFactors(100)
    print(r)
    assert r == [2, 2, 5, 5]

    r = sorted(getDivisors(12))
    print(r)
    assert r == [1, 2, 3, 4, 6, 12]
