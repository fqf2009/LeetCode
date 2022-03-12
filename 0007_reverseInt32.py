# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
# the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(x)[::-1]) if x >= 0 else -self.reverse(-x)
        if res > 2**31 - 1 or res < -(2**31):
            return 0
        return res


class Solution1:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
            
        res = 0
        while x > 0:
            x, r = divmod(x, 10)
            res = res * 10 + r
        
        if res > 2**31 - 1 or res < -(2**31):
            return 0
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        n = sol.reverse(123)
        print(n)
        assert n == 321

        n = sol.reverse(-123)
        print(n)
        assert n == -321

        n = sol.reverse(120)
        print(n)    
        assert n == 21

        n = sol.reverse(8463847412)
        print(n)
        assert n == 0

        n = sol.reverse(-8463847412)
        print(n)
        assert n == 0

    unitTest(Solution())
    unitTest(Solution1())
