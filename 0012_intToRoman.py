# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#   Symbol       Value
#   I             1
#   V             5
#   X             10
#   L             50
#   C             100
#   D             500
#   M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
# which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, 
# the numeral for four is not IIII. Instead, the number four is written as IV. Because 
# the one is before the five we subtract it making four. The same principle applies to 
# the number nine, which is written as IX. There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9. 
#   X can be placed before L (50) and C (100) to make 40 and 90. 
#   C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


class Solution:
    def intToRoman(self, num: int) -> str:
        romanValue = [('M', 1000),
                      ('CM', 900),
                      ('D', 500),
                      ('CD', 400),
                      ('C', 100),
                      ('XC', 90),
                      ('L', 50),
                      ('XL', 40),
                      ('X', 10),
                      ('IX', 9),
                      ('V', 5),
                      ('IV', 4),
                      ('III', 3),
                      ('II', 2),
                      ('I', 1)]
        res = ''
        i = 0
        while num > 0:
            while romanValue[i][1] > num:
                i += 1
            res += romanValue[i][0]
            num -= romanValue[i][1]

        return res


class Solution1:
    def intToRoman(self, num: int) -> str:
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        i = 0
        while num > 0:
            while values[i] > num:
                i += 1
            num -= values[i]
            res += symbols[i]

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.intToRoman(3)
        print(r)
        assert(r == 'III')

        r = sol.intToRoman(4)
        print(r)
        assert(r == 'IV')

        r = sol.intToRoman(9)
        print(r)
        assert(r == 'IX')

        r = sol.intToRoman(58)
        print(r)
        assert(r == 'LVIII')

        r = sol.intToRoman(1994)
        print(r)
        assert(r == 'MCMXCIV')

    unitTest(Solution())
    unitTest(Solution1())
    