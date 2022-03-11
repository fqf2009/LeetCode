# Given the head of a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that
# can be reached again by continuously following the next pointer. Internally,
# pos is used to denote the index of the node that tail's next pointer is
# connected to (0-indexed). It is -1 if there is no cycle. Note that pos is
# not passed as a parameter.
# Do not modify the linked list.
# Constraints:
#   The number of the nodes in the list is in the range [0, 10^4].
#   -10^5 <= Node.val <= 10^5
#   pos is -1 or a valid index in the linked-list.
from typing import List, Optional
from lib.ListUtil import ListNode, ListNodeUtil


# Floyd's Tortoise and Hare: O(n)
# - Fast and slow pointers, each move 2 steps and 1 step
# - If there is no loop, fast reach null, ends
# - If there is loop, and assume length of non-loop and loop portions are L and C,
#   where fast pointer meets slow one:
#       2(L + X) = L + n*C + X,  where X is slow pointer moved in loop portion
#         =>    L + X = n*C
# - Now set slow point back to list head, and both pointers move another L steps,
#   at the same speed, they will meet at the intersection
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next        #type:ignore
            p2 = p2.next.next
            if p1 == p2:
                p1 = head
                while p1 != p2:
                    p1, p2 = p1.next, p2.next   #type:ignore
                return p1

        return None


if __name__ == "__main__":
    def unitTest(sol):
        head = ListNodeUtil.createCyclicList([3, 2, 0, -4], 1)
        r = Solution().detectCycle(head)
        assert r and r.val == 2
        print(r.val)

        head = ListNodeUtil.createCyclicList([1, 2], 0)
        r = Solution().detectCycle(head)
        assert r and r.val == 1
        print(r.val)

        head = ListNodeUtil.createCyclicList([1], 0)
        r = Solution().detectCycle(head)
        assert r and r.val == 1
        print(r.val)

        head = ListNodeUtil.createCyclicList([1], -1)
        r = Solution().detectCycle(head)
        print(r)
        assert not r

    unitTest(Solution())
