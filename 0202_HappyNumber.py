# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the 
# sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# Constraints:
# 1 <= n <= 2^31 - 1
 

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        nums = {n}
        while True:
            n = sum(int(x)**2 for x in str(n))
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)


class Solution1:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        nums = {n}
        while True:
            total = 0
            while n != 0:
                n, r = divmod(n, 10)
                total += r * r
            n = total
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)


if __name__ == '__main__':
    def unit_test(sol):
        r = Solution().isHappy(19)
        print(r)
        assert(r == True)

        r = Solution().isHappy(2)
        print(r)
        assert(r == False)

        r = Solution().isHappy(45)
        print(r)
        assert(r == False)

    unit_test(Solution())
    unit_test(Solution1())
