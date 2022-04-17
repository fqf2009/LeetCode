# Given the root of a binary tree, return the vertical order traversal
# of its nodes' values. (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be
# from left to right.
# Constraints:
#   The number of nodes in the tree is in the range [0, 100].
#   -100 <= Node.val <= 100
from collections import defaultdict, deque
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional, List


# BFS - T/S: O(n*log(n)) due to sort on result, O(n)
# - use dict to save result, instead of deque
class Solution0:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = defaultdict(list)
        dq = deque([(root, int(0))])    # (value, col)
        while dq:
            node, col = dq.popleft()
            res[col].append(node.val)
            if node.left:
                dq.append((node.left, col-1))
            if node.right:
                dq.append((node.right, col+1))
            
        return [res[col] for col in sorted(res.keys())]


# BFS - T/S: O(n), O(n)
# - always from top to bottom, from left to right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = deque()
        dq = deque()
        leftCol = 0
        dq.append((root, 0))    # (value, col)
        while dq:
            node, col = dq.popleft()
            if col < leftCol:
                res.appendleft([])
                leftCol -= 1
            if col >= len(res) + leftCol:
                res.append([])

            res[col - leftCol].append(node.val)

            if node.left:
                dq.append((node.left, col-1))
            if node.right:
                dq.append((node.right, col+1))
            
        return list(res)


# DFS - Wrong
# - not correct when node from left half tree in lower level, and stretch 
#   to the right side, and is visited before those from right half tree 
#   and in higher level.
class Solution1:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        leftList = []
        rightList = []

        def dfsVisit(root, column):
            if not root:
                return
            value = root.val

            if column >= 0:
                lst = rightList
                col = column
            else:
                lst = leftList
                col = -column - 1     # -1, -2, -3, ... => 0, 1, 2, ...

            if col < len(lst):
                lst[col].append(value)
            else:
                lst.append([value])

            dfsVisit(root.left, column-1)
            dfsVisit(root.right, column+1)

        dfsVisit(root, 0)
        return leftList[::-1] + rightList


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
        r = sol.verticalOrder(root)
        print(r)
        assert r == [[9], [3, 15], [20], [7]]

        root = TreeNodeUtil.fromBfsList([3, 9, 8, 4, 0, 1, 7])
        r = sol.verticalOrder(root)
        print(r)
        assert r == [[4], [9], [3, 0, 1], [8], [7]]

        root = TreeNodeUtil.fromBfsList([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])
        r = sol.verticalOrder(root)
        print(r)
        assert r == [[4], [9, 5], [3, 0, 1], [8, 2], [7]]


    unitTest(Solution0())
    unitTest(Solution())
    
    # unitTest(Solution1())
    # DFS generate incorrect result:
    # [[4], [9, 5], [3, 0, 1], [2, 8], [7]]
