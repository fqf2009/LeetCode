# You are given an integer array nums. A number x is lonely when it appears
# only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.
# Return all lonely numbers in nums. You may return the answer in any order.
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^6
from typing import List
from collections import Counter

# Time complexity: O(n), Space complexity O(n)
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res= []
        for n, freq in counter.items():
            if freq == 1 and (n + 1 not in counter) and (n - 1 not in counter):
                res.append(n)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findLonely(nums=[10, 6, 5, 8])
        print(r)
        assert(r == [10, 8])

        r = sol.findLonely(nums=[1, 3, 5, 3])
        print(r)
        assert(r == [1, 5])

    unitTest(Solution())
