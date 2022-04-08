# Given a binary array data, return the minimum number of swaps required
# to group all 1’s present in the array together in any place in the array.

from typing import List


# Sliding window
# - count 1s first, it is the size of windows with all 1s.
# - then use a sliding window of this size to count max 1s or min 0s in it.
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n1s = data.count(1)
        n1sInWin = data[:n1s].count(1)
        max1s = n1sInWin
        for i in range(n1s, len(data)):
            if data[i] == 1:
                n1sInWin += 1
            if data[i - n1s] == 1:
                n1sInWin -= 1
            max1s = max(max1s, n1sInWin)

        return n1s - max1s


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minSwaps(data=[1, 0, 1, 0, 1])
        print(r)
        assert r == 1

        r = sol.minSwaps(data=[0, 0, 0, 1, 0])
        print(r)
        assert r == 0

        r = sol.minSwaps(data=[1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1])
        print(r)
        assert r == 3

    unitTest(Solution())
