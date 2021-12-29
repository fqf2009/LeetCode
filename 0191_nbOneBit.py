# Write a function that takes an unsigned integer and returns the number of '1' bits it 
# has (also known as the Hamming weight).

# Note:
# - in some languages, such as Java, there is no unsigned integer type. In this case, 
#   the input will be given as a signed integer type. It should not affect your 
#   implementation, as the integer's internal binary representation is the same, 
#   whether it is signed or unsigned.
# - In Java, the compiler represents the signed integers using 2's complement notation. 
#   Therefore, in Example 3, the input represents the signed integer. -3.


class Solution:
    def hammingWeight(self, n: int) -> int:
        nb1bit = 0
        while n > 0:
            nb1bit += 1
            n &= n - 1  # From right to left, clear one '1' at a time
        
        return nb1bit


if __name__ == "__main__":
    r = Solution().hammingWeight(0b00000000000000000000000000001011)
    print(r)
    assert(r == 3)

    r = Solution().hammingWeight(0b00000000000000000000000010000000)
    print(r)
    assert(r == 1)

    r = Solution().hammingWeight(0b11111111111111111111111111111101)
    print(r)
    assert(r == 31)
