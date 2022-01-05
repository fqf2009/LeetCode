# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

# Recursion
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {'2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return [x for x in dic[digits]]
        cmb = self.letterCombinations(digits[:-1])
        return [ x + y for x in cmb for y in dic[digits[-1]]]

# Backtracking
class Solution1:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {'2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return res
        pos = [0] * len(digits)
        cmb =''
        i = 0
        while i >= 0:
            if pos[i] < len(dic[digits[i]]):
                cmb = cmb[:i] + dic[digits[i]][pos[i]]
                pos[i] += 1
                if len(cmb) == len(digits):
                    res.append(cmb)
                else:
                    i += 1
            else:
                pos[i] = 0
                i -= 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.letterCombinations('')
        print(r)
        assert(sorted(r) == [])

        r = sol.letterCombinations('9')
        print(r)
        assert(sorted(r) == ['w', 'x', 'y', 'z'])

        r = sol.letterCombinations('23')
        print(r)
        assert(sorted(r) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

        r = sol.letterCombinations('234')
        print(r)
        assert(sorted(r) == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi',
                            'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 
                            'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi'])

        r = sol.letterCombinations('2349')
        print(r)

    unitTest(Solution())
    unitTest(Solution1())
