# Given the root of a binary search tree and a target value, return the 
# value in the BST that is closest to the target.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   0 <= Node.val <= 10^9
#   -10^9 <= target <= 10^9
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Iterative
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        assert root
        cloest = root.val
        while root:
            if abs(root.val - target) < abs(cloest - target):
                cloest = root.val
            root = root.left if target < root.val else root.right

        return cloest


# Binary Search Tree: O(log(n)), or O(H) for imbalanced tree, H is Height
class Solution1:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs_cloest(root: TreeNode) -> int:
            if root.left and target < root.val:
                cloest = dfs_cloest(root.left)
            elif root.right and target > root.val:
                cloest = dfs_cloest(root.right)
            else:
                return root.val

            if abs(root.val - target) <= abs(cloest - target):
                return root.val
            else:
                return cloest

        if not root: return -1
        return dfs_cloest(root)


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([4,2,5,1,3])
        target = 3.714286
        r = sol.closestValue(root, target)
        print(r)
        assert r == 4

        root = TreeNodeUtil.fromBfsList([1])
        target = 4.428571
        r = sol.closestValue(root, target)
        print(r)
        assert r == 1

    unit_test(Solution())
    unit_test(Solution1())
