# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a
# file or memory buffer, or transmitted across a network connection
# link to be reconstructed later in the same or another computer
# environment.
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree
# can be serialized to a string and this string can be deserialized
# to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode
# serializes a binary tree. You do not necessarily need to follow
# this format, so please be creative and come up with different
# approaches yourself.
# Constraints:
#   The number of nodes in the tree is in the range [0, 10^4].
#   -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs_serialize(root):
            if not root:
                res.append("None")
            else:
                res.append(str(root.val))
                dfs_serialize(root.left)
                dfs_serialize(root.right)

        dfs_serialize(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")

        def dfs_deserialize(i):
            if i == len(lst):
                return (None, i)

            if lst[i] == "None":
                return (None, i + 1)
            else:
                root = TreeNode(int(lst[i]))
                root.left, i = dfs_deserialize(i + 1)
                root.right, i = dfs_deserialize(i)
                return (root, i)

        return dfs_deserialize(0)[0]


class Codec1:
    def serialize(self, root):
        res = []

        def dfs_serialize(root):
            if not root:
                res.append("None")
            else:
                res.append(str(root.val))
                dfs_serialize(root.left)
                dfs_serialize(root.right)

        dfs_serialize(root)
        return ",".join(res)

    def deserialize(self, data):
        def dfs_deserialize(dq):
            if dq[0] == "None":
                dq.popleft()
                return None
            else:
                root = TreeNode(int(dq.popleft()))
                root.left = dfs_deserialize(dq)
                root.right = dfs_deserialize(dq)
                return root

        return dfs_deserialize(deque(data.split(",")))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("codec",), [(Codec,), (Codec1,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5]),
                ([], []),
            ]
        )
        def test_maximumProduct(self, bfs_lst, expected):
            root = TreeNodeUtil.fromBfsList(bfs_lst)
            print("")
            print(self.codec.__name__)  # type: ignore
            ser = self.codec()          # type: ignore
            deser = self.codec()        # type: ignore
            r = ser.serialize(root)
            print(r)
            root2 = deser.deserialize(r)
            bfs_lst2 = TreeNodeUtil.toBfsList(root2)
            self.assertEqual(bfs_lst2, expected)

    main()
