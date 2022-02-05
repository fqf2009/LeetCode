# There are n people in a social group labeled from 0 to n - 1.
# You are given an array logs where logs[i] = [timestampi, xi, yi]
# indicates that xi and yi will be friends at the time timestampi.

# Friendship is symmetric. That means if a is friends with b, then
# b is friends with a. Also, person a is acquainted with a person b
# if a is friends with b, or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted
# with every other person. If there is no such earliest time, return -1.

# Constraints:
#  * 2 <= n <= 100
#  * 1 <= logs.length <= 104
#  * logs[i].length == 3
#  * 0 <= timestampi <= 109
#  * 0 <= xi, yi <= n - 1
#  * xi != yi
#  * All the values timestampi are unique.
#  * All the pairs (xi, yi) occur at most one time in the input.

from typing import List


# Union Find: O(n + m*log(m) + m*a(n)), where
#   n is to initialize the UnionFind,
#   m*log(m) is the sort,
#   m*a(n) is the union operation.
#   a(n) is Ackermann_function to estimate cost of each union operation
# reference:
#   https://en.wikipedia.org/wiki/Ackermann_function#Inverse
#   https://www.cnblogs.com/gczr/p/12077934.html
# To get better performance:
#   - always connect small tree to large tree to reduce the depth of combined tree
#   - compress the path when finding root, i.e. for each non-root node in search path,
#     points to its grand-parent node.
class UnionFind:
    def __init__(self, n: int):
        self.grpCnt = n
        self.root = list(range(n))  # root of every node, i.e., each node points to itself
        self.size = [1] * n         # each tree has the size of 1

    def union(self, p1, p2):        # connect two nodes, union the trees of each node belongs to
        r1 = self.find(p1)
        r2 = self.find(p2)
        if r1 == r2:                # two nodes are in the same tree
            return
        if self.size[r1] > self.size[r2]:
            r1, r2 = r2, r1
        self.root[r1] = r2          # connect small tree to large tree to reduce depth
        self.size[r2] += self.size[r1]
        self.grpCnt -= 1            # reduce group count

    def find(self, p):              # find root of the node of the tree
        while p != self.root[p]:
            self.root[p] = self.root[self.root[p]]  # compress the path when finding root
            p = self.root[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.grpCnt


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort(key=lambda x: x[0])
        for x in logs:
            uf.union(x[1], x[2])
            if uf.count() == 1:
                return x[0]

        return -1


if __name__ == '__main__':
    def unit_test(sol):
        logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3],
                [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
                [20190312, 1, 2], [20190322, 4, 5]]
        r = sol.earliestAcq(logs, 6)
        print(r)
        assert r == 20190301

        logs = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
        r = sol.earliestAcq(logs, 4)
        print(r)
        assert r == 3

    unit_test(Solution())
