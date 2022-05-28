# Given two integers representing the numerator and denominator of a 
# fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in 
# parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 
# 10^4 for all the given inputs.
# Constraints:
#   -2^31 <= numerator, denominator <= 2^31 - 1
#   denominator != 0


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, d = numerator, denominator
        res = [] if numerator * denominator >= 0 else ["-"]
        n = -n if n < 0 else n
        d = -d if d < 0 else d

        res.append(str(n // d))
        r = (n % d) * 10
        recur = {}
        if r > 0:
            res.append('.')
        while r > 0:
            recur[r] = len(res)
            res.append(str(r // d))
            r = (r % d) * 10
            if (r in recur):
                return "".join(res[:recur[r]]) + '(' + "".join(res[recur[r]:]) + ")"

        return "".join(res)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.fractionToDecimal(-1, -2147483648)
        print(r)
        assert r == "0.0000000004656612873077392578125"

        r = sol.fractionToDecimal(-50, 8)
        print(r)
        assert r == "-6.25"

        r = sol.fractionToDecimal(1, 2)
        print(r)
        assert r == "0.5"

        r = sol.fractionToDecimal(2, 1)
        print(r)
        assert r == "2"

        r = sol.fractionToDecimal(4, 333)
        print(r)
        assert r == "0.(012)"


    unit_test(Solution())
