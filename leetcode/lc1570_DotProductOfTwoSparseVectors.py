# Given two sparse vectors, compute their dot product.
# Implement class SparseVector:
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse 
# vector efficiently and compute the dot product between two SparseVector.
# Follow up: What if only one of the vectors is sparse?
# Constraints:
#   n == nums1.length == nums2.length
#   1 <= n <= 10^5
#   0 <= nums1[i], nums2[i] <= 100
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.svec = {i: v for i, v in enumerate(nums) if v > 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        sv1, sv2 = self.svec, vec.svec
        if len(sv1) > len(sv2):
            sv1, sv2 = sv2, sv1

        res = 0
        for i, v in sv1.items():
            res += v * sv2.get(i, 0)

        return res


class SparseVector1:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def dotProduct(self, vec: 'SparseVector1') -> int:
        return sum(x*y for x, y in zip(self.nums, vec.nums))


if __name__ == '__main__':
    def unitTest(sol):
        v1 = sol([1, 0, 0, 2, 3])
        v2 = sol([0, 3, 0, 4, 0])
        r = v1.dotProduct(v2)
        print(r)
        assert r == 8

        v1 = sol([0, 1, 0, 0, 0])
        v2 = sol([0, 0, 0, 0, 2])
        r = v1.dotProduct(v2)
        print(r)
        assert r == 0

        v1 = sol([0, 1, 0, 0, 2, 0, 0])
        v2 = sol([1, 0, 0, 0, 3, 0, 4])
        r = v1.dotProduct(v2)
        print(r)
        assert r == 6

    unitTest(SparseVector)
    unitTest(SparseVector1)
