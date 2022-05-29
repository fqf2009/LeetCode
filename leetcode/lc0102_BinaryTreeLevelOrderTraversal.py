# Given the root of a binary tree, return the level order traversal of its
# nodes values. (i.e., from left to right, level by level).
# Constraints:
#   The number of nodes in the tree is in the range [0, 2000].
#   -1000 <= Node.val <= 1000
from collections import deque
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        res = []
        while dq:
            values = []
            n = len(dq)
            for _ in range(n):
                node = dq.popleft()
                values.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(values)

        return res


if __name__ == "__main__":
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
        r = sol.levelOrder(root)
        print(r)
        assert r == [[3], [9, 20], [15, 7]]

        root = TreeNodeUtil.fromBfsList([1])
        r = sol.levelOrder(root)
        print(r)
        assert r == [[1]]

        root = TreeNodeUtil.fromBfsList([])
        r = sol.levelOrder(root)
        print(r)
        assert r == []

    unit_test(Solution())
