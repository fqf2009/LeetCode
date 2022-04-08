from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = p = ListNode()
        while l1 or l2 or carry > 0:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0

            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            
            carry, v = divmod(n1 + n2 + carry, 10)
            p.next = ListNode(v)
            p = p.next

        return head.next


if __name__ == '__main__':
    sol = Solution()

    h1 = ListNodeUtil.createLinkedList([2, 4, 3])
    h2 = ListNodeUtil.createLinkedList([5, 6, 4])
    h3 = sol.addTwoNumbers(h1, h2)
    r = ListNodeUtil.toArrayList(h3)
    print(r)
    assert(r == [7, 0, 8])

    h1 = ListNodeUtil.createLinkedList([0])
    h2 = ListNodeUtil.createLinkedList([0])
    h3 = sol.addTwoNumbers(h1, h2)
    r = ListNodeUtil.toArrayList(h3)
    print(r)
    assert(r == [0])

    h1 = ListNodeUtil.createLinkedList([9, 9, 9, 9, 9, 9, 9])
    h2 = ListNodeUtil.createLinkedList([9, 9, 9, 9])
    h3 = sol.addTwoNumbers(h1, h2)
    r = ListNodeUtil.toArrayList(h3)
    print(r)
    assert(r == [8, 9, 9, 9, 0, 0, 0, 1])

    sol = Solution()
    h1 = ListNodeUtil.createLinkedList([9, 9, 9, 9, 9])
    h2 = ListNodeUtil.createLinkedList([1])
    h3 = sol.addTwoNumbers(h1, h2)
    r = ListNodeUtil.toArrayList(h3)
    print(r)
    assert(r == [0, 0, 0, 0, 0, 1])
