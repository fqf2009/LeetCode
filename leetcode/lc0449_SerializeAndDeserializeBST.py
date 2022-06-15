# Serialization is converting a data structure or object into a 
# sequence of bits so that it can be stored in a file or memory 
# buffer, or transmitted across a network connection link to be
# reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search
# tree. There is no restriction on how your serialization/deserialization
# algorithm should work. You need to ensure that a binary search tree
# can be serialized to a string, and this string can be deserialized to
# the original tree structure.

# The encoded string should be as compact as possible.
# Constraints:
#   The number of nodes in the tree is in the range [0, 10^4].
#   0 <= Node.val <= 104
#   The input tree is guaranteed to be a binary search tree.
from collections import deque
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfsSerialize(root):
            if not root:
                res.append("")
                return
            res.append(str(root.val))
            dfsSerialize(root.left)
            dfsSerialize(root.right)

        res = []
        dfsSerialize(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfsDeserialize(dq):
            v = dq.popleft()
            if len(v) == 0:
                return None
            else:
                node = TreeNode(int(v))
                node.left = dfsDeserialize(dq)
                node.right = dfsDeserialize(dq)

            return node
        
        dq = deque(data.split(","))
        return dfsDeserialize(dq)


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("codec",), [(Codec,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([2,1,3], [2,1,3]),
                ([], []),
                ([1], [1]),
            ]
        )
        def test_maximumProduct(self, bfs_lst, expected):
            root = TreeNodeUtil.fromBfsList(bfs_lst)
            print("")
            print(self.codec.__name__)  # type: ignore
            ser = self.codec()          # type: ignore
            deser = self.codec()        # type: ignore
            r = ser.serialize(root)
            print('"' + r + '"')
            root2 = deser.deserialize(r)
            bfs_lst2 = TreeNodeUtil.toBfsList(root2)
            self.assertEqual(bfs_lst2, expected)

    main()
