# Reverse bits of a given 32 bits unsigned integer.
# Note:
#   - in some languages, such as Java, there is no unsigned integer type. In this case, 
#     both input and output will be given as a signed integer type. They should not 
#     affect your implementation, as the integer's internal binary representation is 
#     the same, whether it is signed or unsigned.
#   - In Java, the compiler represents the signed integers using 2's complement notation. 
#     Therefore, in Example 2 above, the input represents the signed integer -3 and the 
#     output represents the signed integer -1073741825.


# Bit Manipulation
# - similar problem:
#   swap alternate bits in a number: (x & 0xaaaaaaaa) >> 1 | (x & 0x55555555) << 1
#   swap two bits ...
class Solution:
    def reverseBits(self, n: int) -> int:
        n = n >> 16 | n << 16
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1
        return n


class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res


class Solution2:
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
    unitTest(Solution2())
