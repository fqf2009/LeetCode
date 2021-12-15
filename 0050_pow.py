# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Recursion: O(log(n))
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 2:
            q, r = divmod(n, 2)
            res = self.myPow(x, q)
            res *= res
            res = res*x if r > 0 else res
            return  res
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else: # n < 0:
            return 1/self.myPow(x, -n)


if __name__ == "__main__":
    r = Solution().myPow(2, 10)
    print(r)
    assert(r== 1024)

    r = Solution().myPow(2.1, 3)
    print(r)
    assert(r== 9.261000000000001)

    r = Solution().myPow(2, -2)
    print(r)
    assert(r== 0.25)