# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive.
# Constraints:
#     0 <= left <= right <= 2^31 - 1


# Analysis:
# e.g. left:  1011101010101 => 0011100000000, can clear all remaining '0's
#                 ^                ^
#      right: 1011011111111
#                 ^
# - Only the leading common bits matter.
# - Any bit starting from the first mismatch bit, does not matter.
# Complexity: O(1), because max is 32, constant
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in reversed(range(32)):
            hignBitLeft = left & 2**31
            highBitRight = right & 2**31
            left <<= 1
            right <<= 1
            if hignBitLeft ^ highBitRight == 0:
                res = res * 2 + int(hignBitLeft != 0)
            else:
                return res * (2 ** (i+1))

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.rangeBitwiseAnd(10, 11)
        print(r)
        assert(r == 10)

        r = sol.rangeBitwiseAnd(5, 5)
        print(r)
        assert(r == 5)

        r = sol.rangeBitwiseAnd(2, 2)
        print(r)
        assert(r == 2)

        r = sol.rangeBitwiseAnd(5, 7)
        print(r)
        assert(r == 4)

        r = sol.rangeBitwiseAnd(0, 0)
        print(r)
        assert(r == 0)

        # 0b1111111111111111111111111111111
        r = sol.rangeBitwiseAnd(1, 2147483647)
        print(r)
        assert(r == 0)

    unitTest(Solution())