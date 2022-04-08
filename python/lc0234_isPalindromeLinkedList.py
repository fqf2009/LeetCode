from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional

# Given the head of a singly linked list, return true if it is a palindrome.

# Go to the middle of the list, reverse the half in-place, and then compare the
# two of the half list, restore (another reverse) the half back.
# Time Complexity: O(n), Space Complexity: O(1)
# There is one place can be improved: use two points to find middle node.
class Solution:
    def listDepth(self, head: Optional[ListNode]) -> int:
        res = 0
        p = head
        while p != None:
            p = p.next
            res += 1

        return res

    def ReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = self.listDepth(head)
        if n <= 1:
            return True

        p1, p2 = head, head
        for i in range((n + 1) // 2):
            assert(p2)
            p2 = p2.next
 
        p2 = self.ReverseList(p2)
        p3 = p2
        res = True
        for i in range(n // 2):
            assert(p1)
            assert(p2)
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next
            p2 = p2.next                

        self.ReverseList(p3)
        return res


if __name__ == "__main__":
    h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
    h2 = Solution().ReverseList(h1)
    lst = ListNodeUtil.toArrayList(h2)
    print(lst)
    assert(lst == [5, 4, 3, 2, 1])

    h1 = ListNodeUtil.createLinkedList([1,2,2,1])
    r = Solution().isPalindrome(h1)
    print(r)
    assert(r == True)
    lst = ListNodeUtil.toArrayList(h1)
    assert(lst == [1,2,2,1] )

    h1 = ListNodeUtil.createLinkedList([1,2])
    r = Solution().isPalindrome(h1)
    print(r)
    assert(r == False)
    lst = ListNodeUtil.toArrayList(h1)
    assert(lst == [1,2] )
