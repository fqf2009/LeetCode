from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given the root of a binary tree and an integer targetSum, return true if 
# the tree has a root-to-leaf path such that adding up all the values along 
# the path equals targetSum. A leaf is a node with no children.

# Recursion
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return root.val == targetSum
        
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))


if __name__ == "__main__":
    root = TreeNodeUtil.fromBfsList([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    r = Solution().hasPathSum(root, targetSum)
    print(r)
    assert(r == True)

    root = TreeNodeUtil.fromBfsList([1,2,3])
    targetSum = 5
    r = Solution().hasPathSum(root, targetSum)
    print(r)
    assert(r == False)

    root = TreeNodeUtil.fromBfsList([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 0
    r = Solution().hasPathSum(root, targetSum)
    print(r)
    assert(r == False)
