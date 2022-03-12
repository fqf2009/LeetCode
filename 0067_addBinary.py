# Given two binary strings a and b, return their sum as a binary string.
# Constraints:
#   1 <= a.length, b.length <= 104
#   a and b consist only of '0' or '1' characters.
#   Each string does not contain leading zeros except for the zero itself.
from itertools import zip_longest

# more pythonic
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        c = 0
        for ch1, ch2 in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            c, r = divmod(int(ch1) + int(ch2) + c, 2)
            res.append(str(r))

        if c > 0:
            res.append(str(c))
        return ''.join(reversed(res))


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        j = len(b) - 1
        carry = 0
        res = []
        for i in reversed(range(len(a))):
            n1 = int(a[i])
            n2 = int(b[j]) if j >= 0 else 0
            j -= 1
            carry, r = divmod(n1 + n2 + carry, 2)
            res.append(str(r))
        
        if carry > 0:
            res.append(str(carry))

        return ''.join(reversed(res))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.addBinary("11", "1")
        print(r)
        assert r == '100'
    
        r = sol.addBinary("1010", "1011")
        print(r)
        assert r == '10101'

    unitTest(Solution())
    unitTest(Solution1())
