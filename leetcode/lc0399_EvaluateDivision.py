# You are given an array of variable pairs equations and an array of
# real numbers values, where equations[i] = [Ai, Bi] and values[i]
# represent the equation Ai / Bi = values[i]. Each Ai or Bi is a
# string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj]
# represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be
# determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries
#       will not result in division by zero and that there is no contradiction.
# Example 1:
#   Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
#          queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
#   Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
#   Explanation:
#   Given: a / b = 2.0, b / c = 3.0
#   queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
#   return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
#   Input: equations = [["a","b"],["b","c"],["bc","cd"]],
#          values = [1.5,2.5,5.0],
#          queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
#   Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
# Input: equations = [["a","b"]], values = [0.5],
#        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
# Constraints:
#   1 <= equations.length <= 20
#   equations[i].length == 2
#   1 <= Ai.length, Bi.length <= 5
#   values.length == equations.length
#   0.0 < values[i] <= 20.0
#   1 <= queries.length <= 20
#   queries[i].length == 2
#   1 <= Cj.length, Dj.length <= 5
#   Ai, Bi, Cj, Dj consist of lower case English letters and digits.


# https://leetcode.com/discuss/interview-question/483660/google-phone-currency-conversion
# Paramenters:
#  - array of currency conversion rates. E.g. ['USD', 'GBP', 0.77]
#    which means 1 USD is equal to 0.77 GBP
#  - an array containing a 'from' currency and a 'to' currency
# Given the above parameters, find the conversion rate that maps to the 'from'
# currency to the 'to' currency.
# Your return value should be a number.
# Example:
#   You are given the following parameters:
#   Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
#   To/From currency ['GBP', 'AUD']
#   Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.
from collections import deque
from typing import List


# Bi-directional Weighted Graph + DFS
# - T/S: O(E), O(V+E), V=>Vertices, E=>Edges
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_lst = {}
        for (a, b), v in zip(equations, values):
            adj_lst.setdefault(a, []).append((b, v))
            adj_lst.setdefault(b, []).append((a, 1 / v))

        def dfsCalc(visited, src, tgt, val) -> float:
            if src not in visited or visited[src]:
                return -1.0
            visited[src] = True
            for b, v in adj_lst[src]:
                if b == tgt:
                    return val * v
                res = dfsCalc(visited, b, tgt, val * v)
                if res > 0:
                    return res
            return -1.0

        res = []
        for a, b in queries:
            visited = {x: False for x in adj_lst.keys()}
            res.append(dfsCalc(visited, a, b, 1))

        return res


# Bi-directional Weighted Graph + BFS
# - T/S: O(E), O(V+E), V=>Vertices, E=>Edges
class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_lst = {}
        for (a, b), v in zip(equations, values):
            adj_lst.setdefault(a, []).append((b, v))
            adj_lst.setdefault(b, []).append((a, 1 / v))

        res = []
        for src, tgt in queries:
            if src not in adj_lst or tgt not in adj_lst:
                res.append(-1.0)
                continue
            dq = deque([(src, 1.0)])
            visited = {x: False for x in adj_lst.keys()}
            visited[src] = True
            while dq:
                a, val = dq.popleft()
                if a == tgt:            # found
                    res.append(val) 
                    break
                for b, v in adj_lst[a]:
                    if not visited[b]:
                        dq.append((b, val * v))
                        visited[b] = True
            else:   # not found due to disconnected graph
                res.append(-1.0)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.calcEquation(
            [["a", "b"], ["b", "c"]], [2.0, 3.0], 
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        )
        print(r)
        assert r == [6.0, 0.5, -1.0, 1.0, -1.0]

        r = sol.calcEquation(
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        )
        print(r)
        assert r == [3.75000, 0.40000, 5.00000, 0.20000]

        r = sol.calcEquation([["a", "b"]], [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
        print(r)
        assert r == [0.50000, 2.00000, -1.00000, -1.00000]

    unit_test(Solution())
    unit_test(Solution1())
