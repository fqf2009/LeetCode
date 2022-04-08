# You are given a 2D integer array descriptions where 
# descriptions[i] = [parenti, childi, isLefti] indicates that parenti
# is the parent of childi in a binary tree of unique values. Furthermore,
#  - If isLefti == 1, then childi is the left child of parenti.
#  - If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
# The test cases will be generated such that the binary tree is valid.

# Constraints:
#   1 <= descriptions.length <= 10^4
#   descriptions[i].length == 3
#   1 <= parenti, childi <= 10^5
#   0 <= isLefti <= 1
#   The binary tree described by descriptions is valid.
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil
from collections import defaultdict


# Binary Tree
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        childNodes = set()
        for v1, v2, left in descriptions:
            childNodes.add(v2)
            n1, n2 = nodes[v1], nodes[v2]
            n1.val, n2.val = v1, v2
            if left == 1:
                n1.left = n2
            else:
                n1.right = n2

        root = next(n for v, n in nodes.items() if v not in childNodes)
        return root


if __name__ == '__main__':
    def unitTest(sol):
        root = sol.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [50, 20, 80, 15, 17, 19]

        root = sol.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [1, 2, None, None, 3, 4]

    unitTest(Solution())
