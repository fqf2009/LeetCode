# Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely 
# filled, and all nodes in the last level are as far left as possible. It can have 
# between 1 and 2h nodes inclusive at the last level h.
# Constraints:
#   The number of nodes in the tree is in the range [1, 100].
#   1 <= Node.val <= 1000
from collections import deque
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# BFS - T/S: O(n), O(n)
# - Intuition: when traversing a complete binary tree using BFS, you will never 
#   encounter a null node between non-null nodes.
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        dq = deque([root])
        found_null = False
        while dq:
            node = dq.popleft()
            for child in [node.left, node.right]:
                if child:
                    if found_null: return False
                    dq.append(child)
                else:
                    found_null = True
        return True


# BFS - T/S: O(n), O(n)
# - set index of root to 0, then for any node with index i,
#   its child nodes will have index of (2*i+1, 2*i+2)
# - check there is no gap in all nodes' index.
class Solution1:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        dq = deque()
        dq.append([root, 0])
        prev_idx = -1
        while dq:
            node, idx = dq.popleft()
            if idx != prev_idx + 1:
                return False
            prev_idx = idx

            if node.left:
                dq.append([node.left, idx*2+1]) 

            if node.right:
                dq.append([node.right, idx*2+2])

        return True


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,2,3,4,5,6], True),
            ([1,2,3,4,5,None,7], False),
        ])
        def test_isCompleteTree(self, lst, expected):
            sol = self.solution()       # type:ignore
            root = TreeNodeUtil.fromBfsList(lst)
            r = sol.isCompleteTree(root)
            self.assertEqual(r, expected)

    main()
