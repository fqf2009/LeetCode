# A parentheses string is a non-empty string consisting only of '(' and ')'. 
# It is valid if any of the following conditions is true:
#  - It is ().
#  - It can be written as AB (A concatenated with B), where A and B are valid 
#    parentheses strings.
#  - It can be written as (A), where A is a valid parentheses string.
# You are given an m x n matrix of parentheses grid. A valid parentheses 
# string path in the grid is a path satisfying all of the following conditions:
#  - The path starts from the upper left cell (0, 0).
#  - The path ends at the bottom-right cell (m - 1, n - 1).
#  - The path only ever moves down or right.
#  - The resulting parentheses string formed by the path is valid.
# Return true if there exists a valid parentheses string path in the grid. 
# Otherwise, return false.
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 100
#   grid[i][j] is either '(' or ')'.
from collections import defaultdict
from functools import cache
from typing import List


# DP using defaultdict - T/S: O(mn(m+n)), O(mn(m+n))
# - not as fast as DFS, which return true when first path is found.
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (n+m) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        # use set() to save delta (nLeftParenthesis - nRightParenthesis)
        dp = defaultdict(set)
        dp[0, -1] = dp[-1, 0] = {0}
        for i in range(m):
            for j in range(n):
                diff = 1 if grid[i][j] == '(' else -1
                dp[i, j] |= {x + diff for x in (dp[i-1, j] | dp[i, j-1])
                                        if x + diff >= 0 and x + diff <= (m+n) / 2}

        return 0 in dp[m-1, n-1]


# DP - T/S: O(mn(m+n)), O(mn(m+n))
class Solution1:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (n+m) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        
        # use set() to save delta (nLeftParenthesis - nRightParenthesis)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                diff = 1 if grid[i][j] == '(' else -1
                for a in dp[i-1][j] if i else []: 
                    if a + diff >= 0:
                        dp[i][j].add(a+diff)                
                for a in dp[i][j-1] if j else []:
                    if a + diff >= 0:
                        dp[i][j].add(a+diff)

        return 0 in dp[-1][-1]


# Backtracking (or DFS)
# use memo to avoid TLE
class Solution2:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        # total length is (m+n-1), so m+n should be odd.
        if (n+m) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        @cache
        def dfs(i, j, delta):
            if i == m or j == n: return False

            delta += 1 if grid[i][j] == '(' else -1
            if delta < 0 or delta > (n+n) / 2:
                return False

            if i == m - 1 and j == n - 1:
                return delta == 0

            return dfs(i, j+1, delta) or dfs(i+1, j, delta)

        return dfs(0, 0, 0)


