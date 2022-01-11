# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#   Symbol       Value
#   I             1
#   V             5
#   X             10
#   L             50
#   C             100
#   D             500
#   M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as 
# XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
# four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
# subtract it making four. The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9. 
#   X can be placed before L (50) and C (100) to make 40 and 90. 
#   C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
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
        i = j = res = 0
        while i < len(s):
            while not s[i:].startswith(romanValue[j][0]):
                j += 1
                if j >= len(romanValue):
                    raise ValueError(f'{s} is not a valid roman number.')
            res += romanValue[j][1]
            i += len(romanValue[j][0])

        return res


class Solution1:
    def romanToInt(self, s: str) -> int:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i, pos, res = 0, 0, 0
        while pos < len(s) and i < len(symbols):
            while not s[pos:].startswith(symbols[i]):
                i += 1
                if i >= len(symbols):
                    raise ValueError(f'{s} is not a valid roman number.')
            res = res + values[i]
            pos += len(symbols[i])

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.romanToInt('III')
        print(r)
        assert(r == 3)

        r = sol.romanToInt('IV')
        print(r)
        assert(r == 4)

        r = sol.romanToInt('IX')
        print(r)
        assert(r == 9)

        r = sol.romanToInt('LVIII')
        print(r)
        assert(r == 58)

        r = sol.romanToInt('MCMXCIV')
        print(r)
        assert(r == 1994)

    unitTest(Solution())
    unitTest(Solution1())
