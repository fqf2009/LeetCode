# A parentheses string is valid if and only if:
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis
# at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))"
# or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
# Constraints:
#   1 <= s.length <= 1000
#   s[i] is either '(' or ')'.


# Counting
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        nLeft = nRight = 0
        res = 0
        for ch in s:
            if ch == "(":
                nLeft += 1
            else:
                nRight += 1
            if nRight > nLeft:
                res += 1
                nRight -= 1

        return res + nLeft - nRight


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.minAddToMakeValid("())")
        print(r)
        assert r == 1

        r = sol.minAddToMakeValid("(((")
        print(r)
        assert r == 3

    unitTest(Solution())
