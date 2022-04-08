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


# Dict + Priority: put: O(log(capacity)), get: O(log(capacity))
# - note python heapq or PriorityQueue is min heap.
class LFUCache:
    def __init__(self, capacity: int):
        self.seq = 1
        self.capacity = capacity
        self.cache = {}
        self.pq = []
        heapq.heapify(self.pq)

    def printStack(self):
        for node in self.cache.values():
            print(node)
        print('--------------------------')

    def get(self, key: int) -> int:
        if key in self.cache:
            self.seq += 1
            node = self.cache[key]
            self.pq.remove(node)
            node.freq += 1
            node.seq = self.seq
            heapq.heappush(self.pq, node)
            # print (f'get ({key})')
            # self.printStack()
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
        # print (f'put ({key}, {value})')
        # self.printStack()


if __name__ == '__main__':
    def unitTest():
        inputs = [["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]]
        expected = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = LFUCache(capacity)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["LFUCache", "put", "put", "put", "put", "get"],
                  [[2], [3, 1], [2, 1], [2, 2], [4, 4], [2]]]
        expected = [None, None, None, None, None, 2]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = LFUCache(capacity)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["LFUCache", "put", "get"],
                  [[0], [0, 0], [0]]]
        expected = [None, None, -1]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = LFUCache(capacity)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get",
                   "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get",
                   "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put",
                   "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put",
                   "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put",
                   "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get",
                   "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put",
                   "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get",
                   "put", "put", "put", "put", "put", "put", "put"],
                  [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
                   [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14],
                   [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23],
                   [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5],
                   [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12],
                   [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8],
                   [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1],
                   [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4],
                   [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]]
        # LeetCode test case result, most like is wrong
        # expected = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None,
        #             -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None,
        #             -1, None, -1, 24, None, None, 18, None, None, None, None, 14, None, None, 18, None, None, 11,
        #             None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, 11, None, None,
        #             None, None, 29, None, None, None, None, 17, -1, 18, None, None, None, -1, None, None, None,
        #             20, None, None, None, 29, 18, 18, None, None, None, None, 20, None, None, None, None, None,
        #             None, None]
        expected = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None,
                    -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, 
                    -1, None, -1, 24, None, None, 18, None, None, None, None, 14, None, None, 18, None, None, 11, 
                    None, None, None, None, None, 18, None, None, 24, None, 4, 29, 30, None, 12, 11, None, None, 
                    None, None, 29, None, None, None, None, -1, -1, 18, None, None, None, 24, None, None, None, 
                    20, None, None, None, 29, 18, 18, None, None, None, None, 20, None, None, None, None, None, 
                    None, None]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = LFUCache(capacity)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.get(key), obj.pub(key)
            outputs.append(r)
        print(outputs)
        assert outputs == expected
    unitTest()
