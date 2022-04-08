# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
# Return all the possible results. You may return the answer in any order.
# Constraints:
#   1 <= s.length <= 25
#   s consists of lowercase English letters and parentheses '(' and ')'.
#   There will be at most 20 parentheses in s.
from typing import List

# For future improvement:
# - make '()' pair as parameter, scan through from left to right
#   to handle the ')' removing task;
# - after getting the intermediate result set (with '(' already removed),
#   using ')(', and reversed string as parameters, call the same function, 
#   to handle the '(' removing task.
# - calculate min_left_par_to_remove for each pos to prune execution path.


# Backtracking: O(2^n), where n is number of parentheses.
# Similar problem: 1249_MinimumRemoveToMakeValidParentheses
# Analysis:
# - the objective is to remove the minimum number parentheses.
# - to remove ')', we need to scan through the string from left to right,
#   count the '(', ')' into nLeft and nRight, any time nRight > nLeft,
#   one ')' can be removed from this pos or left of this pos.
# - however, this is the minimus parentheses have to be removed till this
#   pos, not the maximus parentheses can be removed, because the future
#   excessive ')' at any pos will retroactively affect all pos before it.
# - e.g.:                          (  a  )  b  )  c  (  d  )  ) 
#   number of ')' to remove - min  0  0  0  0  1  1  1  1  1  2
#                             max  2  2  2  2  2  2  2  2  2  2
# - to remove '(', scan through from right to left, do the opposite???
# - The problem is, when any ')' is removed, the calculation for '(' is
#   different.
# - Therefore, easier solution is to just implement with the counting of
#   the max_right_par_to_remove and max_left_par_to_remove, and leave the
#   min_right_par_to_remove and min_left_par_to_remove for future improvement.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        excess_right_par = 0
        diff = 0    # nLeft - nRight
        for ch in s:
            if ch == '(':
                diff += 1
            if ch == ')':
                diff -= 1
            if diff < 0:
                diff = 0
                excess_right_par += 1

        diff = 0
        excess_left_par = 0
        for ch in reversed(s):
            if ch == ')':
                diff += 1
            if ch == '(':
                diff -= 1
            if diff < 0:
                diff = 0
                excess_left_par += 1

        s1 = list(s)
        res = set()

        def backtrack(pos, left_to_remove, right_to_remove, left_cnt, right_cnt):
            if left_to_remove < 0 or right_to_remove < 0 or right_cnt > left_cnt:
                return

            while pos < len(s1) and s1[pos] not in ('(', ')'):
                pos += 1

            if pos == len(s1):
                if left_to_remove == 0 and right_to_remove == 0 and left_cnt == right_cnt:
                    res.add(''.join(s1))
                return

            if s1[pos] == '(':
                backtrack(pos+1, left_to_remove, right_to_remove, left_cnt+1, right_cnt)
                s1[pos] = ''
                backtrack(pos+1, left_to_remove-1, right_to_remove, left_cnt, right_cnt)
                s1[pos] = '('
            else: # s1[pos] == ')'
                backtrack(pos+1, left_to_remove, right_to_remove, left_cnt, right_cnt+1)
                s1[pos] = ''
                backtrack(pos+1, left_to_remove, right_to_remove-1, left_cnt, right_cnt)
                s1[pos] = ')'

        backtrack(0, excess_left_par, excess_right_par, 0, 0)
        return list(res)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.removeInvalidParentheses("()())()")
        print(r)
        assert sorted(r) == sorted(["(())()", "()()()"])

        r = sol.removeInvalidParentheses("(a)())()")
        print(r)
        assert sorted(r) == sorted(["(a())()", "(a)()()"])

        r = sol.removeInvalidParentheses(")(")
        print(r)
        assert r == [""]

    unit_test(Solution())
