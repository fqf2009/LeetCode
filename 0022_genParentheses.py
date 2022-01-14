# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.

# Recursion + Stack
# stk is a special stack, which represents string of n pairs of parentheses
# - left, right are the number of '(', ')' in the stack
# - only when left < n, a '(' can be pushed into stack
# - only when right < left, a ')' can be pushed into stack
# - when stack has 2*n items, collect result
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def genPar(stk = [], left = 0, right = 0):
            if len(stk) == 2*n:
                res.append(''.join(stk))
                return
            if left < n:
                stk.append('(')
                genPar(stk, left+1, right)
                stk.pop()
            if left > right:
                stk.append(')')
                genPar(stk, left, right+1)
                stk.pop()

        res = []
        genPar()
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
