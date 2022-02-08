from functools import cache

# Recursion, DP, Memo: O(n)
class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Iteration
class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        n1, n2, f = 0, 1, 0
        for _ in range(n-1):
            f = n1 + n2
            n1, n2 = n2, f
        return f

    
if __name__ == '__main__':
    def unitTest(sol):
        r = sol.fib(2)
        print(r)
        assert r == 1

        r = sol.fib(3)
        print(r)
        assert r == 2

        r = sol.fib(4)
        print(r)
        assert r == 3

        r = sol.fib(5)
        print(r)
        assert r == 5

    unitTest(Solution())
    unitTest(Solution1())
