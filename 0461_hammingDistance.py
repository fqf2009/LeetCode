# The Hamming distance between two integers is the number of positions 
# at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# xor = x ^ y: (bitwise exclusive or) get an int with all bits set, if the
#              corresponding bits are different between x and y.
# xor &= (xor - 1): from right to left, each time, clear the right-most '1' bit.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        xor = x ^ y
        while xor != 0:
            dis += 1
            xor &= (xor - 1)
        
        return dis


if __name__ == '__main__':
    sol = Solution()

    n = sol.hammingDistance(0b1, 0b100)
    print(n)
    assert(n == 2)

    n = sol.hammingDistance(0b11, 0b100)
    print(n)
    assert(n == 3)
