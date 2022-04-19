# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return
# the root node of any one of them.
# Two trees are duplicate if they have the same structure with
# the same node values.
# Constraints:
#   The number of the nodes in the tree will be in the range [1, 10^4]
#   -200 <= Node.val <= 200
from collections import defaultdict
from turtle import update
from typing import Optional, List
from lib.TreeUtil import TreeNodeUtil, TreeNode
import hashlib


# Merkle Tree (Hash Tree)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_tree = defaultdict(list)

        def dfs_hash(node: Optional[TreeNode]) -> bytes:
            if not node:
                return hashlib.sha1().digest()
            h = hashlib.sha1()
            h.update(str(node.val).encode())
            h.update(dfs_hash(node.left))
            h.update(dfs_hash(node.right))
            dig = h.digest()
            hash_tree[dig].append(node)
            return dig

        dfs_hash(root)
        return [nodes[0] for nodes in hash_tree.values() if len(nodes) > 1]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]),
                ([2, 1, 1], [[1]]),
                ([2, 2, 2, 3, None, 3, None], [[2, 3], [3]]),
                ([2, 1, 1, 2], []),
            ]
        )
        def test_findDuplicateSubtrees(self, bfs_lst, expected):
            sol = self.solution()  # type:ignore
            root = TreeNodeUtil.fromBfsList(bfs_lst)
            dups = sol.findDuplicateSubtrees(root)
            r = [TreeNodeUtil.toBfsList(node) for node in dups]
            self.assertEqual(sorted(r), sorted(expected))

    main()
