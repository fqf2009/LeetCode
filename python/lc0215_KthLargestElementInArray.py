# Given an integer array nums and an integer k, return the kth
# largest element in the array.
# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.

# Constraints:
#   1 <= k <= nums.length <= 10^4
#   -10^4 <= nums[i] <= 10^4
import random
from typing import List
import heapq

# QuickSelect: O(n)
# https://en.wikipedia.org/wiki/Quickselect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # to partition nums[left, right+1] around nums[pvt_idx],
        # and then return new pivot index
        def partition(left, right):
            pvt_idx = random.randint(left, right)
            pivot = nums[pvt_idx]
            # move pivot to the end
            nums[pvt_idx], nums[right] = nums[right], nums[pvt_idx]

            # move items smaller than pivot to the left
            pvt_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[pvt_idx], nums[i] = nums[i], nums[pvt_idx]
                    pvt_idx += 1

            # move pivot back to pvt_idx position
            nums[pvt_idx], nums[right] = nums[right], nums[pvt_idx]

            return pvt_idx
        
        # select k-th smallest item from nums[] (not nums[left: right+1])
        def select(left, right, kth):
            if left == right: return nums[left]
            # randint get random int in [a, b], not [a, b)
            pvt_idx = partition(left, right)
            if kth == pvt_idx:
                return nums[kth]
            elif kth < pvt_idx:
                return select(left, pvt_idx-1, kth)
            else:
                return select(pvt_idx+1, right, kth)

        return select(0, len(nums)-1, len(nums)-k)


# PriorityQueue (heapq) - T/S: O(n*log(k)), O(k)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for v in nums:
            if len(hq) < k:
                heapq.heappush(hq, v)
            elif v > hq[0]:
                    heapq.heapreplace(hq, v)

        return hq[0]


# Heap sort: O(n*log(k))
# - heapq take O(log(n)) time to store a value
# - before heapify, nlargest take log(k) time to store a value
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# Quick sort or merge sort: O(n*log(n))
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
        print(r)
        assert r == 5

        r = sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        print(r)
        assert r == 4

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
