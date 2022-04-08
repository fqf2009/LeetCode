# You are given an integer num. Rearrange the digits of num such that 
# its value is minimized and it does not contain any leading zeros.

# Return the rearranged number with minimal value.

# Note that the sign of the number does not change after rearranging 
# the digits.

from typing import List

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        if num < 0:
            sign = -1
            digits = sorted(str(-num), reverse=True)
        else:
            sign = 1
            digits = sorted(str(num))
            for i in range(len(digits)):
                if digits[i] != '0':
                    if i > 0:
                        digits[0] = digits[i]
                        digits[i] = '0'
                    break

        return sign * int(''.join(digits))


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.smallestNumber(310)
        print(r)
        assert r == 103

        r = sol.smallestNumber(-7605)
        print(r)
        assert r == -7650

    unit_test(Solution())
