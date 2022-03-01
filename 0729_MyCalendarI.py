# You are implementing a program to use as your calendar. We can add a
# new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty
# intersection (i.e., some moment is common to both events).
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range
# of real numbers x such that start <= x < end.
# Implement the MyCalendar class:
#  - MyCalendar() Initializes the calendar object.
#  - boolean book(int start, int end) Returns True if the event can be
#    added to the calendar successfully without causing a double booking.
#    Otherwise, return False and do not add the event to the calendar.
# Constraints:
#   0 <= start < end <= 109
#   At most 1000 calls will be made to book.
from unittest import expectedFailure
import sortedcontainers


# Python also provides you with data structures similar to Java TreeMap
# http://www.grantjenks.com/docs/sortedcontainers/
class MyCalendar:
    def __init__(self):
        self.cal = sortedcontainers.SortedList()

    def book(self, start: int, end: int) -> bool:
        if self.cal:
            i = max(self.cal.bisect_left((start, end)) - 1, 0)
            j = min(self.cal.bisect_right((start, end)), len(self.cal) - 1)
            for k in range(i, j + 1):
                lo = max(self.cal[k][0], start)
                hi = min(self.cal[k][1], end)
                if lo < hi: return False

        self.cal.add((start, end))
        return True


class MyCalendar1:
    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        return True


if __name__ == '__main__':
    def unitTest():
        inputs = [["MyCalendar", "book", "book", "book", "book", "book"],
                  [[], [10, 20], [10, 20], [15, 25], [20, 30], [20, 30]]]
        expected = [None, True, False, False, True, False]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.fetch(k)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["MyCalendar", "book", "book", "book", "book",
                   "book", "book", "book", "book", "book", "book"],
                  [[], [47, 50], [33, 41], [39, 45], [33, 42], [25, 32],
                   [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]]]
        expected = [None, True, True, False, False, True, False, True, True, True, False]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
