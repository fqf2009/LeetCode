# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
# add the key-value pair to the cache. If the number of keys exceeds the capacity from 
# this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Use dict (hash table) for fast get/put operations (O(1)), and use double linked list to achieve
# LRU functionality, i.e., move to head of list when accessing, pop and delete from tail when
# capacity is not enough.
# Constraints:
#   1 <= capacity <= 3000
#   0 <= key <= 10^4
#   0 <= value <= 10^5
#   At most 2 * 10^5 calls will be made to get and put.
from typing import Optional


class DLinkedNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev: Optional[DLinkedNode] = prev
        self.next: Optional[DLinkedNode] = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def _add_node(self, node: DLinkedNode):
        assert(self.head.next)
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _del_node(self, node: DLinkedNode):
        assert(node.prev)
        assert(node.next)
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: DLinkedNode):
        self._del_node(node)
        self._add_node(node)

    def _pop_from_tail(self) -> DLinkedNode:
        node = self.tail.prev
        assert(node != self.head)
        assert(node)
        self._del_node(node)
        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self._move_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add_node(node)
            if len(self.cache) > self.capacity:
                node = self._pop_from_tail()
                del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    # test case
    inputs = [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
              [[2], [1, 'A'], [2, 'B'], [1], [3, 'C'], [2], [4, 'D'], [1], [3], [4]]
             ]
    expected = [None, None, None, 'A', None, -1, None, -1, 'C', 'D']
    outputs = [None]
    obj = globals()[inputs[0][0]](*inputs[1][0])
    for i in range(1, len(inputs[0])):
        outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
    print(outputs)
    assert outputs == expected
