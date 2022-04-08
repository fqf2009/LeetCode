# You are given an array of strings equations that represent relationships
# between variables where each string equations[i] is of length 4 and takes 
# one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are 
# lowercase letters (not necessarily different) that represent one-letter 
# variable names.

# Return true if it is possible to assign integers to variable names so as 
# to satisfy all the given equations, or false otherwise.

# Constraints:
#   1 <= equations.length <= 500
#   equations[i].length == 4
#   equations[i][0] is a lowercase letter.
#   equations[i][1] is either '=' or '!'.
#   equations[i][2] is '='.
#   equations[i][3] is a lowercase letter.
from typing import List


# Union Find - T/S: O(n), O(n)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = {}

        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for e in equations:
            if e[1:3] == '==':
                uf[find(e[0])] = find(e[3])
        
        for e in equations:
            if e[1:3] == '!=':
                if find(e[0]) == find(e[3]):
                    return False
        
        return True


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.equationsPossible(["a==b","b!=a"])
        print(r)
        assert r == False

        r = sol.equationsPossible(["b==a","a==b"])
        print(r)
        assert r == True
        
    unitTest(Solution())
