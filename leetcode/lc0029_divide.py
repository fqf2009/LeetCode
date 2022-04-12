# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers
#       within the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem,
#       if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
#       if the quotient is strictly less than -2^31, then return -2^31.


# Use left shift and right shift to simulate division
# O(log(n)), where n = dividend
# - e.g.: 1000 / 3
# - first left shift
#   d1  3 -> 6 -> 12 -> ... -> 1536 (until >= 1000)
#   q1  1 -> 2 -> 4  -> ... -> 512
# - then right shift
#   d1          1536 -> 768 .-> 192 .-> 24  -> 12  -> 3
#   q1          512  -> 256 .-> 64  .-> 8   -> 4   -> 1  -> 0
#   dividend    1000 -> 232  -> 40   -> 16  -> 4   -> 1
#   quotient    0    -> 256  -> 320  -> 328 -> 332 -> 333
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (1 if (dividend > 0 and divisor > 0) or
                     (dividend < 0 and divisor < 0) else -1)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient, d1, q1 = 0, divisor, 1
        while dividend > d1:
            d1 <<= 1
            q1 <<= 1

        while True:
            while dividend < d1:
                d1 >>= 1
                q1 >>= 1
            if q1 == 0:
                break
            dividend -= d1
            quotient += q1

        quotient = quotient if sign > 0 else -quotient
        quotient = -2**31 if quotient < -2**31 else quotient
        quotient = 2**31-1 if quotient > 2**31-1 else quotient
        return quotient


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.divide(1000, 3)
        print(r)
        assert(r == 333)

        r = sol.divide(10, 3)
        print(r)
        assert(r == 3)

        r = sol.divide(7, -3)
        print(r)
        assert(r == -2)

        r = sol.divide(-2**31, -1)
        print(r)
        assert(r == 2**31-1)

    unitTest(Solution())
