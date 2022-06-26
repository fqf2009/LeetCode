# There is an undirected connected tree with n nodes labeled 
# from 0 to n - 1 and n - 1 edges.
# You are given a 0-indexed integer array nums of length n where 
# nums[i] represents the value of the ith node. You are also given 
# a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
# indicates that there is an edge between nodes ai and bi in the tree.
# Remove two distinct edges of the tree to form three connected components. 
# For a pair of removed edges, the following steps are defined:
# Get the XOR of all the values of the nodes for each of the three 
# components respectively.
# The difference between the largest XOR value and the smallest XOR value
# is the score of the pair.
# For example, say the three components have the node values: [4,5,7], 
# [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, 
# and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR
# value is 3. The score is then 8 - 3 = 5.
# Return the minimum score of any possible pair of edge removals on 
# the given tree.
# Constraints:
#   n == nums.length
#   3 <= n <= 1000
#   1 <= nums[i] <= 108
#   edges.length == n - 1
#   edges[i].length == 2
#   0 <= ai, bi < n
#   ai != bi
#   edges represents a valid tree.
from collections import defaultdict
from typing import List


# T/S: O(n^2), O(n)
# Analysis:
# - use a timer to record the time of each tree node visit (in, out),
#   to easily determine if two nodes has ancestor/descendant relationship
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)  # undirected graph
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        timer, n = 0, len(nums)
        time_in, time_out = [0] * n, [0] * n
        tree = defaultdict(list)  # directed graph
        tree_xor = nums.copy()  # initial xor is node value

        def dfs_create_tree(v1, visited=set()) -> int:  # return xor
            nonlocal timer
            timer += 1
            time_in[v1] = timer
            visited.add(v1)
            for v2 in graph[v1]:
                if v2 not in visited:
                    tree[v1].append(v2)
                    tree_xor[v1] ^= dfs_create_tree(v2, visited)
            timer += 1
            time_out[v1] = timer
            return tree_xor[v1]

        def is_ancestor(ancestor, decendant):
            return time_in[ancestor] < time_in[decendant] < time_out[ancestor]

        res = 10**9

        def calc_score(xor1, xor2, xor3):
            nonlocal res
            res = min(res, max(xor1, xor2, xor3) - min(xor1, xor2, xor3))

        dfs_create_tree(0)  # pick 0 as root
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if is_ancestor(i, j):
                    calc_score(tree_xor[0] ^ tree_xor[i], tree_xor[i] ^ tree_xor[j], tree_xor[j])
                elif is_ancestor(j, i):
                    calc_score(tree_xor[0] ^ tree_xor[j], tree_xor[i] ^ tree_xor[j], tree_xor[i])
                else:
                    calc_score(tree_xor[0] ^ tree_xor[i] ^ tree_xor[j], tree_xor[i], tree_xor[j])
        return res


# Algorithm - T/S: O(n^2), O(n)
# - Note that: (A^B)^B == A, i.e., (A^B^C)^B == (A^C), where ^ is xor
# - Build an undirected graph
# - DFS traverse the graph to build a tree (directed graph),
#   and calculate xor for each node (i.e., xor of each sub-tree)
# - Remove two edges and calculate minimum score of 3 components
# - First edge to remove: DFS traverse (iterative) the tree, when
#   visiting each non-root node (N1), cut the edge connecting to it
#   - at the same time, collect all visited nodes by far:
#       first_DFS_visited_nodes
# - Second edge to remove, two scenarios:
#   a. inside the sub-tree N1, to cut the edge connecting to N2,
#       - require another DFS traversal (recursive) starting from N1
#       - at time same time, collect all sub-tree nodes of N1
#       - the xor of 3 components:
#           - tree_xor[root] ^ tree_xor[N1]
#           - tree_xor[N1] ^ tree_xor[N2]
#           - tree_xor[N2]
#   b. to cut the edge connecting to N3:
#      - N3 is outside of the sub-tree N1
#      - N3 is not in first_DFS_visited_nodes, so N3 is
#        not the parent of N1
#      - the xor of 3 components:
#           - tree_xor[root] ^ tree_xor[N1] ^ tree_xor[N2]
#           - tree_xor[N1]
#           - tree_xor[N2]
class Solution1:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # xor_sum = reduce(lambda a, b: a^b, nums)  # not used
        graph = defaultdict(list)  # undirected graph
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        tree = defaultdict(list)  # directed graph
        tree_xor = nums.copy()  # initial xor is node value

        def dfs_create_tree(v1, visited=set()) -> int:  # return xor
            visited.add(v1)
            for v2 in graph[v1]:
                if v2 not in visited:
                    tree[v1].append(v2)
                    tree_xor[v1] ^= dfs_create_tree(v2, visited)
            return tree_xor[v1]

        dfs_create_tree(0)  # pick any node as root

        res = 10**9

        def calc_score(xor1, xor2, xor3):
            nonlocal res
            res = min(res, max(xor1, xor2, xor3) - min(xor1, xor2, xor3))

        def dfs_visit_tree(v1, visited1=set()):
            def dfs_visit_subtree(n1):
                visited2.add(n1)
                for n2 in tree[n1]:
                    xor1 = tree_xor[0] ^ tree_xor[v2]
                    xor2 = tree_xor[v2] ^ tree_xor[n2]
                    xor3 = tree_xor[n2]
                    calc_score(xor1, xor2, xor3)
                    dfs_visit_subtree(n2)

            visited1.add(v1)
            for v2 in tree[v1]:
                visited2 = set()
                dfs_visit_subtree(v2)
                for v3 in range(len(nums)):
                    if v3 not in visited1 and v3 not in visited2:
                        xor1 = tree_xor[0] ^ tree_xor[v2] ^ tree_xor[v3]
                        xor2 = tree_xor[v2]
                        xor3 = tree_xor[v3]
                        calc_score(xor1, xor2, xor3)
                dfs_visit_tree(v2, visited1)

        dfs_visit_tree(0)
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minimumScore([1, 5, 5, 4, 11], edges=[[0, 1], [1, 2], [1, 3], [3, 4]])
        print(r)
        assert r == 9

        r = sol.minimumScore([5, 5, 2, 4, 4, 2], edges=[[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]])
        print(r)
        assert r == 0

    unit_test(Solution())
    unit_test(Solution1())
