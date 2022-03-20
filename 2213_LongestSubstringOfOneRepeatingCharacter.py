# You are given a 0-indexed string s. You are also given a 0-indexed string
# queryCharacters of length k and a 0-indexed array of integer indices
# queryIndices of length k, both of which are used to describe k queries.
# The ith query updates the character in s at index queryIndices[i] to the
# character queryCharacters[i].
# Return an array lengths of length k where lengths[i] is the length of
# the longest substring of s consisting of only one repeating character
# after the ith query is performed.
# Example 1:
# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation:
# - 1st query updates s = "bbbacc". The longest substring consisting of
#   one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc".
#   The longest substring consisting of one repeating character can be
#   "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring consisting of
#   one repeating character is "bbbb" with length 4.
#   Thus, we return [3,3,4].
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of lowercase English letters.
#   k == queryCharacters.length == queryIndices.length
#   1 <= k <= 10^5
#   queryCharacters consists of lowercase English letters.
#   0 <= queryIndices[i] < s.length
from typing import List, Optional
import math


class Node:
    def __init__(self, prefix: str, prefixLen: int, suffix: str, suffixLen: int,
                 lrcLen: int, segLen: int) -> None:
        self.prefix: str = prefix
        self.prefixLen: int = prefixLen
        self.suffix: str = suffix
        self.suffixLen: int = suffixLen
        # self.lrc = lrc
        self.lrcLen: int = lrcLen    # Length of longest repeating char
        self.segLen: int = segLen    # Segment Length

    def update(self, ch: str):
        assert self.segLen == 1
        self.prefix = self.suffix = ch

    @staticmethod
    def mergeNodes(left: Optional['Node'], right: Optional['Node']) -> Optional['Node']:
        if not left and not right:
            return None
        if not right:
            return left
        if not left:
            return right
        prefixLen, suffixLen = left.prefixLen, right.suffixLen
        if left.prefixLen == left.segLen and left.prefix == right.prefix:
            prefixLen += right.prefixLen
        if right.suffixLen == right.segLen and left.suffix == right.suffix:
            suffixLen += left.suffixLen
        lrcLen = max(prefixLen, suffixLen, left.lrcLen, right.lrcLen,
                     (left.suffixLen + right.prefixLen) if left.suffix == right.prefix else 0)
        return Node(left.prefix, prefixLen, right.suffix, suffixLen,
                    lrcLen, left.segLen+right.segLen)


# SegmentTree - node relationship
# total storage: 2*n
# i - branch node
# (i) leaf node
# node i's chilren: 2i+1, 2i+2
# node i's parent : (i-1)//2
#
#                                            0
#                         1                                    2
#              3                      4                  5           6
#         7         8         9           (10)       (11)  (12)  (13)  (14)
#     (15) (16) (17) (18) (19)
#
# - However, in this problem, we have to use "Complete Binary Tree" to maintain
#   the order (or the position) of characters in string
#
#                                 0
#                  1                            2
#           3             4               5             6
#       (7)   (8)     (9)   (10)     (11)   (12)   (13)   (14)
class SegementTree:
    def __init__(self, data: str) -> None:
        n = 1 if len(data) == 1 else len(data) - 1
        # self.size - number of leaves in complete binary tree
        # branch size will be self.size -1, i.e. tree[0: self.size -1]
        self.size = 2 ** (int(math.log(n, 2)) + 1)
        self.tree: List[Optional[Node]] = [None] * (self.size*2)
        for i in range(self.size-1, self.size-1 + len(data)):
            ch = data[i-(self.size-1)]
            self.tree[i] = Node(prefix=ch, prefixLen=1, suffix=ch, suffixLen=1, lrcLen=1, segLen=1)
        for i in reversed(range(self.size-1)):
            self.tree[i] = Node.mergeNodes(self.tree[i*2+1], self.tree[i*2+2])

    def update(self, idx: int, ch: str):
        i = self.size - 1 + idx
        node = self.tree[i]
        assert node
        node.update(ch)
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = Node.mergeNodes(self.tree[i*2+1], self.tree[i*2+2])

    def longestRepeatingCharLength(self):
        node = self.tree[0]
        assert node
        return node.lrcLen


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegementTree(s)
        res = []
        for i, ch in zip(queryIndices, queryCharacters):
            st.update(i, ch)
            res.append(st.longestRepeatingCharLength())

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestRepeating("seeu", "qjcqvsnhq", [3, 1, 0, 2, 1, 3, 3, 1, 0])
        print(r)
        assert r == [2, 1, 1, 2, 2, 1, 1, 1, 1]

        r = sol.longestRepeating("d", "voeleb", [0, 0, 0, 0, 0, 0])
        print(r)
        assert r == [1, 1, 1, 1, 1, 1]

        r = sol.longestRepeating(s="babacc", queryCharacters="bcb", queryIndices=[1, 3, 3])
        print(r)
        assert r == [3, 3, 4]

        r = sol.longestRepeating(s="abyzz", queryCharacters="aa", queryIndices=[2, 1])
        print(r)
        assert r == [2, 3]

        n = 100000
        r = sol.longestRepeating("a"*n, "z"*n, list(range(n)))
        print(r)
        assert r == list(reversed(range(n//2, n))) + list(range(n//2 + 1, n+1))

    unitTest(Solution())
