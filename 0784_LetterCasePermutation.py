# Given a string s, you can transform every letter individually 
# to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return 
# the output in any order.
# Constraints:
#   1 <= s.length <= 12
#   s consists of lowercase English letters, uppercase English letters, and digits.
from typing import List


# Backtracking
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def nextPos(i: int) -> int:
            while i < n - 1:
                i += 1
                if not ('0' <= s[i] <= '9'):
                    return i
            return -1

        def prevPos(i: int) -> int:
            while i > 0:
                i -= 1
                if not ('0' <= s[i] <= '9'):
                    return i
            return -1

        n = len(s)
        res = []
        cmb = [x if '0' <= x <= '9' else '$' + str.lower(x) for x in s]
        i = nextPos(-1)
        if i == -1: return [s]
        while i >= 0:
            if cmb[i][0] == '$':
                cmb[i] = cmb[i][1]
            elif 'a' <= cmb[i] <= 'z':
                cmb[i] = str.upper(cmb[i])
            else:
                cmb[i] = '$' + str.lower(cmb[i])
                i = prevPos(i)
                continue

            i = nextPos(i)
            if i == - 1:
                res.append(''.join(cmb))
                i = prevPos(n)

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.letterCasePermutation("12345")
        print(r)
        assert sorted(r) == sorted(["12345"])

        r = sol.letterCasePermutation("a1b2")
        print(r)
        assert sorted(r) == sorted(["a1b2","a1B2","A1b2","A1B2"])

        r = sol.letterCasePermutation("3z4")
        print(r)
        assert sorted(r) == sorted(["3z4","3Z4"])

    unit_test(Solution())
