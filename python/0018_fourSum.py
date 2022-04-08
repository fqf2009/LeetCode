# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
from typing import List
from collections import defaultdict, Counter

# Inspired by 0454_4SumII, here is the T/S: O(n^2), O(n^2) solution???
# 58.6 ms ± 1.2 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# manually compare, instead of frozenset() and sorted():
# 25.4 ms ± 717 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
# Remove the dedup code, the performance is terrible: 11 seconds !!!
# 10.9 s ± 107 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = Counter(nums)
        nums = []
        for v, cnt in freq.items():
            nums.extend([v] * min(cnt, 4))

        n = len(nums)
        twoSum = defaultdict(set)
        for i in range(n - 1):
            for j in range(i + 1, n):   # i always < j
                twoSum[nums[i] + nums[j]].add((i, j))

        quadSet = set() # set to make sure unique quadruplets
        for v, idx1 in twoSum.items():
            if target - v in twoSum:
                idx2 = twoSum[target - v]
                for x in idx1:
                    for y in idx2:
                        # if len(frozenset(x + y)) == 4: # subscription, i.e., a, b, c, d are distinct
                        #     quadSet.add(tuple(sorted(([nums[x[0]], nums[x[1]], nums[y[0]], nums[y[1]]]))))
                        if x[0] < y[0]:
                            a = x[0]
                            if x[1] < y[0]:
                                b, c, d = x[1], y[0], y[1]
                            elif x[1] == y[0]:
                                continue
                            elif x[1] < y[1]:
                                b, c, d = y[0], x[1], y[1]
                            elif x[1] == y[1]:
                                continue
                            else:
                                b, c, d = y[0], y[1], x[1]
                            quadSet.add((nums[a], nums[b], nums[c], nums[d]))

        return [list(x) for x in quadSet]


