# You are given the head of a linked list, which contains a series 
# of integers separated by 0's. The beginning and end of the linked 
# list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between 
# them into a single node whose value is the sum of all the merged 
# nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.

# Constraints:
#   The number of nodes in the list is in the range [3, 2 * 10^5].
#   0 <= Node.val <= 1000
#   There are no two consecutive nodes with Node.val == 0.
#   The beginning and end of the linked list have Node.val == 0.
from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil


# Linked List: O(n)
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h0 = p = ListNode()
        p1 = head
        while p1 and p1.next:
            p.next = ListNode(val=0)
            p = p.next
            p1 = p1.next
            while p1 and p1.val != 0:
                p.val += p1.val
                p1 = p1.next

        return h0.next


if __name__ == '__main__':
    def unitTest(sol):
        head = ListNodeUtil.createLinkedList([0, 3, 1, 0, 4, 5, 2, 0])
        r = ListNodeUtil.toArrayList(sol.mergeNodes(head))
        print(r)
        assert r == [4, 11]

        head = ListNodeUtil.createLinkedList([0, 1, 0, 3, 0, 2, 2, 0])
        r = ListNodeUtil.toArrayList(sol.mergeNodes(head))
        print(r)
        assert r == [1, 3, 4]

    unitTest(Solution())
