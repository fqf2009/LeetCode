# Given an integer n, return true if it is a power of two. 
# Otherwise, return false.
# An integer n is a power of two, if there exists an 
# integer x such that n == 2x.

# Constraints:
#   -231 <= n <= 231 - 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n - 1 & n) == 0


class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n % 2 == 0:
            n >>= 1
        return n == 1


class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            if n != (n >> 1) << 1:
                return False
            n >>= 1
        return True


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.isPowerOfTwo(1)
        print(r)
        assert r == True

        r = sol.isPowerOfTwo(16)
        print(r)
        assert r == True

        r = sol.isPowerOfTwo(3)
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
