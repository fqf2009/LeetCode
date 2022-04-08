# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached 
# again by continuously following the next pointer. Internally, pos is used to denote
# the index of the node that tail's next pointer is connected to. Note that pos is not 
# passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Constraints:
#   The number of the nodes in the list is in the range [0, 10^4].
#   -10^5 <= Node.val <= 10^5
#   pos is -1 or a valid index in the linked-list.
from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional


# Floyd's Tortoise and Hare: O(n)
# - Fast and slow pointers, each move 2 steps and 1 step
# - If there is no loop, fast one reach null, ends.
# - If there is loop, two pointers meet at certain time.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next        #type:ignore
            p2 = p2.next.next
            if p1 == p2:
                return True

        return False


if __name__ == "__main__":
    def unitTest(sol):
        head = ListNodeUtil.createCyclicList([3,2,0,-4], 1)
        r = Solution().hasCycle(head)
        print(r)
        assert r == True

        head = ListNodeUtil.createCyclicList([1,2], 0)
        r = Solution().hasCycle(head)
        print(r)
        assert r == True

        head = ListNodeUtil.createCyclicList([1], -1)
        r = Solution().hasCycle(head)
        print(r)
        assert r == False

    unitTest(Solution())
