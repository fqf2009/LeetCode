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
from collections import defaultdict, deque
import heapq
from typing import List


# Graph + DFS - T/S: O(n), O(n)
# - build a (top-down, or root-to-leaf) directed graph (tree);
# - DFS visit starting from root node;
# - only the extendable length is returned from the recursive 
#   DFS visit of child nodes;
# - for all the child nodes with different value from parent node,
#   the longest two (or one) of the returned length can be added up 
#   and plus parent node to form new length (path);
# - because each node will update the global max_length, so no need
#   to return un-extendable length to parent node.
# - the code below use node count as path length
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i, p in enumerate(parent):
            tree[p].append(i)

        max_len = 1
        def dfs_len(node: int) -> int: # extendable_length
            lengths = []
            for child in tree[node]:
                child_len = dfs_len(child)
                if s[child] != s[node]:
                    lengths.append(child_len)
            
            largest2 = heapq.nlargest(2, lengths)
            nonlocal max_len
            max_len = max(max_len, sum(largest2) + 1)
            return 1 if not largest2 else 1 + largest2[0]
        
        dfs_len(0)
        return max_len


# Graph + BFS - T/S: O(n), O(n)
# Optimize and simplify the code:
# - keep max_len on the go; 
# - only save extendable length in each node, just like DFS solution
class Solution1:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        indegree = [0] * n
        for p in parent:
            if p != -1:
                indegree[p] += 1

        max_len = 0
        path_len = [0] * n      # extendable_length for each node
        dq = deque([i for i, v in enumerate(indegree) if v == 0])
        while dq:
            i = dq.popleft()
            p = parent[i]

            if s[i] != s[p]:
                max_len = max(max_len, path_len[p] + path_len[i] + 1)
                path_len[p] = max(path_len[p], path_len[i] + 1)

            indegree[p] -= 1
            if indegree[p] == 0 and p != 0: # do not add root node
                dq.append(p)

        return max_len + 1


# Graph + BFS - T/S: O(n), O(n)
# - no need to build graph, the parent list is graph;
# - compute indegree for all nodes;
# - BFS starting from leaf node, reduce indegree for its parent node
#   add parent node to deque if its indegree is reduced to zero;
# - distinguish extendable_path_len, un_extendable_path_len:
#   if a node has different value with its child, then this path
#   length can still be exended to its parent.
class Solution2:
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
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([-1, 0, 0, 1, 1, 2], "abacbe", 3),
            ([-1, 0, 0, 0], "aabc", 3),
        ])
        def test_longestPath(self, parent, s, expected):
            sol = self.solution()       # type:ignore
            r = sol.longestPath(parent, s)
            self.assertEqual(r, expected)

    main()
