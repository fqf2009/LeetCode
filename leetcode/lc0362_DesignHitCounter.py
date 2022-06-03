# Design a hit counter which counts the number of hits received in the
# past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds granularity),
# and you may assume that calls are being made to the system in
# chronological order (i.e., timestamp is monotonically increasing).
# Several hits may arrive roughly at the same time.
# Implement the HitCounter class:
#  - HitCounter() Initializes the object of the hit counter system.
#  - void hit(int timestamp) Records a hit that happened at timestamp
#  - (in seconds). Several hits may happen at the same timestamp.
#  - int getHits(int timestamp) Returns the number of hits in the
#  - past 5 minutes from timestamp (i.e., the past 300 seconds).
# Constraints:
#   1 <= timestamp <= 2 * 10^9
#   All the calls are being made to the system in chronological
#       order (i.e., timestamp is monotonically increasing).
#   At most 300 calls will be made to hit and getHits.
# Follow up: What if the number of hits per second could be huge?
# Does your design scale?
from collections import deque


# deque
class HitCounter:
    def __init__(self):
        self.dq = deque()
        self.cnt = 0

    def hit(self, timestamp: int) -> None:
        self.getHits(timestamp)     # remove outdated hits to save memory

        if self.dq and self.dq[-1][0] == timestamp:
            self.dq[-1][1] += 1
        else:
            self.dq.append([timestamp, 1])

        self.cnt += 1

    def getHits(self, timestamp: int) -> int:
        while self.dq and self.dq[0][0] <= timestamp - 300:
            self.cnt -= self.dq[0][1]
            self.dq.popleft()

        return self.cnt


# fix-size array - circular
class HitCounter1:
    def __init__(self):
        self.log = [[0, 0] for _ in range(301)]  # [[t1, cnt1], [t2, cnt2],...]
        self.log[0][0] = 1
        self.start = 0
        self.end = 0
        self.cnt = 0

    def hit(self, timestamp: int) -> None:
        self.cnt += 1
        if timestamp == self.end:
            self.log[self.end][1] += 1
        else:
            self.end = (self.end + 1) % 301
            self.log[self.end][0] = timestamp
            self.log[self.end][1] = 1

        while self.log[self.start][0] <= timestamp - 300:
            self.cnt -= self.log[self.start][1]
            self.log[self.start][1] = 0
            self.start = (self.start + 1) % 301

    def getHits(self, timestamp: int) -> int:
        while self.log[self.start][0] <= timestamp - 300:
            self.cnt -= self.log[self.start][1]
            self.log[self.start][1] = 0
            # important when there is no hit for a long time and then a getHits, 
            # which will leads to end-less loop.
            if self.start == self.end:
                break
            self.start = (self.start + 1) % 301

        return self.cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

if __name__ == "__main__":

    def unit_test1(solution):
        print(solution.__name__)

        sol = solution()
        inputs = [
            ["hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"],
            [[1], [2], [3], [4], [300], [300], [301]],
        ]
        expected = [None, None, None, 3, None, 4, 3]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(sol, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    def unit_test2(solution):
        print(solution.__name__)

        sol = solution()
        inputs = [
            ["hit", "hit", "hit", "getHits", "getHits", "getHits", "getHits", "getHits", "hit", "getHits"],
            [[2], [3], [4], [300], [301], [302], [303], [304], [501], [600]],
        ]
        expected = [None, None, None, 3, 3, 2, 1, 0, None, 1]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(sol, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unit_test1(HitCounter)
    unit_test2(HitCounter)

    unit_test1(HitCounter1)
    unit_test2(HitCounter1)
