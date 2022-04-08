# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


from typing import List
# Binary search in sorted array: O(log(n)), where n is the length of shorter list
#  - Assume A, B are the two lists, where A is the shorter one
#  - pick a pos i, which split A into two parts: AL = A[:i+1], AR = A[i+1:]
#  - calculate a pos j in B to split B into, BL = B[:j+1], BR = [j+1:],
#    where j = (total_len_of_two_list // 2) - i - 2
#  - if total_len is even, len(AL) + len(BL) == len(AR) + len(BR)     == total_len // 2
#    if total_len is odd,  len(AL) + len(BL) == len(AR) + len(BR) - 1 == total_len // 2
#  - use binary search to find a pos i in A, to make sure,
#    A[i] <= B[j+1] and B[j] <= A[i+1], i.e., AL, BL are the smaller half of the two lists
#    combined, and AR, BR are the larger half of two.
#    if total_len is even: median = avg(max(A[i], B[j]), min(A[i+1], B[j+1]))
#    if total_len is odd:  median = min(A[i+1], B[j+1])
#  - Note there are edge case, where i, j can be -1 or len(either list)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        total = len(nums1) + len(nums2)
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = total // 2 - i - 2
            al = A[i] if i >= 0 else -2**63
            ar = A[i+1] if i+1 < len(A) else 2**63
            bl = B[j] if j >= 0 else -2**63
            br = B[j+1] if j+1 < len(B) else 2**63
            if al <= br and bl <= ar:
                if total % 2 == 0:
                    return (max(al, bl) + min(ar, br)) / 2
                else:
                    return min(ar, br)
            elif al > br:
                r = i - 1
            else:   # bl > ar
                l = i + 1


if __name__ == '__main__':
    def unitTest(sol):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

        nums1 = [0, 0]
        nums2 = [0, 0]
        expected = 0
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

        nums1 = []
        nums2 = [1]
        expected = 1
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

        nums1 = [2]
        nums2 = []
        expected = 2
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

        nums1 = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        expected = 7
        output = sol.findMedianSortedArrays(nums1, nums2)
        print(output)
        assert output == expected

    unitTest(Solution())
