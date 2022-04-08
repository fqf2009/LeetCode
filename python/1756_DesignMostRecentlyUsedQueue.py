# Design a queue-like data structure that moves the most recently
# used element to the end of the queue.
# Implement the MRUQueue class:
#  - MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
#  - int fetch(int k) moves the kth element (1-indexed) to the end of the
#    queue and returns it.
# Constraints:
#   1 <= n <= 2000
#   1 <= k <= n
#   At most 2000 calls will be made to fetch.
# Follow up: Finding an O(n) algorithm per fetch is a bit easy. Can you
# find an algorithm with a better complexity for each fetch call?
from collections import deque


# - deque does not support pop(k)
# - deque has better performance when deleting first half of items
class MRUQueue:
    def __init__(self, n: int):
        self.dq = deque(i+1 for i in range(n))

    def fetch(self, k: int) -> int:
        v = self.dq[k-1]
        del self.dq[k-1]
        self.dq.append(v)
        return v


class MRUQueue1:
    def __init__(self, n: int):
        self.que = [i for i in range(1, n+1)]

    def fetch(self, k: int) -> int:
        self.que.append(self.que.pop(k-1))
        return self.que[-1]


if __name__ == '__main__':
    def unitTest():
        inputs = [["MRUQueue", "fetch", "fetch", "fetch", "fetch"],
                  [[8], [3], [5], [2], [8]]]
        expected = [None, 3, 6, 2, 2]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = MRUQueue(n)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.fetch(k)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
