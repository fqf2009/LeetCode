# Given two integers num and k, consider a set of positive 
# integers with the following properties:
#   The units digit of each integer is k.
#   The sum of the integers is num.
# Return the minimum possible size of such a set, or -1 if 
# no such set exists.
# Note:
# The set can contain multiple instances of the same integer, 
# and the sum of an empty set is considered 0.
# The units digit of a number is the rightmost digit of the number.
# Constraints:
#   0 <= num <= 3000
#   0 <= k <= 9


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        # if k == 0: return -1 if num % 10 != 0 else 1
        for i in range(1, 11):
            if k * i % 10 == num % 10 and k * i <= num:
                return i
        return -1


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.minimumNumbers(58, k = 9)
        print(r)
        assert r == 2

        r = sol.minimumNumbers(37, k = 2)
        print(r)
        assert r == -1

        r = sol.minimumNumbers(0, 7)
        print(r)
        assert r == 0

        r = sol.minimumNumbers(2, 8)
        print(r)
        assert r == -1

        r = sol.minimumNumbers(32, 8)
        print(r)
        assert r == 4

        r = sol.minimumNumbers(10, 8)
        print(r)
        assert r == -1

    unit_test(Solution())
