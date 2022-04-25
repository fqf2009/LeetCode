# You are given a 0-indexed 2D integer array flowers, where 
# flowers[i] = [starti, endi] means the ith flower will be in 
# full bloom from starti to endi (inclusive). You are also 
# given a 0-indexed integer array persons of size n, where 
# persons[i] is the time that the ith person will arrive to 
# see the flowers.
# Return an integer array answer of size n, where answer[i] is 
# the number of flowers that are in full bloom when the ith
# person arrives.
#
# Constraints:
#   1 <= flowers.length <= 5 * 10^4
#   flowers[i].length == 2
#   1 <= starti <= endi <= 10^9
#   1 <= persons.length <= 5 * 10^4
#   1 <= persons[i] <= 10^9
from collections import defaultdict
from itertools import accumulate, chain
from typing import List
from sortedcontainers import SortedDict
from bisect import bisect_left, bisect_right


# Sweep Line: T/S: O((f+p)*log(f+p)), O(f+p)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        res = [0] * len(persons)
        bloom = 0
        for _, delta, i in sorted(chain(((t, 2, i)for i, t in enumerate(persons)),
                chain.from_iterable([(t1, 1, 0), (t2+1, -1, 0)] for t1, t2 in flowers))):
            if delta == 2:
                res[i] = bloom
            else:
                bloom += delta

        return res


# from: https://leetcode.com/problems/number-of-flowers-in-full-bloom/discuss/1976804/Python3-2-Lines-Sort-and-Binary-Search
# idea: binary search for: how many flowers started bloom, minus how many ended bloom.
class Solution1:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end = sorted(a for a, _ in flowers), sorted(b for _, b in flowers)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]


# from: https://leetcode.com/problems/number-of-flowers-in-full-bloom/discuss/1977099/C%2B%2BPython-Binary-Search-and-Sweep-Line
class Solution2:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        bloom_by_time = SortedDict({0: 0})
        for i, j in flowers:
            bloom_by_time[i] = bloom_by_time.get(i, 0) + 1
            bloom_by_time[j + 1] = bloom_by_time.get(j + 1, 0) - 1

        bloom_count = list(accumulate(bloom_by_time.values()))
        return [bloom_count[bloom_by_time.bisect_right(t) - 1] for t in persons]


# Prefix Sum + Binary Search
# T/S: O(f*log(f) + p*log(f)), O(f)
class Solution3:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        bloom = defaultdict(int)
        for start, end in flowers:
            bloom[start] += 1
            bloom[end + 1] -= 1  # the end is inclusive

        bloom = [[0, 0]] + [list(x) for x in sorted(bloom.items())]
        for i in range(1, len(bloom)):
            bloom[i][1] += bloom[i - 1][1]
        # bloom.append([bloom[-1][0]+1, 0]) # unnecessary, because there is no flower at the end

        res = []
        for ptime in persons:
            i, j = 0, len(bloom)
            while i < j:
                k = (i + j) // 2
                if bloom[k][0] <= ptime:  # bisect.bisect_right
                    i = k + 1
                else:
                    j = k
            res.append(bloom[i - 1][1])

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.fullBloomFlowers([[19, 37], [19, 38], [19, 35]], [6, 7, 21, 1, 13, 37, 5, 37, 46, 43])
        print(r)
        assert r == [0, 0, 3, 0, 0, 2, 0, 2, 0, 0]

        r = sol.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11])
        print(r)
        assert r == [1, 2, 2, 2]

        r = sol.fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2])
        print(r)
        assert r == [2, 2, 1]

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
