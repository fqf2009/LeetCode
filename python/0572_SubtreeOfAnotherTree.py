# Given the roots of two binary trees root and subRoot, return true if there is a
# subtree of root with same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of
# this node's descendants. The tree tree could also be considered as a subtree of itself.
# Constraints:
#   The number of nodes in the root tree is in the range [1, 2000].
#   The number of nodes in the subRoot tree is in the range [1, 1000].
#   -10^4 <= root.val <= 10^4
#   -10^4 <= subRoot.val <= 10^4
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS + Recursion
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def matchTree(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            return ( r1.val == r2.val and 
                          matchTree(r1.left, r2.left) and 
                          matchTree(r1.right, r2.right) )

        if not root or not subRoot: return subRoot is None

        return (matchTree(root, subRoot)
                or self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([3, 4, 5, 1, 2])
    subRoot = TreeNodeUtil.fromBfsList([4, 1, 2])
    r = sol.isSubtree(root, subRoot)
    print(r)
    assert(r == True)

    root = TreeNodeUtil.fromBfsList([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = TreeNodeUtil.fromBfsList([4, 1, 2])
    r = sol.isSubtree(root, subRoot)
    print(r)
    assert(r == False)

    root = TreeNodeUtil.fromBfsList([-1, -4, 8, -6, -2, 3, 9, None, -5, None, None, 0, 7])
    subRoot = TreeNodeUtil.fromBfsList([3, 0, 5848])
    r = sol.isSubtree(root, subRoot)
    print(r)
    assert(r == False)
