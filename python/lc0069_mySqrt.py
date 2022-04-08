# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, 
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5.
# Constraints:
#   0 <= x <= 2^31 - 1


# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x <= 3: return 1
        left = 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            v = mid * mid
            if v == x:
                return mid
            elif v < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right


# Math - Newton's formula
class Solution1:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)


if __name__ == '__main__':
    r = Solution().mySqrt(4)
    print(r)
    assert(r == 2)

    r = Solution().mySqrt(6)
    print(r)
    assert(r == 2)

    r = Solution().mySqrt(8)
    print(r)
    assert(r == 2)

    r = Solution().mySqrt(100)
    print(r)
    assert(r == 10)

    r = Solution().mySqrt(1000)
    print(r)
    assert(r == 31)
