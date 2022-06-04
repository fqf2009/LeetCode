# Design and implement a data structure for a Least Frequently Used (LFU) cache.
# Implement the LFUCache class:
#  - LFUCache(int capacity) Initializes the object with the capacity of the
#    data structure.
#  - int get(int key) Gets the value of the key if the key exists in the cache.
#    Otherwise, returns -1.
#  - void put(int key, int value) Update the value of the key if present, or
#    inserts the key if not already present. When the cache reaches its capacity,
#    it should invalidate and remove the least frequently used key before inserting
#    a new item. For this problem, when there is a tie (i.e., two or more keys with
#    the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key
# in the cache. The key with the smallest use counter is the least frequently used key.
# When a key is first inserted into the cache, its use counter is set to 1 (due to the
# put operation). The use counter for a key in the cache is incremented either a get or
# put operation is called on it.
# The functions get and put must each run in O(1) average time complexity.
# Constraints:
#   0 <= capacity <= 10^4
#   0 <= key <= 10^5
#   0 <= value <= 10^9
#   At most 2 * 10^5 calls will be made to get and put.
import heapq
from typing import Optional


class Node:
    def __init__(self, freq, seq, key, value):
        self.freq = freq
        self.seq = seq
        self.key = key
        self.value = value

    def __eq__(self, next: 'Node'):
        return self.key == next.key

    def __lt__(self, next: 'Node'):
        return self.freq < next.freq or (self.freq == next.freq and self.seq < next.seq)

    def __str__(self) -> str:
        return f'[key: {self.key}, value: {self.value}, freq: {self.freq}, seq: {self.seq}]'


# Incorrect! But why???
# Dict + Priority: put: O(log(capacity)), get: O(log(capacity))
# - note python heapq or PriorityQueue is min heap.
class LFUCache:
    def __init__(self, capacity: int):
        self.seq = 1
        self.capacity = capacity
        self.cache = {}
        self.pq = []
        heapq.heapify(self.pq)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.seq += 1
            node = self.cache[key]
            self.pq.remove(node)
            node.freq += 1
            node.seq = self.seq
            heapq.heappush(self.pq, node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        self.seq += 1
        if key in self.cache:
            node = self.cache[key]
            self.pq.remove(node)
            node.freq += 1
            node.seq = self.seq
            node.value = value
            heapq.heappush(self.pq, node)
        else:
            if self.capacity == len(self.cache):
                node = heapq.heappop(self.pq)
                del self.cache[node.key]
            node = Node(1, self.seq, key, value)
            self.cache[key] = node
            heapq.heappush(self.pq, node)


# doubly linked node
class DLNode:
    def __init__(self, key: int, val: int, freq: int):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev: DLNode = self
        self.next: DLNode = self

# doubly-linked list for every frequency!
# T/S: O(1), O(n)
class LFUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._nodes = {}
        self._freq = {}
        self.min_freq = 1

    def _remove(self, node: DLNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.min_freq == node.freq and self._is_empty_freq(node.freq):
            self.min_freq = node.freq + 1

    def _add(self, node: DLNode):
        head = self._freq.setdefault(node.freq, DLNode(-1, -1, node.freq))
        node.prev, node.next = head, head.next
        node.next.prev, head.next = node, node

    def _is_empty_freq(self, freq):
        return freq not in self._freq or self._freq[freq].next == self._freq[freq]

    def get(self, key: int) -> int:
        if key not in self._nodes: return -1
        node = self._nodes[key]
        self._remove(node)
        node.freq += 1
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key not in self._nodes:
            if len(self._nodes) >= self.capacity:
                lfu_node = self._freq[self.min_freq].prev
                self._remove(lfu_node)
                del self._nodes[lfu_node.key]
            node = DLNode(key, value, 1)
            self._nodes[key] = node
            self.min_freq = 1
            self._add(node)
        else:
            node = self._nodes[key]
            node.val = value
            self._remove(node)
            node.freq += 1
            self._add(node)


if __name__ == '__main__':
    def unit_test1(Cache):
        print(Cache.__name__)

        cache = Cache(2)    # cache = LFUCache(capacity)
        inputs = [["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                  [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]]
        expected = [None, None, 1, None, -1, 3, None, -1, 3, 4]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(cache, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        cache = Cache(2)
        inputs = [["put", "put", "put", "put", "get"],
                  [[3, 1], [2, 1], [2, 2], [4, 4], [2]]]
        expected = [None, None, None, None, 2]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(cache, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        cache = Cache(0)
        inputs = [["put", "get"],
                  [[0, 0], [0]]]
        expected = [None, -1]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(cache, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        cache = Cache(10)
        inputs = [["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get",
                   "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get",
                   "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put",
                   "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put",
                   "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put",
                   "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get",
                   "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put",
                   "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get",
                   "put", "put", "put", "put", "put", "put", "put"],
                  [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
                   [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14],
                   [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23],
                   [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5],
                   [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12],
                   [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8],
                   [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1],
                   [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4],
                   [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]]
        expected = [None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None,
                    -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None,
                    -1, None, -1, 24, None, None, 18, None, None, None, None, 14, None, None, 18, None, None, 11,
                    None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, 11, None, None,
                    None, None, 29, None, None, None, None, 17, -1, 18, None, None, None, -1, None, None, None,
                    20, None, None, None, 29, 18, 18, None, None, None, None, 20, None, None, None, None, None,
                    None, None]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(cache, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    # unit_test1(LFUCache) # incorrect
    unit_test1(LFUCache1)
