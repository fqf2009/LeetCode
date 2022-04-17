# You are given a tree (i.e. a connected, undirected graph that has no cycles) 
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is 
# represented by a 0-indexed array parent of size n, where parent[i] is the 
# parent of node i. Since node 0 is the root, parent[0] == -1.
# You are also given a string s of length n, where s[i] is the character 
# assigned to node i.
# Return the length of the longest path in the tree such that no pair of adjacent 
# nodes on the path have the same character assigned to them.
# Constraints:
#   n == parent.length == s.length
#   1 <= n <= 10^5
#   0 <= parent[i] <= n - 1 for all i >= 1
#   parent[0] == -1
#   parent represents a valid tree.
#   s consists of only lowercase English letters.
from collections import deque
from typing import List


# Graph + BFS - T/S: O(n), O(n)
# - no need to build graph, the parent list is graph;
# - compute indegree for all nodes;
# - BFS starting from leaf node, reduce indegree for its parent node
#   add parent node to deque if its indegree is reduced to zero;
# - distinguish extendable_path_len, un_extendable_path_len:
#   if a node has different value with its child, then this path
#   length can still be exended to its parent.
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        indegree = [0] * n
        for p in parent:
            if p != -1:
                indegree[p] += 1

        res = 0
        max_path = [[0, 0] for _ in range(n)]  # [extendable_len, un_extendable_len]
        dq = deque([i for i, v in enumerate(indegree) if v == 0])
        while dq:
            i = dq.popleft()
            p = parent[i]
            if p == -1:
                break

            child_ext, child_unext = max_path[i]
            parent_ext, parent_unext = max_path[p]  # previous value
            if s[i] != s[p]:
                max_path[p][0] = max(parent_ext, child_ext + 1)
                max_path[p][1] = max(parent_unext, child_unext, parent_ext + child_ext + 1)
            else:
                max_path[p][1] = max(parent_unext, child_unext)

            res = max(res, max(max_path[p]))
            indegree[p] -= 1
            if indegree[p] == 0:
                dq.append(p)

        return res + 1


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe")
        print(r)
        assert r == 3

        r = sol.longestPath(parent=[-1, 0, 0, 0], s="aabc")
        print(r)
        assert r == 3

    unit_test(Solution())
