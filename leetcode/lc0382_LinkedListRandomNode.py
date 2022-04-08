from lib.ListUtil import ListNode, ListNodeUtil
import random

# https://en.wikipedia.org/wiki/Reservoir_sampling
# Reservoir sampling is a family of randomized algorithms for choosing a simple random
# sample, without replacement, of k items from a population of unknown size n in a single 
# pass over the items. The size of the population n is not known to the algorithm and is 
# typically too large for all n items to fit into main memory. The population is revealed 
# to the algorithm over time, and the algorithm cannot look back at previous items. At  
# any point, the current state of the algorithm must permit extraction of a simple random 
# sample without replacement of size k over the part of the population seen so far.

# Code below is from leetcode
# My solution will be:
# - just keep the list size, adjust each time on append or delete
# - compute which node to take: random.random()*size; then traverse to that node
class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    # O(n)
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
