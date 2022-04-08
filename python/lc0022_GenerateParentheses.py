# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.

# Constraints:
#   1 <= n <= 8

# Backtracking + Recursion + Stack
# - backtracking template:
#   - every pos can have either '(' or ')', as long as:
#     - left parenthesis count no more than n
#     - right parenthesis count less or equal to left one
# - Another way of thinking:
#   - stk is a special stack, which represents string of n pairs of parentheses
#   - left, right are the number of '(', ')' in the stack
#   - only when left < n, a '(' can be pushed into stack
#   - only when right < left, a ')' can be pushed into stack
#   - when stack has 2*n items, collect result
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(parStk, left, right):
            if len(parStk) == 2*n:
                res.append(''.join(parStk))
                return
            if left < n:
                parStk.append('(')
                backtrack(parStk, left+1, right)
                parStk.pop()
            if left > right:
                parStk.append(')')
                backtrack(parStk, left, right+1)
                parStk.pop()

        res = []
        backtrack([], 0, 0)
        return res


# Incorrect, miss '(())(())' when n == 4
class Solution1:
    def generateParenthesis(self, n: int) -> list[str]:
        res = ['']
        for i in range(n):
            par = set()
            for x in res:
                par.add('(' + x + ')')
                par.add('()' + x)
                par.add(x + '()')
            res = list(par)

        return res


if __name__ == '__main__':
    r = Solution().generateParenthesis(3)
    print(r)
    assert(sorted(r) == ["((()))","(()())","(())()","()(())","()()()"])

    r = Solution().generateParenthesis(4)
    print(r)
    assert(sorted(r) == [
        "(((())))","((()()))","((())())","((()))()","(()(()))",
        "(()()())","(()())()","(())(())","(())()()","()((()))",
        "()(()())","()(())()","()()(())","()()()()"
    ])
