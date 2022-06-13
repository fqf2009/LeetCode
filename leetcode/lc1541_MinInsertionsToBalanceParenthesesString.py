# Given a parentheses string s containing only the characters '(' and ')'. 
# A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right 
# parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive 
# right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a 
# closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" 
# and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string 
# to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of '(' and ')' only.


class Solution:
    def minInsertions(self, s: str) -> int:
        res, diff, i = 0, 0, 0
        while i < len(s):
            if s[i] == '(':
                diff += 1
            else:
                diff -= 1
                if i + 1 < len(s) and s[i+1] == ')':    # match with '))'
                    i += 1
                else:       # match with ')'
                    res += 1
            if diff < 0:
                res -= diff
                diff = 0
            i += 1

        return res + diff * 2


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.minInsertions("(()))")
        print(r)
        assert r == 1

        r = sol.minInsertions("())")
        print(r)
        assert r == 0

        r = sol.minInsertions("))())(")
        print(r)
        assert r == 3

    unit_test(Solution())
