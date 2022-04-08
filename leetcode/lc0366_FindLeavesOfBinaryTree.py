# Given the root of a binary tree, collect a tree's nodes as if
# you were doing this:
#   Collect all the leaf nodes.
#   Remove all the leaf nodes.
#   Repeat until the tree is empty.
# Constraints:
#   The number of nodes in the tree is in the range [1, 100].
#   -100 <= Node.val <= 100
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import List, Optional


# - Q: Do I really remove leaf nodes?
# - If true, DFS multiple times, O(n*log(n)), worst O(n^2) for skewed tree
# - If false, using DFS to collect all node into list or queue, tag how far
#   away from the leaf for each item, then sort by distance to leaf.
#   Time: O(n*log(n)), DFS is O(n), sort is O(n*log(n)), Space: O(n)
# - "as if" means false.
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfsCollect(root: Optional[TreeNode]) -> int:
            if not root: return 0
            distance = max(dfsCollect(root.left), dfsCollect(root.right)) + 1
            leaves.setdefault(distance, list()).append(root.val)
            return distance

        leaves = {}
        dfsCollect(root)
        return [nodes for _, nodes in sorted(leaves.items())]


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([1, 2, 3, 4, 5])
        r = sol.findLeaves(root)
        print(r)
        assert r == [[4, 5, 3], [2], [1]]

        root = TreeNodeUtil.fromBfsList([1])
        r = sol.findLeaves(root)
        print(r)
        assert r == [[1]]

    unitTest(Solution())
