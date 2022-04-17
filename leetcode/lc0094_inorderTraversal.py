from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# DFS + Recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        res = []
        dfs(root)
        return res


# Recursion
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res


if __name__ == "__main__":
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([1, None, 2, 3])
        r = sol.inorderTraversal(root)
        print(r)
        assert(r == [1, 3, 2])

        root = TreeNodeUtil.fromBfsList([])
        r = sol.inorderTraversal(root)
        print(r)
        assert(r == [])

        root = TreeNodeUtil.fromBfsList([1])
        r = sol.inorderTraversal(root)
        print(r)
        assert(r == [1])

        root = TreeNodeUtil.fromBfsList([1, 2])
        r = sol.inorderTraversal(root)
        print(r)
        assert(r == [2, 1])

        root = TreeNodeUtil.fromBfsList([1, None, 2])
        r = sol.inorderTraversal(root)
        print(r)
        assert(r == [1, 2])

    unit_test(Solution())
    unit_test(Solution1())
