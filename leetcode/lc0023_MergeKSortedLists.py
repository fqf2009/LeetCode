# You are given an array of k linked-lists lists, each linked-list 
# is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Constraints:
#   k == lists.length
#   0 <= k <= 10^4
#   0 <= lists[i].length <= 500
#   -10^4 <= lists[i][j] <= 10^4
#   lists[i] is sorted in ascending order.
#   The sum of lists[i].length will not exceed 10^4.
from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional, List, Any
from queue import PriorityQueue
from dataclasses import dataclass, field
import heapq

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


# Merge with Divide And Conquer (Merge every two neighbour linked lists together each pass)
# Time complexity: O(k*n*log(k)), where n is average list length.
# Time complexity: O(N*log(k)), where N = k*n, which is the number of nodes from all lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists) == 1: return lists[0]     # only have one list
            head = p = ListNode()
            p1, p2 = lists[0], lists[1]
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            p.next = p1 if p1 else p2
            return head.next

        if len(lists) == 0: return None
        while len(lists) > 1:
            lists = [merge2Lists(lists[i:i+2]) for i in range(0, len(lists), 2)]

        return lists[0]


# Use heapq as PriorityQueue (in Python lib, PriorityQueue is based on heapq)
# - use a unique sequence as a tie-breaker, because the ListNode does not 
#   implement the comparison method like __eq__ etc.
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que = []
        seq = 0     # tie-breaker for tuples in Priority Queue
        for node in lists:
            if node:
                seq += 1
                heapq.heappush(que, (node.val, seq, node))

        head = p = ListNode()
        while len(que) > 0:
            _, _, p.next = heapq.heappop(que)
            p = p.next
            if p.next:
                seq += 1
                heapq.heappush(que, (p.next.val, seq, p.next))

        return head.next


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    node: Any = field(compare=False)

# Merge k-Lists using PriorityQueue: put all head nodes from k-Lists into a PriorityQueue,
# each time pop the smallest node, and push the next node of the poped-up node into queue.
# Time complexity: O(k*n*log(k)), where n is average list length.
# Time complexity: O(N*log(k)), where N = k*n, which is the number of nodes from all lists
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que = PriorityQueue(maxsize=len(lists))
        for node in lists:
            if node:
                que.put(PrioritizedItem(node.val, node))

        head = p = ListNode()
        while not que.empty():
            item = que.get()
            node = item.node
            p.next = node
            p = node
            if node.next:
                que.put(PrioritizedItem(node.next.val, node.next))

        return head.next


# TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
# A typical pattern for entries is a tuple in the form: (priority_number, data)
# If the data elements are not comparable, the data can be wrapped in a class 
# that ignores the data item and only compares the priority number.
# See Solution1.
class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que = PriorityQueue(maxsize=len(lists))
        for node in lists:
            if node:
                que.put((node.val, node))

        head = p = ListNode()
        while not que.empty():
            v, node = que.get()
            p.next = node
            p = p.next
            if node.next:
                que.put((node.next.val, node.next))

        return head.next


if __name__ == '__main__':
    def unitTest(sol):
        input = ListNodeUtil.createListOfLinkedList([[1, 4, 5], [1, 3, 4], [2, 6]])
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        h1 = sol.mergeKLists(input)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert(r == expected)

        input = ListNodeUtil.createListOfLinkedList([])
        expected = []
        h1 = sol.mergeKLists(input)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert(r == expected)

        input = ListNodeUtil.createListOfLinkedList([[]])
        expected = []
        h1 = sol.mergeKLists(input)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert(r == expected)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    # unitTest(Solution3())
