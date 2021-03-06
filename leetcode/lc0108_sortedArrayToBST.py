# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. A height-balanced binary 
# tree is a binary tree in which the depth of the two subtrees of every node 
# never differs by more than one.
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import List, Optional


# Recursion
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def toBST(i, j):
            if i > j: return None
            k = (i+j) // 2
            root = TreeNode(val = nums[k])
            root.left = toBST(i, k-1)
            root.right = toBST(k+1, j)
            return root

        return toBST(0, len(nums)-1)


# test case
if __name__ == "__main__":
    def unit_test(sol):
        nums = [-10, -3, 0, 5, 9]
        expected1 = [0, -3, 9, -10, None, 5]
        expected2 = [0, -10, 5, None, -3, None, 9]
        r = TreeNodeUtil.toBfsList(sol.sortedArrayToBST(nums))
        print(r)
        assert r == expected1 or r == expected2 

        nums = [1, 3]
        expected1 = [3, 1]
        expected2 = [1, None, 3]
        r = TreeNodeUtil.toBfsList(sol.sortedArrayToBST(nums))
        print(r)
        assert r == expected1 or r == expected2

    unit_test(Solution())
    unit_test(Solution1())
