# Given a non-negative integer represented as a linked list of 
# digits, plus one to the integer.

# The digits are stored such that the most significant digit is 
# at the head of the list.

# Constraints:
#  - The number of nodes in the linked list is in the range [1, 100].
#  - 0 <= Node.val <= 9
#  - The number represented by the linked list does not contain leading
#    zeros except for the zero itself. 

from lib.ListUtil import ListNode, ListNodeUtil

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def plusOneHelper(node) -> int: # return carry
            if node.next:
                carry, node.val = divmod(node.val + plusOneHelper(node.next), 10)
            else:
                carry, node.val = divmod(node.val + 1, 10)
            return carry

        carry = plusOneHelper(head)
        if carry > 0:
            head = ListNode(carry, next = head)
        return head


if __name__ == "__main__":
    def unitTest(sol):
        head = ListNodeUtil.createLinkedList([1,2,3])
        r = ListNodeUtil.toArrayList(sol.plusOne(head))
        print(r)
        assert r == [1,2,4]

        head = ListNodeUtil.createLinkedList([9,9,9])
        r = ListNodeUtil.toArrayList(sol.plusOne(head))
        print(r)
        assert r == [1,0,0,0]

        head = ListNodeUtil.createLinkedList([0])
        r = ListNodeUtil.toArrayList(sol.plusOne(head))
        print(r)
        assert r == [1]

    unitTest(Solution())
