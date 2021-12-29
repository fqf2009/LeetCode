# Reverse bits of a given 32 bits unsigned integer.
# Note:
#   - in some languages, such as Java, there is no unsigned integer type. In this case, 
#     both input and output will be given as a signed integer type. They should not 
#     affect your implementation, as the integer's internal binary representation is 
#     the same, whether it is signed or unsigned.
#   - In Java, the compiler represents the signed integers using 2's complement notation. 
#     Therefore, in Example 2 above, the input represents the signed integer -3 and the 
#     output represents the signed integer -1073741825.


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res


class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in reversed(range(32)):
            res += (n & 1) << i
            n = n >> 1
            if n == 0:
                break
        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.reverseBits(0b00000010100101000001111010011100)
        print(r)
        assert(r == 0b00111001011110000010100101000000)

        r = sol.reverseBits(0b11111111111111111111111111111101)
        print(r)
        assert(r == 0b10111111111111111111111111111111)
    
    unitTest(Solution())
    unitTest(Solution1())