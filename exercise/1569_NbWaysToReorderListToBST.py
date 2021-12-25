# 1569. Number of Ways to Reorder Array to Get Same BST (Hard)

# Given an array nums that represents a permutation of integers from 1 to n. We are going
# to construct a binary search tree (BST) by inserting the elements of nums in order into
# an initially empty BST. Find the number of different ways to reorder nums so that the
# constructed BST is identical to that formed from the original array nums. For example,
# given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right
# child. The array [2,3,1] also yields same BST but [3,2,1] yields a different BST.
# - Return the number of ways to reorder nums such that the BST formed is identical to the
#   original BST formed from nums.
# - Since the answer may be very large, return it modulo 109 + 7.

# Solution
# - The first item is always root node
# - Root item divide the list into left sub tree (L items) and right sub tree (R items).
# - For a specific LSB and RSB, i.e., assume L items in left list does not change order
#   so does R items in right list, however, the order of items between LSB and RSB does
#   not matter, because: LSB items' value < root < RSB items' value. So there are
#   C(L+R, L) combinations possible ways to interleave LSB and RSB items.
# - Recursively, assume LSB and RSB each has Ways(LSB) and Ways(RSB) to form BST.
# - So for entire BST:
#       Ways(BST) = C(L+R, L) * Ways(LSB) * Ways(RSB)

from typing import Optional, List, Tuple
from math import comb


class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# DFS + Recursion
class Solution:
    # Create a Binary Search Tree
    @staticmethod
    def fromListToBST(nums: List[int]) -> Optional[TreeNode]:
        def addToBST(root: TreeNode, n: int):
            if n < root.val:
                if root.left == None:
                    root.left = TreeNode(n)
                else:
                    addToBST(root.left, n)
            else:
                if root.right == None:
                    root.right = TreeNode(n)
                else:
                    addToBST(root.right, n)

        if len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            addToBST(root, nums[i])
        return root

    def numOfWays(self, nums: List[int]) -> int:
        def dfsWays(node: TreeNode) -> Tuple[int, int]:
            leftWays, leftItems = 1, 0
            rightWays, rightItems = 1, 0
            if node.left != None:
                leftWays, leftItems = dfsWays(node.left)
            if node.right != None:
                rightWays, rightItems = dfsWays(node.right)

            # note: comb(0, 0) == 1, so no special treatment
            return (comb(leftItems+rightItems, leftItems) * leftWays * rightWays,
                    leftItems + rightItems + 1)

        root = Solution.fromListToBST(nums)
        assert(root != None)
        res = dfsWays(root)[0]
        return (res - 1) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()

    # Note: the number of ways other than the original one
    r = sol.numOfWays([2, 1, 3])
    print(r)
    assert(r == 1)

    r = sol.numOfWays([3, 4, 5, 1, 2])
    print(r)
    assert(r == 5)

    r = sol.numOfWays([1, 2, 3])
    print(r)
    assert(r == 0)

    r = sol.numOfWays([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18])
    print(r)
    assert(r == 216212978)
