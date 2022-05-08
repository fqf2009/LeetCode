# Given the root of a binary tree, return the number of nodes where the
# value of the node is equal to the average of the values in its subtree.
# Note:
#  - The average of n elements is the sum of the n elements divided by n
#    and rounded down to the nearest integer.
#  - A subtree of root is a tree consisting of root and all of its descendants.
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
#   0 <= Node.val <= 1000
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def count(root: Optional[TreeNode]):
            nonlocal res
            if not root: return (0, 0)
            l_sum, l_cnt = count(root.left)
            r_sum, r_cnt = count(root.right)
            total = l_sum + r_sum + root.val
            cnt = l_cnt + r_cnt + 1
            if total // cnt == root.val:
                res += 1
            return (total, cnt)

        res = 0
        count(root)
        return res


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([4,8,5,0,1,None,6])
        r = sol.averageOfSubtree(root)
        print(r)
        assert r == 5

        root = TreeNodeUtil.fromBfsList([1])
        r = sol.averageOfSubtree(root)
        print(r)
        assert r == 1

    unit_test(Solution())
