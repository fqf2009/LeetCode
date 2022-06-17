from typing import List
from math import sqrt


# greatest common divisor
def my_gcd(x: int, y: int) -> int:
    return x if y == 0 else my_gcd(y, x % y)


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


# too slow, calculate all prime is unnecessary
def getFactors2(n: int) -> List[int]:
    fac = []
    primes = getPrimes(int(sqrt(n))+1)
    i, m = 0, n
    while m > 1 and i < len(primes):
        if m % primes[i] == 0:
            fac.append(primes[i])
            m = m // primes[i]
        else:
            i += 1

    if m > 1:
        fac.append(m)
    return fac


def getFactors(n: int) -> List[int]:
    m, i = n, 2
    fac = []
    while m > 1 and i <= n**0.5 + 1:
        if m % i == 0:
            fac.append(i)
            m //= i
        else:
            i += 1

    if m > 1:
        fac.append(m)
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


from itertools import chain

def base62Encode(n: int, minlen: int = 1) -> str:
    # ''.join(chr(x) for x in chain(range(ord('0'), ord('9')+1), 
    #                               range(ord('A'), ord('Z')+1), 
    #                               range(ord('a'), ord('z')+1)))
    charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    chs = []
    while n > 0:
        n, r = divmod(n, 62)
        chs.append(charset[r])

    if len(chs) == 0:
        s = '0'
    else:
        s = ''.join(chs[::-1])

    return charset[0] * max(minlen - len(s), 0) + s


def base62Decode(s: str) -> int:
    res = 0
    for ch in s:
        if '0' <= ch <= '9':
            v = ord(ch) - ord('0')
        elif 'A' <= ch <= 'Z':
            v = ord(ch) - ord('A') + 10
        elif 'a' <= ch <= 'z':
            v = ord(ch) - ord('a') + 36
        else:
            raise ValueError(f'{s} is not a valid Base 62 string!')
        res = res*62 + v

    return res


if __name__ == '__main__':
    r = my_gcd(2, 8)
    print(r)
    assert r == 2

    r = my_gcd(12, 9)
    print(r)
    assert r == 3

    r = getPrimes(100)
    print(r)
    assert r == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    r = getFactors(100)
    print(r)
    assert r == [2, 2, 5, 5]

    r = getFactors(7591)
    print(r)
    assert r == [7591]

    r = getFactors2(100)
    print(r)
    assert r == [2, 2, 5, 5]

    r = getFactors2(7591)
    print(r)
    assert r == [7591]

    r = sorted(getDivisors(12))
    print(r)
    assert r == [1, 2, 3, 4, 6, 12]

    r = base62Encode(123456789)
    print(r)
    assert r == '8M0kX'

    r = base62Encode(34441886726)
    print(r)
    assert r == 'base62'

    r = base62Decode('8M0kX')
    print(r)
    assert r == 123456789

    r = base62Decode('base62')
    print(r)
    assert r == 34441886726
