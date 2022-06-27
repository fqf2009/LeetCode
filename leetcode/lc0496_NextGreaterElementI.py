# The next greater element of some element x in an array is the first greater 
# element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where
# nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. If there is no next 
# greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater 
# element as described above.
# Constraints:
#   1 <= nums1.length <= nums2.length <= 1000
#   0 <= nums1[i], nums2[i] <= 104
#   All integers in nums1 and nums2 are unique.
#   All the integers of nums1 also appear in nums2.
from typing import List


# Monotonic Stack: T/S: O(n), O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []      # Monotonic decreasing, because we want next greater
        right = {}      # greater value on the right
        for v in nums2:
            while stack and stack[-1] < v:
                right[stack.pop()] = v
            stack.append(v)
        
        res = [-1] * len(nums1)
        for i, v in enumerate(nums1):
            res[i] = right.get(v, -1)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.nextGreaterElement([4,1,2], nums2 = [1,3,4,2])
        print(r)
        assert r == [-1,3,-1]

        r = sol.nextGreaterElement([2,4], nums2 = [1,2,3,4])
        print(r)
        assert r == [3,-1]

    unit_test(Solution())
