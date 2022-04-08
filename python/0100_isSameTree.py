from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not. Two binary trees are considered the same if they 
# are structurally identical, and the nodes have the same value. 

# Recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return type(p) == type(q)

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# test case
if __name__ == "__main__":
    root1 = TreeNodeUtil.fromBfsList([1,2,3])
    root2 = TreeNodeUtil.fromBfsList([1,2,3])
    r = Solution().isSameTree(root1, root2)
    print(r)
    assert(r)

    root1 = TreeNodeUtil.fromBfsList([1,2])
    root2 = TreeNodeUtil.fromBfsList([1,None, 2])
    r = Solution().isSameTree(root1, root2)
    print(r)
    assert(not r)

    root1 = TreeNodeUtil.fromBfsList([1,2,1])
    root2 = TreeNodeUtil.fromBfsList([1,1,2])
    r = Solution().isSameTree(root1, root2)
    print(r)
    assert(not r)
