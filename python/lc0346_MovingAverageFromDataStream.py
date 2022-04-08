# Given a stream of integers and a window size, calculate the moving
# average of all integers in the sliding window.
# Implement the MovingAverage class:
#  - MovingAverage(int size) Initializes the object with the size of 
#    the window size.
#  - double next(int val) Returns the moving average of the last size 
#    values of the stream.
# Constraints:
#   1 <= size <= 1000
#   -10^5 <= val <= 10^5
#   At most 104 calls will be made to next.
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.dq = deque()
        self.capacity = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.dq) == self.capacity:
            self.total -= self.dq.popleft()
        self.total += val
        self.dq.append(val)

        return self.total / len(self.dq)


if __name__ == '__main__':
    def unitTest(Solution):
        inputs = [ ["next", "next", "next", "next"],
                   [[1], [10], [3], [5]] ]
        expected = [None, 1.0, 5.5, 4.666666666666667, 6.0]
        outputs = [None]
        obj = Solution(3)                                   # obj = MovingAverage(size)
        for method, param in zip(inputs[0], inputs[1]):
            r = getattr(obj, method)(*param)                # obj.next(val)
            outputs.append(r)
        print(outputs)
        # assert outputs == expected

    unitTest(MovingAverage)
