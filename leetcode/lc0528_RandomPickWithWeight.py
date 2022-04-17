# You are given a 0-indexed array of positive integers w where w[i]
# describes the weight of the ith index.
# You need to implement the function pickIndex(), which randomly picks
# an index in the range [0, w.length - 1] (inclusive) and returns it.
# The probability of picking an index i is w[i] / sum(w).
# For example, if w = [1, 3], the probability of picking index 0
# is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking
# index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
# Constraints:
#   1 <= w.length <= 10^4
#   1 <= w[i] <= 10^5
#   pickIndex will be called at most 10^4 times.
from random import random
from typing import List


# Math, Binary Search, Prefix Sum - Time Limit Exceeded???
# T/S: O(n + M*log(n)), O(n), where n is len(w), M is the number of calls
class Solution:
    def __init__(self, w: List[int]):
        n = len(w)
        self.weights = [0.0] * n
        self.weights[0] = float(w[0])
        for i, v in enumerate(w[1:], 1):
            self.weights[i] = self.weights[i-1] + v

    def pickIndex(self) -> int:
        r = random() * self.weights[-1]
        i, j = 0, len(self.weights) - 1
        while i < j:
            k = (i + j) // 2
            if self.weights[k] < r:
                i = k + 1
            else:
                j = k

        return i


if __name__ == "__main__":

    def unitTest():
        inputs = [["Solution", "pickIndex"], [[[1]], []]]
        expected = [None, 0]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])  # obj = Solution(w)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])  # obj.pickIndex()
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [ ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"],
                   [[[1, 3]], [], [], [], [], []] ]
        expected = [None, 1, 1, 1, 1, 0]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])  # obj = Solution(w)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])  # obj.pickIndex()
            outputs.append(r)
        print(outputs)
        # assert outputs == expected

        inputs = [ ["Solution", "pickIndex", "pickIndex", "pickIndex", 
                    "pickIndex", "pickIndex", "pickIndex", "pickIndex"],
                   [[[3, 14, 1, 7]], [], [], [], [], [], [], [], []] ]
        expected = [None, 0, 1, 1, 1, 3, 2, 3]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])  # obj = Solution(w)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])  # obj.pickIndex()
            outputs.append(r)
        print(outputs)
        # assert outputs == expected

    unitTest()
