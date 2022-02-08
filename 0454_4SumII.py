# Given four integer arrays nums1, nums2, nums3, and nums4 all
# of length n, return the number of tuples (i, j, k, l) such that:
#   0 <= i, j, k, l < n
#   nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
from typing import List
from collections import Counter
from itertools import product

# https://leetcode.com/problems/4sum-ii/discuss/1740490/Java-or-3-liner-or-Simple-or-Explained
# Note this problem is different than the 4Sum (0018) problem: this one only need the count!!!
# so, to further improve performance, we can use more space:
#  - Use a, b, c, d to represent numbers from 4 arrays
#  - compute (a + b) value and count (frequency) into a hashmap (Counter): O(n^2)
#  - compute (c + d) value and count (frequency) into a hashmap (Counter): O(n^2)
#  - iterate on Counter(a+b), and test whether (-a-b) is in Counter(c+d): O(n^2)
# T/S: O(n^2), O(n^2)
#
# Here is the actual result (30ms, 30 times faster)
# .: %%timeit
# .: %run 0454_4SumII.py
#    1342435
#    ...
# 1342435
# 30.5 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        freq1 = Counter(map(lambda x: x[0] + x[1], product(nums1, nums2)))
        freq2 = Counter(map(lambda x: x[0] + x[1], product(nums3, nums4)))
        # note freq2[-x[0]] returns 0 if -x[0] is not in freq2
        res = sum(map(lambda x: x[1] * freq2[-x[0]], freq1.items()))

        return res


# LeetCode: time exceeded.
# Here is the actual result (less than 1s) for last test case:
# .: %%timeit
# .: %run 0454_4SumII.py
#    1342435
#    ...
#    961 ms ± 34.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# Time complexity: O(n^3), Space complexity: O(n)
#  - Similar to 4Sum, sort first, for the 3rd and 4th array, one use forward
#    scan, another use backward scan, to reduce 4 levels of loop into 3 levels.
#  - Note: use Counter to cope with duplicate values.
class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        freq1 = sorted(list(Counter(nums1).items()))
        freq2 = sorted(list(Counter(nums2).items()))
        freq3 = sorted(list(Counter(nums3).items()))
        freq4 = sorted(list(Counter(nums4).items()))
        res = 0
        for i in range(len(freq1)):
            for j in range(len(freq2)):
                k, l = 0, len(freq4) - 1
                while k < len(freq3) and l >= 0:
                    total = freq1[i][0] + freq2[j][0] + freq3[k][0] + freq4[l][0]
                    if total == 0:
                        res += freq1[i][1] * freq2[j][1] * freq3[k][1] * freq4[l][1]
                        k += 1
                        l -= 1
                    elif total < 0:
                        k += 1
                    else:
                        l -= 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
        print(r)
        assert r == 2

        r = sol.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0])
        print(r)
        assert r == 1

        r = sol.fourSumCount(nums1=[0, 0], nums2=[0, 0], nums3=[0, 0], nums4=[0, 0])
        print(r)
        assert r == 16

        nums1 = [-3,-82,-16,41,-20,-59,21,96,8,-28,87,32,5,-84,29,-6,-79,24,87,-71,24,95,-67,-1,59,49,14,20,12,77,79,-86,-69,-62,-91,-69,61,-56,-98,-84,73,88,-29,72,-43,76,-57,10,43,-57,-73,63,30,-32,33,45,18,37,24,93,56,70,27,-54,17,54,37,-52,88,-13,64,2,-79,-17,-66,-36,-91,3,47,-52,-91,63,80,34,-77,80,58,-27,75,97,77,58,22,-2,-65,52,95,54,-80,-41,-29,-43,46,-99,14,46,70,47,-18,-67,-73,-8,88,32,-39,53,48,-10,-91,32,28,36,85,-32,-27,-36,52,-64,-92,78,-32,47,11,92,16,-98,93,-10,-81,-8,-99,2]
        nums2 = [19,22,84,-84,81,-37,-53,13,10,85,-25,26,-21,99,-23,9,-16,-62,1,-6,-91,-50,86,39,-72,78,-92,-87,19,-67,-39,-67,-62,-76,23,59,96,-31,-63,-52,75,85,7,-32,99,16,-90,98,64,-59,73,-3,38,-61,36,100,59,-91,23,79,34,-7,-65,89,16,18,-100,-77,93,19,3,-71,-71,32,42,-6,87,64,81,-38,-86,32,-59,-33,61,-72,-11,-47,18,-10,-82,53,24,-52,-12,-73,95,42,-29,39,-8,-71,31,40,59,-90,54,77,99,-9,57,-3,-26,53,-69,77,80,-10,-78,-10,82,84,69,-89,72,-22,74,-4,-38,51,7,-78,-69,79,-71,44,29,-75,-92,44,7,-6]
        nums3 = [-55,-90,-43,-90,68,8,30,-40,61,-83,51,77,-31,-74,-53,71,-40,45,95,-68,17,66,33,-31,-47,-66,-47,3,81,50,-63,60,13,-57,92,73,83,-79,61,-93,-100,-34,23,-100,90,-81,-18,-92,-57,12,42,-51,55,71,-17,97,-40,-2,58,-13,82,83,-11,35,-53,44,-48,60,-76,94,84,-55,-43,62,-45,71,14,-64,84,-100,-2,50,25,-84,-13,-17,27,96,-45,-47,-98,66,21,-63,51,-36,-76,88,50,-67,-22,33,96,-69,-18,44,26,71,19,60,48,43,62,89,11,-57,56,-52,-45,-35,27,-46,-11,65,94,-88,-38,32,-39,81,-92,61,-31,-43,-90,40,34,-49,-88,83,31,75]
        nums4 = [-64,-62,12,6,-62,-21,-18,54,-90,18,-76,-12,8,-46,27,65,-8,91,-4,-23,-40,-19,19,-7,15,-1,76,28,71,37,12,13,17,35,82,67,-18,-64,-86,-34,-28,-41,41,-48,23,0,40,-11,2,89,69,12,7,-14,-78,7,-37,25,100,-63,4,18,35,-78,-27,-60,91,-65,87,14,-79,94,3,52,-48,3,-91,98,27,0,8,85,98,-38,-34,-87,-53,72,33,-79,33,-76,11,22,71,-7,-22,91,64,38,85,-43,35,5,3,-19,36,-99,31,-18,-24,3,-71,-64,-1,-1,41,-10,3,-99,36,44,0,-47,-99,-40,-42,63,94,49,29,-47,0,-69,11,11,-23,25,29,66,-20,47]
        r = sol.fourSumCount(nums1, nums2, nums3, nums4)
        print(r)
        assert r == 1342435

    unitTest(Solution())
    unitTest(Solution1())
