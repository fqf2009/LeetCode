# You are given two strings current and correct representing two 24-hour times.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM 
# is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes.
# You can perform this operation any number of times.
# Return the minimum number of operations needed to convert current to correct.
# Constraints:
#   current and correct are in the format "HH:MM"
#   current <= correct


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_number(s):
            h, m = s.split(':')
            return int(h)*60 + int(m)

        time1 = to_number(current)
        time2 = to_number(correct)
        # if time1 > time2: time2 += 1440   # no need, according to constraints

        gap = time2 - time1
        adjusts = [60, 15, 5, 1]
        res = 0
        for val in adjusts:
            ops, gap = divmod(gap, val)
            res += ops

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.convertTime(current = "02:30", correct = "04:35")
        print(r)
        assert r == 3

        r = sol.convertTime(current = "11:00", correct = "11:01")
        print(r)
        assert r == 1

    unit_test(Solution())
