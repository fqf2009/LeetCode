# Given the head of a singly linked list, return true if it is a palindrome.
# Constraints:
#   The number of nodes in the list is in the range [1, 10^5].
#   0 <= Node.val <= 9
from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil


# Reverse Linked List in place at middle - T/S: O(n), O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(head: ListNode) -> ListNode:
            p1, p2 = head, head.next
            while p2:
                p3 = p2.next
                p2.next = p1
                p1, p2 = p2, p3
            head.next = None
            return p1

        def list_len(head: Optional[ListNode]) -> int:
            res = 0
            while head:
                res += 1
                head = head.next
            return res

        n = list_len(head)
        if n < 2: return True

        p = head
        for _ in range((n+1) // 2 - 1): # one place before right half for restoration of list
            p = p.next      # type: ignore
        
        res = True
        p1 = head
        p2 = reverse_list(p.next)   # type: ignore
        p3 = p2     # save for restoration of list
        for _ in range(n//2):
            if p1.val != p2.val:    # type: ignore
                res = False
                break
            p1, p2 = p1.next, p2.next   # type: ignore
        
        p.next = reverse_list(p3)       # type: ignore
        return res


# Linked List to Array - T/S: O(n), O(n)
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        n = len(lst)
        return lst[:n//2] == lst[(n+1)//2:][::-1]


# Linked List to Array - T/S: O(n), O(n)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        return all(lst[i] == lst[-1-i] for i in range(len(lst)//2))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,2,2,1], True),
            ([1,2], False),
        ])
        def test_isPalindrome(self, arr, expected):
            sol = self.solution()       # type:ignore
            head = ListNodeUtil.createLinkedList(arr)
            r = sol.isPalindrome(head)
            self.assertEqual(r, expected)

    main()
