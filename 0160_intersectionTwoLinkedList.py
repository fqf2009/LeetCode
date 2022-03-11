# Given the heads of two singly linked-lists headA and headB, return the  
# node at which the two lists intersect. If the two linked lists have no 
# intersection at all, return null.
# Example 1:
#   Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], 
#          skipA = 2, skipB = 3
#   Output: Intersected at '8'
#   Explanation: The intersected node's value is 8 (note that this must not 
#                be 0 if the two lists intersect). From the head of A, it 
#                reads as [4,1,8,4,5]. From the head of B, it reads as
#                [5,6,1,8,4,5]. There are 2 nodes before the intersected node 
#                in A; There are 3 nodes before the intersected node in B.
# Constraints:
#   The number of nodes of listA is in the m.
#   The number of nodes of listB is in the n.
#   1 <= m, n <= 3 * 10^4
#   1 <= Node.val <= 10^5
#   0 <= skipA < m
#   0 <= skipB < n
#   intersectVal is 0 if listA and listB do not intersect.
#   intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
from lib.ListUtil import ListNode, ListNodeUtil, List
from typing import Optional

# Analysis: O(m+n)
# - assume there is intersection between two linked list, and the length are:
#   ListA: L1 + L3, ListB: L2 + L3, where L3 is the common part
# - use two pointers to visit two list simultaneously, when reach the end,
#   swith to another list, and continue, the two  pathes will be: 
#       Pointer1: L1 -> L3 -> L2 -> L3
#       Pointer1: L2 -> L3 -> L1 -> L3
# - If there is intersection, the best case scenario is L1 = L2,
#   the normal case is L1 != L2, but they meet at second L3.
# - If no intersection, both pointer are None at the end of second L3.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next
            pb = pb.next
            if pa == None and pb == None:
                return None
            if not pa: pa = headB 
            if not pb: pb = headA 

        return pa


# Approach 3 from LeetCode website.
# - bug: Because pa and pb will never be None, if both lists 
#        do not intersect, it will be an endless loop
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            if not pa.next and not pb.next: return None # fix bug
            pa = pa.next if pa.next else headB
            pb = pb.next if pb.next else headA

        return pa


if __name__ == "__main__":
    def unitTest(sol):
        lst = ListNodeUtil.createIntersectedLinkedList([4,1,8,4,5], [5,6,1,8,4,5], 2, 3)
        expected = [8, 4, 5]
        h2 = sol.getIntersectionNode(lst[0], lst[1])
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == expected)

        lst = ListNodeUtil.createIntersectedLinkedList([1,9,1,2,4], [3,2,4], 3, 1)
        expected = [2, 4]
        h2 = sol.getIntersectionNode(lst[0], lst[1])
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == expected)

        lst = ListNodeUtil.createIntersectedLinkedList([2,6,4], [1,5], 3, 2)
        expected = []
        h2 = sol.getIntersectionNode(lst[0], lst[1])
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == expected)

    unitTest(Solution())
    unitTest(Solution1())