# Mimic solution for 3-Sum problem:
# First sort, then three level of loops, in the inner-most level of loop,
# use two pointers from both ends to scan.
# Time complexity: O(n^3)
# Before dedup: 391 ms ± 14.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# After dedup: 63.5 ms ± 2.92 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = Counter(nums)
        nums = []
        for v, cnt in sorted(freq.items()):
            nums.extend([v] * min(cnt, 4))

        # nums.sort() # already sorted in dedup
        res = set()
        for i in range(0, len(nums)-3):     # if len(nums) < 4, still safe
            for j in range(i + 1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    sum4 = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum4 == target:
                        res.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif sum4 < target:
                        k += 1
                    else:
                        l -= 1

        return [list(x) for x in res]


# Recursive: O(n^3)
# General solution for N-Sum: O(n^(N-1))
# N will not be very big, so the stack memory consumption is not a concern
# 172 ms ± 2.51 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
class Solution2:
    def recursiveNSum(self, nums: List[int], target: int, n: int, freq: dict[int, int]):
        res = set()

        if len(nums) < n:
            return res

        if n == 1:
            if target >= nums[0] and target in freq:
                res.add((target,))
            return res

        for i in range(len(nums)):
            nSum = self.recursiveNSum(nums[i + 1:], target - nums[i], n - 1, freq)
            for x in nSum:
                res.add(tuple(sorted([nums[i]] + list(x))))

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        nums2 = []
        for i, n in sorted(freq.items()):
            nums2.extend([i] * min(n, 4))

        nSum = self.recursiveNSum(nums2, target, 4, freq)
        return [list(x) for x in nSum]


# Iteration (no recursion), sort and uniq avoid last level of iteration.
# But too many kind of validations, terrible code!
# Time complexity: O(n^3)
# 192 ms ± 15.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
class Solution3:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        uniqNums = list(sorted(freq.keys()))

        nSum = set()
        for i in range(len(uniqNums)):
            if freq[uniqNums[i]] >= 4 and uniqNums[i] * 4 == target:
                nSum.add((uniqNums[i], uniqNums[i], uniqNums[i], uniqNums[i]))
            for j in range(i + 1, len(uniqNums)):
                if freq[uniqNums[i]] >= 3 and (uniqNums[i] * 3 + uniqNums[j]) == target:
                    nSum.add((uniqNums[i], uniqNums[i], uniqNums[i], uniqNums[j]))
                if freq[uniqNums[i]] >= 2 and freq[uniqNums[j]] >= 2 and (uniqNums[i] * 2 + uniqNums[j] * 2) == target:
                    nSum.add((uniqNums[i], uniqNums[i], uniqNums[j], uniqNums[j]))
                if freq[uniqNums[j]] >= 3 and (uniqNums[i] + uniqNums[j] * 3) == target:
                    nSum.add((uniqNums[i], uniqNums[j], uniqNums[j], uniqNums[j]))
                if freq[uniqNums[j]] >= 4 and uniqNums[j] * 4 == target:
                    nSum.add((uniqNums[j], uniqNums[j], uniqNums[j], uniqNums[j]))
                for k in range(j + 1, len(uniqNums)):
                    if freq[uniqNums[i]] >= 3 and (uniqNums[i] * 3 + uniqNums[k]) == target:
                        nSum.add((uniqNums[i], uniqNums[i], uniqNums[i], uniqNums[k]))
                    if freq[uniqNums[i]] >= 2 and (uniqNums[i] * 2 + uniqNums[j] + uniqNums[k]) == target:
                        nSum.add((uniqNums[i], uniqNums[i], uniqNums[j], uniqNums[k]))
                    if freq[uniqNums[j]] >= 2 and (uniqNums[i] + uniqNums[j] * 2 + uniqNums[k]) == target:
                        nSum.add((uniqNums[i], uniqNums[j], uniqNums[j], uniqNums[k]))
                    if freq[uniqNums[j]] >= 3 and (uniqNums[j] * 3 + uniqNums[k]) == target:
                        nSum.add((uniqNums[j], uniqNums[j], uniqNums[j], uniqNums[k]))
                    if freq[uniqNums[i]] >= 2 and freq[uniqNums[k]] >= 2 and (uniqNums[i] * 2 + uniqNums[k] * 2) == target:
                        nSum.add((uniqNums[i], uniqNums[i], uniqNums[k], uniqNums[k]))
                    if freq[uniqNums[k]] >= 2 and (uniqNums[i] + uniqNums[j] + uniqNums[k] * 2) == target:
                        nSum.add((uniqNums[i], uniqNums[j], uniqNums[k], uniqNums[k]))
                    if freq[uniqNums[j]] >= 2 and freq[uniqNums[k]] >= 2 and (uniqNums[j] * 2 + uniqNums[k] * 2) == target:
                        nSum.add((uniqNums[j], uniqNums[j], uniqNums[k], uniqNums[k]))
                    if freq[uniqNums[k]] >= 3 and (uniqNums[i] + uniqNums[k] * 3) == target:
                        nSum.add((uniqNums[i], uniqNums[k], uniqNums[k], uniqNums[k]))
                    if freq[uniqNums[k]] >= 3 and (uniqNums[j] + uniqNums[k] * 3) == target:
                        nSum.add((uniqNums[j], uniqNums[k], uniqNums[k], uniqNums[k]))
                    if freq[uniqNums[k]] >= 4 and (uniqNums[k] * 4) == target:
                        nSum.add((uniqNums[k], uniqNums[k], uniqNums[k], uniqNums[k]))
                    left = target - uniqNums[i] - uniqNums[j] - uniqNums[k]
                    if left > uniqNums[k] and left in freq:
                        nSum.add((uniqNums[i], uniqNums[j], uniqNums[k], left))

        return [list(x) for x in nSum]


# Brute force, too slow: O(n^4)
# 1.11 s ± 172 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
class Solution4:
    def fourSum(self, nums: List[int], target: int) -> List[list[int]]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        nums2 = []
        for i, n in freq.items():
            nums2.extend([i] * min(n, 4))
        nums2.sort

        nSum = set()
        for i in range(len(nums2) - 3):
            for j in range(i + 1, len(nums2) - 2):
                for k in range(j + 1, len(nums2) - 1):
                    for l in range(k + 1, len(nums2)):
                        if nums2[i] + nums2[j] + nums2[k] + nums2[l] == target:
                            nSum.add((nums2[i], nums2[j], nums2[k], nums2[l]))

        return [list(x) for x in nSum]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.fourSum([0, 0, 4, -4, -2, 3], 8)
        print(r)
        assert(r == [])

        r = sol.fourSum([0, 0, 0], 0)
        print(r)
        assert(r == [])

        r = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
        r = sorted([sorted(x) for x in r])
        print(r)
        assert(r == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

        r = sol.fourSum([2, 2, 2, 2, 2], 8)
        print(r)
        assert(r == [[2, 2, 2, 2]])

        r = sol.fourSum([-2, -1, -1, 1, 1, 2, 2], 0)
        r = sorted([sorted(x) for x in r])
        print(r)
        assert(r == [[-2, -1, 1, 2], [-1, -1, 1, 1]])

        r = sol.fourSum([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30,
                         30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50, 50, 50,
                         50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                         70, 70, 70, 70, 70, 70, 70, 70, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                         90, 90, 90, 90], 200)
        print(r)

        r = sol.fourSum([-493, -487, -480, -464, -456, -449, -445, -439, -437, -427, -415, -403, -400, -398, -372, -349, -347, -332, -330, -324, -287, -282, -273, -254, -249, -243, -220,
                         -219, -217, -217, -214, -199, -198, -170, -153, -150, -143, -136, -113, -93, -91, -88, -87, -78, -58, -58, -55, -51, -49, -42, -38, -36, -26, 0, 13, 28, 54, 61, 85, 90,
                         90, 111, 118, 136, 138, 167, 170, 172, 195, 198, 205, 209, 241, 263, 290, 302, 324, 328, 347, 359, 373, 390, 406, 417, 435, 439, 443, 446, 464, 465, 468, 484, 486, 492, 493], -4437)
        print(r)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
    unitTest(Solution4())
