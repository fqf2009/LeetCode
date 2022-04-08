# Given a positive integer num, return the number of positive 
# integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.
# Constraints:
#   1 <= num <= 1000


# One liner, but hard to read
class Solution:
    def countEven(self, num: int) -> int:
        return len([v for v in range(2, num+1) if sum(int(x) for x in str(v)) % 2 == 0])


class Solution1:
    def countEven(self, num: int) -> int:
        res = 0
        for v in range(2, num+1):
            if sum(int(x) for x in str(v)) % 2 == 0:
                res += 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countEven(4)
        print(r)
        assert r == 2

        r = sol.countEven(30)
        print(r)
        assert r == 14
        
    unitTest(Solution())
    unitTest(Solution1())
