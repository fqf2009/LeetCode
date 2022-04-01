# # Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling 
# large integers (such as BigInteger). You must also not convert the inputs to 
# integers directly.
#
# Constraints:
#   1 <= num1.length, num2.length <= 10^4
#   num1 and num2 consist of only digits.
#   num1 and num2 don't have any leading zeros except for the zero itself.
from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        for c1, c2 in zip_longest(reversed(num1), reversed(num2)):
            d1 = ord(c1) - ord('0') if c1 is not None else 0
            d2 = ord(c2) - ord('0') if c2 is not None else 0
            carry, val = divmod(d1 + d2 + carry, 10)
            res.append(val)
        
        if carry > 0 or len(res) == 0:
            res.append(carry)

        return ''.join(chr(x + ord('0')) for x in res[::-1])


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.addStrings("11", "123")
        print(r)
        assert r == "134"

        r = sol.addStrings("99", "99")
        print(r)
        assert r == "198"

        r = sol.addStrings("456", "77")
        print(r)
        assert r == "533"

        r = sol.addStrings("0", "0")
        print(r)
        assert r == "0"

    unit_test(Solution())
