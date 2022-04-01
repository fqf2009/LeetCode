# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
# Constraints:
#   -100.0 < x < 100.0
#   -2^31 <= n <= 2^31-1
#   -10^4 <= xn <= 10^4

# Iteration: O(log(n))
# Analysis:
# - res = x^n
# - if n is represented in biniary form:
#   n = (n0)*2^0 + (n1)*2^1 + ... + (nm)*2^m
#       here n0, n1, ..., nm are either 1 or 0
# - n % 2 is n0;
#   (n // 2) % 2 is n1;
#   ...
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        product = x
        while n > 0:
            if n % 2 > 0:
                res *= product
            product *= product
            n //= 2

        return res


# Recursion: O(log(n))
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n >= 2:
            q, r = divmod(n, 2)
            res = self.myPow(x, q)
            res *= res
            return res*x if r > 0 else res
        else: # n < 0:
            return 1/self.myPow(x, -n)


if __name__ == "__main__":
    def unitTest(sol):
        r = Solution().myPow(2, 10)
        print(r)
        assert r== 1024

        r = Solution().myPow(2.1, 3)
        print(r)
        assert r== 9.261000000000001

        r = Solution().myPow(2, -2)
        print(r)
        assert r== 0.25

    unitTest(Solution())
    unitTest(Solution1())
