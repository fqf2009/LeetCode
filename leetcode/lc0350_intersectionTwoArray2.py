from typing import List

# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must appear as many times 
# as it shows in both arrays and you may return the result in any order.

# hash table: Time O(m+n), Space O(m+n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for n in nums1:
            freq.setdefault(n, [0,0])[0] += 1
        for n in nums2:
            f = freq.get(n)
            if f: f[1] += 1
        res = []
        for n, f in freq.items():
            res.extend([n] * min(f))
        return res

# Sort and two pointers
# Time O(m*log(m) + n*log(n)) due to sort, Space O(1) except results
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res


if __name__ == "__main__":
    r = Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])
    print(r)
    assert(r == [2, 2])

    r = Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
    print(r)
    assert(r == [4, 9])
