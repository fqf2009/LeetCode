# You are given an integer n denoting the number of nodes of a weighted directed graph.
# The nodes are numbered from 0 to n - 1.
#
# You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti]
# denotes that there exists a directed edge from fromi to toi with weight weighti.
#
# Lastly, you are given three distinct integers src1, src2, and dest denoting three
# distinct nodes of the graph.
#
# Return the minimum weight of a subgraph of the graph such that it is possible to
# reach dest from both src1 and src2 via a set of edges of this subgraph. In case
# such a subgraph does not exist, return -1.
#
# A subgraph is a graph whose vertices and edges are subsets of the original graph.
# The weight of a subgraph is the sum of weights of its constituent edges.
#
# Constraints:
#   3 <= n <= 10^5
#   0 <= edges.length <= 10^5
#   edges[i].length == 3
#   0 <= fromi, toi, src1, src2, dest <= n - 1
#   fromi != toi
#   src1, src2, and dest are pairwise distinct.
#   1 <= weight[i] <= 10^5

from typing import List


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minimumWeight(6, [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3],
                                  [2, 3, 4], [3, 4, 2], [4, 5, 1]], src1=0, src2=1, dest=5)
        print(r)
        assert r == 9

        r = sol.integerBreak(3, [[0, 1, 1], [2, 1, 1]], src1=0, src2=1, dest=2)
        print(r)
        assert r == -1

    unitTest(Solution())
