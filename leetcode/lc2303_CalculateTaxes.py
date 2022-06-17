# You are given a 0-indexed 2D integer array brackets where 
# brackets[i] = [upperi, percenti] means that the ith tax bracket 
# has an upper bound of upperi and is taxed at a rate of percenti.
# The brackets are sorted by upper bound (i.e. upperi-1 < upperi 
# for 0 < i < brackets.length).
# Tax is calculated as follows:
#   The first upper0 dollars earned are taxed at a rate of percent0.
#   The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
#   The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
#   And so on.
# You are given an integer income representing the amount of money you earned. 
# Return the amount of money that you have to pay in taxes. Answers within 
# 10^-5 of the actual answer will be accepted.
# Constraints:
#   1 <= brackets.length <= 100
#   1 <= upperi <= 1000
#   0 <= percenti <= 100
#   0 <= income <= 1000
#   upperi is sorted in ascending order.
#   All the values of upperi are unique.
#   The upper bound of the last tax bracket is greater than or equal to income.
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        b0 = 0
        for b, p in brackets:
            if income > b:
                tax += (b - b0) * p / 100
            else:
                tax += (income - b0) * p / 100
                break
            b0 = b

        return tax


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.calculateTax( [[3,50],[7,10],[12,25]], income = 10)
        print(r)
        assert r == 2.65000

        r = sol.calculateTax([[1,0],[4,25],[5,50]], income = 2)
        print(r)
        assert r == 0.25

        r = sol.calculateTax([[2,50]], income = 0)
        print(r)
        assert r == 0

    unit_test(Solution())
