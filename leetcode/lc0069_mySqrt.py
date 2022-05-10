# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.
# Constraints:
#   0 <= x <= 2^31 - 1


# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        left = 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            v = mid * mid
            if v == x:
                return mid
            elif v < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# Math - Newton's formula
class Solution1:
    def mySqrt(self, x):
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)


# Math - Newton's formula
# - for float type
class Solution2:
    def mySqrt(self, x: float) -> float:
        def isGoodEnough(guess: float) -> bool:
            return abs(guess * guess - x) / x < 0.0000001

        def improve(guess: float):
            return (guess + x / guess) / 2

        def sqrtIter(guess: float) -> float:
            return guess if isGoodEnough(guess) else sqrtIter(improve(guess))

        return sqrtIter(1.0)


if __name__ == "__main__":

    def unit_test(solution):
        sol = solution()

        r = sol.mySqrt(4)
        print(r)
        assert r == 2

        r = sol.mySqrt(6)
        print(r)
        assert r == 2

        r = sol.mySqrt(8)
        print(r)
        assert r == 2

        r = sol.mySqrt(100)
        print(r)
        assert r == 10

        r = sol.mySqrt(1000)
        print(r)
        assert r == 31

    def unit_test2(solution):
        sol = solution()

        r = sol.mySqrt(64.0)
        print(r)
        assert abs(r - 8.0) < 0.000001

        r = sol.mySqrt(1.0)
        print(r)
        assert abs(r - 1.0) < 0.000001

        r = sol.mySqrt(10.0)
        print(r)
        assert abs(r - 3.1622776602) < 0.000001

        r = sol.mySqrt(.5)
        print(r)
        assert abs(r - 0.7071067812) < 0.000001

    unit_test(Solution)
    unit_test(Solution1)
    unit_test2(Solution2)
