from collections import deque
from typing import Optional

# Some utility functions to facilitate the code testing of the algorithm using trees

class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class TreeNodeUtil:
    # Depth First Search (Traversal)
    @staticmethod
    def toInorderList(root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = TreeNodeUtil.toInorderList(root.left)
        res.append(root.val)
        res.extend(TreeNodeUtil.toInorderList(root.right))
        return res

    @staticmethod
    def toPreorderList(root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []
        res = [root.val]
        res.extend(TreeNodeUtil.toPreorderList(root.left))
        res.extend(TreeNodeUtil.toPreorderList(root.right))
        return res

    @staticmethod
    def toPostorderList(root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []
        res = TreeNodeUtil.toPostorderList(root.left)
        res.extend(TreeNodeUtil.toPostorderList(root.right))
        res.append(root.val)
        return res

    # Breadth First Search (Traversal)
    @staticmethod
    def toBfsList(root: Optional[TreeNode]) -> list[Optional[int]]:
        res = []
        if root == None:
            return res

        dq = deque()
        dq.append(root)
        res.append(root.val)
        while len(dq) > 0:
            node = dq.popleft()
            if node.left == None:
                res.append(None)
            else:
                dq.append(node.left)
                res.append(node.left.val)

            if node.right == None:
                res.append(None)
            else:
                dq.append(node.right)
                res.append(node.right.val)

        # remove trailing None
        for i in reversed(range(len(res))):
            if res[i] != None:
                break
            res.pop()

        return res

    @staticmethod
    def fromBfsList(nums: list[Optional[int]]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root = TreeNode(nums[0])
        dq = deque()
        dq.append(root)
        isLeft = True
        for n in nums[1:]:
            node = dq[0]
            if isLeft:
                if n != None:
                    node.left = TreeNode(n)
                    dq.append(node.left)
                isLeft = False
            else:
                if n != None:
                    node.right = TreeNode(n)
                    dq.append(node.right)
                isLeft = True
                dq.popleft()

        return root

    # Create a Binary Search Tree
    @staticmethod
    def fromListToBST(nums: list[int]) -> Optional[TreeNode]:
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


if __name__ == "__main__":
    # test case
    root = TreeNodeUtil.fromBfsList([1, None, 2, 3])
    r = TreeNodeUtil.toInorderList(root)
    print(r)
    assert(r == [1, 3, 2])

    root = TreeNodeUtil.fromBfsList([])
    r = TreeNodeUtil.toInorderList(root)
    print(r)
    assert(r == [])

    root = TreeNodeUtil.fromBfsList([1])
    r = TreeNodeUtil.toInorderList(root)
    print(r)
    assert(r == [1])

    root = TreeNodeUtil.fromBfsList([1, 2])
    r = TreeNodeUtil.toInorderList(root)
    print(r)
    assert(r == [2, 1])

    root = TreeNodeUtil.fromBfsList([1, None, 2])
    r = TreeNodeUtil.toInorderList(root)
    print(r)
    assert(r == [1, 2])

    # test case
    n1 = TreeNode(2)
    n2 = TreeNode(5)
    n3 = TreeNode(8)
    n4 = TreeNode(6)
    n5 = TreeNode(7)
    n1.right = n2
    n2.left = n3
    n2.right = n4
    n4.left = n5

    nums = TreeNodeUtil.toBfsList(n1)
    print(nums)
    assert(nums == [2, None, 5, 8, 6, None, None, 7])

    root = TreeNodeUtil.fromBfsList(nums)
    nums = TreeNodeUtil.toBfsList(root)
    print(nums)
    assert(nums == [2, None, 5, 8, 6, None, None, 7])
