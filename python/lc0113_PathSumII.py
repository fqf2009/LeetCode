from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import List, Optional

# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf  paths where the sum of node values in the path equals
# targetSum. Each path should be returned as a list of the node values,
# not node references. A root-to-leaf path is a path starting from the
# root and ending at any leaf node. A leaf is a node with no children.

# DFS + Recursion
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfsPathSum(root: Optional[TreeNode], targetSum: int):
            if not root:
                return
            path.append(root.val)
            if root.val == targetSum and root.left == None and root.right == None:
                paths.append(path.copy())   # copy()!!!
            dfsPathSum(root.left, targetSum - root.val)
            dfsPathSum(root.right, targetSum - root.val)
            path.pop()

        paths = []
        path = []
        dfsPathSum(root, targetSum)
        return paths


if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    r = sol.pathSum(root, 22)
    print(r)
    assert(r == [[5, 4, 11, 2], [5, 8, 4, 5]])

    root = TreeNodeUtil.fromBfsList([1, 2, 3])
    r = sol.pathSum(root, 5)
    print(r)
    assert(r == [])

    root = TreeNodeUtil.fromBfsList([1, 2])
    r = sol.pathSum(root, 0)
    print(r)
    assert(r == [])
