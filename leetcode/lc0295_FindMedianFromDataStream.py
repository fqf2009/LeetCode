# The median is the middle value in an ordered integer list. If the size of
# the list is even, there is no middle value and the median is the mean of
# the two middle values.
#   For example, for arr = [2,3,4], the median is 3.
#   For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#  - MedianFinder() initializes the MedianFinder object.
#  - void addNum(int num) adds the integer num from the data stream to
#    the data structure.
#  - double findMedian() returns the median of all elements so far.
#    Answers within 10-5 of the actual answer will be accepted.
# Constraints:
#   -10^5 <= num <= 10^5
#   There will be at least one element in the data structure before calling findMedian.
#   At most 5 * 10^4 calls will be made to addNum and findMedian.
# Follow up:
#  - If all integer numbers from the stream are in the range [0, 100],
#    how would you optimize your solution?
#  - If 99% of all integer numbers from the stream are in the
#    range [0, 100], how would you optimize your solution?
import heapq

# Self-balancing Binary Search Tree
# https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint
class MedianFinder2:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        return 0


# Maintain two heaps (hi: min-heap and lo: max-heap), and rebalance them.
# - heapq is min-heap, store -(num + 10**7) to simulate max-heap
# - rebalance, lo always maintain the same or one more item than hi:
#   a. first, push num to lo
#   b. then, pop max one from lo, push into hi
#   c. finally, if hi has more item than lo, pop min item from hi, push into lo
class MedianFinder:
    def __init__(self):
        self.lo = []    # low end half of all values, max-heap
        self.hi = []    # high end half of all values, min-heap
        self._shift = 10**7

    def addNum(self, num: int) -> None:
        num += self._shift
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.hi) < len(self.lo):
            return -self.lo[0] - self._shift
        else:
            return (-self.lo[0] + self.hi[0]) / 2 - self._shift


# !!! Wrong !!!
# https://stackoverflow.com/questions/18118090/python-heapq-not-being-pushed-in-right-order
# - The heapq functions do not keep your list sorted, but only guarantee 
#   that the heap property is maintained:
#       heap[k] <= heap[2*k+1]
#       heap[k] <= heap[2*k+2]
#   Consequently, heap[0] is always the smallest item.
# - When you want to iterate over the items in order of priority, you cannot simply 
#   iterate over the heap but need to pop until queue is empty. heappop() will take 
#   the first item, then reorganize the list to fulfil the heap invariant.
class MedianFinder1:
    def __init__(self):
        self.que = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.que, num)

    def findMedian(self) -> float:
        # print(self.que)
        n = len(self.que)
        return (self.que[n//2] + self.que[(n-1)//2]) / 2


if __name__ == '__main__':
    def unitTest(Finder):
        finder = Finder()
        inputs = [["addNum", "addNum", "findMedian", "addNum", "findMedian"],
                  [[1], [2], [], [3], []]]
        expected = [None, None, 1.5, None, 2.0]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(finder, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected

        finder = Finder()
        inputs = [["addNum", "findMedian", "addNum", "findMedian", "addNum",
                   "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
                  [[-1], [], [-2], [], [-3], [], [-4], [], [-5], []]]
        expected = [None, -1.0, None, -1.5, None, -2.0, None, -2.5, None, -3.0]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(finder, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected

    unitTest(MedianFinder)
    # unitTest(MedianFinder1)
