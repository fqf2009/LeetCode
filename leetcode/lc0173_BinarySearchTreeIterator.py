# Implement the BSTIterator class that represents an iterator over the
# in-order traversal of a binary search tree (BST):
#  - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
#    The root of the BST is given as part of the constructor. The pointer should 
#    be initialized to a non-existent number smaller than any element in the BST.
#  - boolean hasNext() Returns True if there exists a number in the traversal to
#    the right of the pointer, otherwise returns false.
#  - int next() Moves the pointer to the right, then returns the number at the 
#    pointer.
# Notice that by initializing the pointer to a non-existent smallest number, 
# the first call to next() will return the smallest element in the BST.
# You may assume that next() calls will always be valid. That is, there will 
# be at least a next number in the in-order traversal when next() is called.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^5].
#   0 <= Node.val <= 10^6
#   At most 10^5 calls will be made to hasNext, and next.
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS + Iterative
# - to simplify the code
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration

        while self.node:                
            self.stack.append(self.node)    # push node into stack
            self.node = self.node.left      # hold left branch, until None

        self.node = self.stack.pop()    # pop up
        value = self.node.val           # visit node
        self.node = self.node.right     # discard and then hold right branch
        return value

    def hasNext(self) -> bool:
        return bool(self.node or self.stack)


# DFS + Iterative
class BSTIterator1:
    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration

        if not self.node:
            self.node = self.stack.pop()
            value = self.node.val
            self.node = self.node.right
            return value

        while self.node.left:
            self.stack.append(self.node)
            self.node = self.node.left

        value = self.node.val
        self.node = self.node.right
        return value

    def hasNext(self) -> bool:
        return bool(self.node or self.stack)


if __name__ == '__main__':
    def unitTest(Solution):
        inputs = [ ["next", "next", "hasNext", "next",
                    "hasNext", "next", "hasNext", "next", "hasNext"],
                   [[], [], [], [], [], [], [], [], []] ]
        expected = [None, 3, 7, True, 9, True, 15, True, 20, False]
        outputs = [None]
        root = TreeNodeUtil.fromBfsList([7, 3, 15, None, None, 9, 20])
        obj = Solution(root)                                # obj = BSTIterator(root)
        for i in range(len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.hasNext() or obj.next()
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest(BSTIterator)
    unitTest(BSTIterator1)
