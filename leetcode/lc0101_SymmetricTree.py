from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given the root of a binary tree, check whether it is a mirror of
# itself (i.e., symmetric around its center).

# Recursion
class Solution:
    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None or root2 == None:
            return type(root1) == type(root2)  # type: ignore

        return ( root1.val == root2.val and 
                 self.isMirror(root1.left, root2.right) and 
                 self.isMirror(root1.right, root2.left) )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)


# The following is wrong
class Solution1:
    def toInorderList(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = self.toInorderList(root.left)
        res.append(root.val)
        res.extend(self.toInorderList(root.right))
        return res

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lst = self.toInorderList(root)
        for i in range(len(lst) // 2):
            if lst[i] != lst[len(lst) - 1 - i]:
                return False
        return True


# test case
if __name__ == "__main__":
    root = TreeNodeUtil.fromBfsList([1, 2, 2, 2, None, 2])
    # print(Solution().toInorderList(root)) # [2, 2, 1, 2, 2]
    r = Solution().isSymmetric(root)
    print(r)
    assert(not r)

    root = TreeNodeUtil.fromBfsList([1, 2, 2, 3, 4, 4, 3])
    r = Solution().isSymmetric(root)
    print(r)
    assert(r)

    root = TreeNodeUtil.fromBfsList([1, 2, 2, None, 3, None, 3])
    r = Solution().isSymmetric(root)
    print(r)
    assert(not r)
