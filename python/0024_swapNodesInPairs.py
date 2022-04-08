
from lib.ListUtil import ListNode, ListNodeUtil, List
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = dummyHead = ListNode(next=head)
        while p.next and p.next.next:
            p1, p2 = p.next, p.next.next
            p.next = p2
            p = p1
            p1.next = p2.next
            p2.next = p1

        return dummyHead.next


if __name__ == '__main__':
    def unitTest(sol):
        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4])
        h2 = Solution().swapPairs(h1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [2, 1, 4, 3])

        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        h2 = Solution().swapPairs(h1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [2, 1, 4, 3, 5])

        h1 = ListNodeUtil.createLinkedList([])
        h2 = Solution().swapPairs(h1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [])

        h1 = ListNodeUtil.createLinkedList([1])
        h2 = Solution().swapPairs(h1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [1])

    unitTest(Solution())
