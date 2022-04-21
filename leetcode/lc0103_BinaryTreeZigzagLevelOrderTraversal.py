# Given the root of a binary tree, return the zigzag level order 
# traversal of its nodes' values. (i.e., from left to right, then 
# right to left for the next level and alternate between).
# Constraints:
#   The number of nodes in the tree is in the range [0, 2000].
#   -100 <= Node.val <= 100
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        def dfs_collect(node, depth):
            if not node: return

            if depth >= len(res):
                res.append([])
            res[depth].append(node.val)

            dfs_collect(node.left, depth+1)
            dfs_collect(node.right, depth+1)

        dfs_collect(root, 0)
        return [x if i%2 == 0 else x[::-1] for i, x in enumerate(res)]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]),
            ([1], [[1]]),
            ([], []),
        ])
        def test_zigzagLevelOrder(self, lst, expected):
            sol = self.solution()       # type:ignore
            root = TreeNodeUtil.fromBfsList(lst)
            r = sol.zigzagLevelOrder(root)
            self.assertEqual(r, expected)

    main()
