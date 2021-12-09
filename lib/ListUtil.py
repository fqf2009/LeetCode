from typing import Optional
# from dataclasses import dataclass

from typing import List

# Definition for singly-linked list.
# @dataclass(order=True)
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class ListNodeUtil:
    @staticmethod
    def createLinkedList(nums: list[int]) -> Optional[ListNode]:
        if len(nums) == 0:
            return None

        head = ListNode()
        p = head
        for i in range(len(nums)):
            p.next = ListNode(nums[i])
            p = p.next

        return head.next

    @staticmethod
    def createListOfLinkedList(lst: list[list[int]]) -> list[Optional[ListNode]]:
        if len(lst) == 0:
            return []

        res = []
        for nums in lst:
            res.append(ListNodeUtil.createLinkedList(nums))
        return res

    @staticmethod
    def createIntersectedLinkedList(nums1: list[int], nums2: list[int], skip1: int, skip2: int) -> list[Optional[ListNode]]:
        p1 = h1 = ListNode()
        p2 = h2 = ListNode()
        for n in nums1[:skip1]:
            p1.next = ListNode(n)
            p1 = p1.next
        for n in nums2[:skip2]:
            p2.next = ListNode(n)
            p2 = p2.next
        
        p3 = p1
        for n in nums1[skip1:]:
            p1.next = ListNode(n)
            p1 = p1.next
        p2.next = p3.next

        return [h1.next, h2.next]

    @staticmethod
    def createCyclicList(nums: list[int], pos) -> Optional[ListNode]:
        if len(nums) == 0:
            return None

        p0, tail = None, None
        for i in reversed(range(len(nums))):
            p = ListNode(nums[i])
            p.next = p0
            if tail == None:
                tail = p
            if pos == i:
                tail.next = p
            p0 = p

        return p0

    @staticmethod
    def toArrayList(head: Optional[ListNode]) -> list[int]:
        res = []
        p = head
        while p != None:
            res.append(p.val)
            p = p.next

        return res

    # Reverse list iteratively
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        p, p1 = head, head.next
        while p1 != None:
            p2 = p1
            p1 = p1.next
            p2.next = p
            p = p2

        head.next = None
        return p

    # Reverse list recursively
    @staticmethod
    def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(head: Optional[ListNode]) -> tuple:
            if head == None:
                return (None, None)
            if head.next == None:
                return (head, head)
            h1, tail = reverseListHelper(head.next)
            tail.next = head
            head.next = None
            return (h1, head)

        return reverseListHelper(head)[0]


if __name__ == "__main__":
    h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
    h2 = ListNodeUtil.reverseList(h1)
    lst = ListNodeUtil.toArrayList(h2)
    print(lst)
    assert(lst == [5, 4, 3, 2, 1])

    h1 = ListNodeUtil.createLinkedList([3, 7, 8])
    h2 = ListNodeUtil.reverseList2(h1)
    lst = ListNodeUtil.toArrayList(h2)
    print(lst)
    assert(lst == [8, 7, 3])
