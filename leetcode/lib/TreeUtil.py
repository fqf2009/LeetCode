# Some utility functions to facilitate the code testing of the
# algorithm using trees
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=-1, left=None, right=None, parent=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
        self.parent: Optional[TreeNode] = parent


class TreeNodeUtil:
    # Depth First Search (Traversal)
    @staticmethod
    def toInorderList(root: Optional[TreeNode]) -> list:
        if root is None:
            return []
        res = TreeNodeUtil.toInorderList(root.left)
        res.append(root.val)
        res.extend(TreeNodeUtil.toInorderList(root.right))
        return res

    @staticmethod
    def toPreorderList(root: Optional[TreeNode]) -> list:
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

    @staticmethod
    def toInorderListIterative(root: Optional[TreeNode]) -> list:
        stack, res = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)  # type: ignore
            root = root.right  # type: ignore
        return res

    @staticmethod
    def toPreorderListIterative(root: Optional[TreeNode]) -> list:
        stack, res = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right  # type: ignore
        return res

    # 1. Push root to first stack.
    # 2. Loop while first stack is not empty
    #    2.1 Pop a node from first stack and push it to second stack
    #    2.2 Push left and right children of the popped node to first stack
    # 3. Print contents of second stack
    @staticmethod
    def toPostorderListIterative(root: Optional[TreeNode]) -> list:
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        return res[::-1]

    @staticmethod
    def dfsFind(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        node = TreeNodeUtil.dfsFind(root.left, val)
        return node if node else TreeNodeUtil.dfsFind(root.right, val)

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
        for v in nums[1:]:
            node = dq[0]
            if isLeft:
                if v != None:
                    node.left = TreeNode(val=v, parent=node)
                    dq.append(node.left)
                isLeft = False
            else:
                if v != None:
                    node.right = TreeNode(val=v, parent=node)
                    dq.append(node.right)
                isLeft = True
                dq.popleft()

        return root

    # Create a Binary Search Tree
    @staticmethod
    def fromListToBST(nums: list[int]) -> Optional[TreeNode]:
        def addToBST(root: TreeNode, v: int):
            if v < root.val:
                if root.left == None:
                    root.left = TreeNode(val=v, parent=root)
                else:
                    addToBST(root.left, v)
            else:
                if root.right == None:
                    root.right = TreeNode(val=v, parent=root)
                else:
                    addToBST(root.right, v)

        if len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            addToBST(root, nums[i])
        return root


if __name__ == "__main__":

    def test_toBfsList():
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
        assert nums == [2, None, 5, 8, 6, None, None, 7]

        root = TreeNodeUtil.fromBfsList(nums)
        nums = TreeNodeUtil.toBfsList(root)
        print(nums)
        assert nums == [2, None, 5, 8, 6, None, None, 7]

    def test_toXorderList(bfsList, inorderExpected, preorderExpected, postorderExpected):
        root = TreeNodeUtil.fromBfsList(bfsList)

        r1 = TreeNodeUtil.toInorderList(root)
        r2 = TreeNodeUtil.toInorderListIterative(root)
        print(r1)
        assert r1 == inorderExpected
        assert r2 == inorderExpected

        r1 = TreeNodeUtil.toPreorderList(root)
        r2 = TreeNodeUtil.toPreorderListIterative(root)
        print(r1)
        assert r1 == preorderExpected
        assert r2 == preorderExpected

        r1 = TreeNodeUtil.toPostorderList(root)
        r2 = TreeNodeUtil.toPostorderListIterative(root)
        print(r1)
        assert r1 == postorderExpected
        assert r2 == postorderExpected

    test_toBfsList()
    test_toXorderList([1, None, 2, 3], [1, 3, 2], [1, 2, 3], [3, 2, 1])
    test_toXorderList([], [], [], [])
    test_toXorderList([1], [1], [1], [1])
    test_toXorderList([1, 2], [2, 1], [1, 2], [2, 1])
