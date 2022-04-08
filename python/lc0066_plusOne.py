# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. The digits are
# ordered from most significant to least significant in left-to-right 
# order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Constraints:
#   1 <= digits.length <= 100
#   0 <= digits[i] <= 9
#   digits does not contain any leading 0's.
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in reversed(range(len(digits))):
            c, digits[i] = divmod(digits[i] + c, 10)
            if c == 0:
                break

        if c != 0:
            digits.insert(0, c)

        return digits


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.plusOne([1, 2, 3])
        print(r)
        assert(r == [1, 2, 4])

        r = sol.plusOne([4, 3, 2, 1])
        print(r)
        assert(r == [4, 3, 2, 2])

        r = sol.plusOne([9])
        print(r)
        assert(r == [1, 0])

        r = sol.plusOne([0])
        print(r)
        assert(r == [1])

        r = sol.plusOne([9, 9, 9])
        print(r)
        assert(r == [1, 0, 0, 0])

    unitTest(Solution())
    
