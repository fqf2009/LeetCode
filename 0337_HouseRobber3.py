from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# The thief has found himself a new place for his thievery again. There is only one entrance to this
# area, called root. Besides the root, each house has one and only one parent house. After a tour, 
# the smart thief realized that all houses in this place form a binary tree. It will automatically 
# contact the police if two directly-linked houses were broken into on the same night. Given the root 
# of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# DFS + Memorization
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfsRob(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if root in memo:
                return memo[root]
            v1, v2 = 0, 0
            if root.left:
                v1 = dfsRob(root.left.left) + dfsRob(root.left.right)
            if root.right:
                v2 = dfsRob(root.right.left) + dfsRob(root.right.right)
            v3 = dfsRob(root.left) + dfsRob(root.right)
            res = max(root.val + v1 + v2, v3)
            memo[root] = res
            return res

        memo = {}
        return dfsRob(root)


# Time Limit Exceeded
class Solution1:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfsRob(root: Optional[TreeNode], RootOk: bool) -> int:
            if not root:
                return 0
            res1 = dfsRob(root.left, True) + dfsRob(root.right, True)
            res2 = 0
            if RootOk:
                res2 = root.val + dfsRob(root.left, False) + dfsRob(root.right, False)
            return max(res1, res2)

        return dfsRob(root, True)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([3, 2, 3, None, 3, None, 1])
    r = sol.rob(root)
    print(r)
    assert r == 7

    root = TreeNodeUtil.fromBfsList([3, 4, 5, 1, 3, None, 1])
    r = sol.rob(root)
    print(r)
    assert r == 9

    root = TreeNodeUtil.fromBfsList(
        [
            79,
            99,
            77,
            None,
            None,
            None,
            69,
            None,
            60,
            53,
            None,
            73,
            11,
            None,
            None,
            None,
            62,
            27,
            62,
            None,
            None,
            98,
            50,
            None,
            None,
            90,
            48,
            82,
            None,
            None,
            None,
            55,
            64,
            None,
            None,
            73,
            56,
            6,
            47,
            None,
            93,
            None,
            None,
            75,
            44,
            30,
            82,
            None,
            None,
            None,
            None,
            None,
            None,
            57,
            36,
            89,
            42,
            None,
            None,
            76,
            10,
            None,
            None,
            None,
            None,
            None,
            32,
            4,
            18,
            None,
            None,
            1,
            7,
            None,
            None,
            42,
            64,
            None,
            None,
            39,
            76,
            None,
            None,
            6,
            None,
            66,
            8,
            96,
            91,
            38,
            38,
            None,
            None,
            None,
            None,
            74,
            42,
            None,
            None,
            None,
            10,
            40,
            5,
            None,
            None,
            None,
            None,
            28,
            8,
            24,
            47,
            None,
            None,
            None,
            17,
            36,
            50,
            19,
            63,
            33,
            89,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            94,
            72,
            None,
            None,
            79,
            25,
            None,
            None,
            51,
            None,
            70,
            84,
            43,
            None,
            64,
            35,
            None,
            None,
            None,
            None,
            40,
            78,
            None,
            None,
            35,
            42,
            98,
            96,
            None,
            None,
            82,
            26,
            None,
            None,
            None,
            None,
            48,
            91,
            None,
            None,
            35,
            93,
            86,
            42,
            None,
            None,
            None,
            None,
            0,
            61,
            None,
            None,
            67,
            None,
            53,
            48,
            None,
            None,
            82,
            30,
            None,
            97,
            None,
            None,
            None,
            1,
            None,
            None,
        ]
    )
    r = sol.rob(root)
    print(r)
    assert(r == 3038)