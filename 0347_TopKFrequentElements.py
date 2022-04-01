# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# Constraints:
#   1 <= nums.length <= 10^5
#   k is in the range [1, the number of unique elements in the array].
#   It is guaranteed that the answer is unique.
# Follow up: Your algorithm's time complexity must be better than
#            O(n log n), where n is the array's size.
import heapq
from typing import Counter, List


# Counter: O(n*log(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [v for v, f in counter.most_common(k)]


# Priority Queue: O(n + n*log(k)) => O(n*log(k))
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        que = []
        heapq.heapify(que)
        for val, freq in counter.items():
            if len(que) >= k:
                if que[0][0] < freq:
                    heapq.heapreplace(que, (freq, val))
            else:
                heapq.heappush(que, (freq, val))

        return [val for _, val in que]


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2)
        print(r)
        assert r == [1, 3] or r == [3, 1]

        r = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        print(r)
        assert r == [1, 2] or r == [2, 1]

        r = sol.topKFrequent([1], 1)
        print(r)
        assert r == [1]

    unit_test(Solution())
    unit_test(Solution1())
