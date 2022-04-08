# Given the root of a binary tree, return an array of the largest value in 
# each row of the tree (0-indexed).
# Constraints:
#   The number of nodes in the tree will be in the range [0, 10^4].
#   -2^31 <= Node.val <= 2^31 - 1
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs_visit(root: Optional[TreeNode], level: int):
            if not root: return

            if level < len(res):
                res[level] = max(res[level], root.val)
            else:
                res.append(root.val)
            
            dfs_visit(root.left, level + 1)
            dfs_visit(root.right, level + 1)

        dfs_visit(root, 0)
        return res


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([1,3,2,5,3,None,9])
        r = sol.largestValues(root)
        print(r)
        assert r == [1,3,9]

        root = TreeNodeUtil.fromBfsList([1,2,3])
        r = sol.largestValues(root)
        print(r)
        assert r == [1,3]

    unit_test(Solution())