# Backtracking: Time Limit Exceed
# T/S: O(Combination(m+n, m)), O(m+n)
class Solution3:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        # total length is (m+n-1), so m+n should be odd.
        if (n+m) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        def backtrack(i, j, left, right):
            if i == m or j == n: return False

            if grid[i][j] == '(':
                left += 1
            else:
                right += 1

            if left < right:
                return False

            if i == m - 1 and j == n - 1:
                return left == right

            return backtrack(i, j+1, left, right) or backtrack(i+1, j, left, right)

        return backtrack(0, 0, 0, 0)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.hasValidPath([['(','(','('],
                              [')','(',')'],
                              ['(','(',')'],
                              ['(','(',')']])
        print(r)
        assert r == True

        r = sol.hasValidPath([[')',')'],
                              ['(','(']])
        print(r)
        assert r == False

        r = sol.hasValidPath([
        ['(',')',')','(','(','(','(',')',')','(',')','(',')','(','(','(','(',')','(',')','('],
        ['(','(',')',')','(',')',')',')','(',')','(',')','(','(',')','(','(','(','(','(',')'],
        [')',')','(',')',')','(','(',')','(','(',')','(',')',')','(',')',')','(','(',')',')'],
        ['(','(',')','(',')','(',')',')',')','(',')','(','(',')','(',')',')','(',')',')',')'],
        ['(','(','(',')','(','(',')','(',')',')','(',')',')',')',')',')',')','(',')','(','('],
        [')',')','(','(',')',')',')',')',')','(',')',')',')','(','(',')','(','(','(','(',')'],
        [')',')',')',')','(',')','(',')','(','(',')','(','(',')','(','(',')',')','(',')','('],
        ['(',')','(','(','(',')',')',')',')','(','(',')','(','(',')',')','(',')',')',')','('],
        ['(',')','(',')','(','(','(','(',')','(','(','(','(','(','(',')','(',')','(',')',')'],
        ['(',')','(','(','(',')','(',')',')',')',')','(','(','(','(',')',')','(','(','(',')'],
        ['(','(',')','(',')',')','(',')','(',')',')',')',')',')','(',')','(',')',')',')','('],
        [')','(','(','(',')','(',')',')','(',')','(',')','(','(',')','(','(',')','(','(',')'],
        ['(',')','(',')',')','(','(',')','(',')','(',')',')',')','(','(','(','(',')','(',')'],
        ['(','(',')','(',')',')','(','(','(',')','(',')','(','(',')',')','(','(','(',')',')'],
        ['(','(','(','(',')',')','(',')','(','(','(',')',')','(',')','(',')',')',')',')','('],
        ['(','(','(',')',')',')','(',')',')','(',')',')','(','(',')','(',')','(','(','(',')'],
        [')',')',')',')',')',')','(',')',')',')','(','(',')','(',')','(','(','(','(',')',')']])
        print(r)
        assert r == False

        r = sol.hasValidPath(
        [['(','(',')','(',')','(','(',')','(','(',')',')',')',')',')','(',')','(','(',')','(','(',')',')',')',')',')','(','(','(','('],
         [')','(','(','(',')','(',')','(','(',')',')',')',')','(',')',')','(','(',')',')','(',')','(',')','(','(',')','(',')','(','('],
         [')',')','(','(',')','(','(',')',')',')',')','(','(',')',')','(',')','(',')',')','(','(','(',')',')',')','(',')',')','(',')'],
         ['(','(',')','(',')','(','(',')','(','(','(',')',')','(',')','(',')',')',')',')',')',')','(','(',')','(',')','(',')','(','('],
         [')',')','(',')',')','(','(','(',')',')','(',')','(',')',')',')','(','(','(',')',')','(',')','(',')',')','(','(','(','(',')'],
         [')',')','(','(',')','(',')','(',')','(',')','(',')',')','(',')','(',')',')','(',')','(','(','(',')','(',')',')',')','(','('],
         [')','(','(','(','(','(','(',')',')','(','(',')','(',')',')','(',')',')',')','(','(','(',')','(','(',')',')','(',')','(',')'],
         [')',')','(','(','(','(','(','(','(',')',')','(','(','(','(','(','(','(','(','(','(','(','(',')',')','(','(',')',')','(',')'],
         ['(',')',')',')','(','(',')',')',')',')','(',')',')','(',')',')','(','(','(','(','(','(','(',')',')','(','(',')',')','(','('],
         ['(','(',')','(',')',')',')',')','(','(','(',')',')',')','(',')','(','(',')','(','(','(',')','(','(','(','(','(',')',')',')'],
         ['(',')','(','(','(','(',')','(','(',')',')','(','(',')','(','(','(',')','(','(','(',')',')','(',')',')','(',')','(','(',')'],
         [')',')','(','(','(','(',')','(','(',')',')','(',')',')','(',')','(','(','(','(','(','(','(',')','(','(',')',')','(','(','('],
         ['(',')',')',')','(',')','(','(','(',')',')',')','(',')','(',')',')','(','(','(','(',')','(',')',')',')',')',')',')','(','('],
         ['(','(','(','(','(','(',')',')','(',')','(','(','(',')',')','(',')','(',')','(',')','(','(','(',')',')',')','(',')','(','('],
         ['(',')',')',')',')','(','(',')',')',')',')',')',')','(','(',')','(',')',')','(',')','(',')',')',')','(','(',')','(','(','('],
         ['(',')',')','(','(',')',')','(',')',')','(','(','(',')',')',')',')','(','(','(',')',')','(',')','(','(','(','(',')',')',')'],
         [')','(','(',')','(','(',')',')',')','(','(','(','(',')','(',')',')',')','(',')','(',')','(','(',')','(','(','(','(','(','('],
         ['(',')','(',')','(','(',')',')',')',')',')','(','(',')',')','(',')','(',')',')',')',')','(','(','(',')','(',')','(',')',')'],
         ['(',')','(',')',')',')','(','(','(',')','(',')','(','(',')',')','(',')','(',')','(',')','(','(','(','(','(',')','(',')','('],
         [')',')',')',')',')','(',')',')','(','(',')','(',')',')','(',')',')','(','(','(','(',')','(','(','(','(',')',')',')',')','('],
         [')','(','(','(','(','(',')','(',')',')',')',')','(','(','(',')',')','(',')',')','(','(','(','(','(','(',')',')','(','(','('],
         ['(','(','(',')',')','(',')','(',')',')',')',')','(',')',')',')',')','(',')','(','(','(','(',')','(','(','(','(','(','(',')']])
        print(r)
        assert r == False

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
