# Given two numbers, hour and minutes, return the smaller angle
# (in degrees) formed between the hour and the minute hand.
# Answers within 10-5 of the actual value will be accepted as correct.
# Constraints:
#   1 <= hour <= 12
#   0 <= minutes <= 59


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_minute = (360 / 60) * float(minutes)
        angle_hour = (360 / 12) * (float(hour % 12) + minutes / 60)
        angle = max(angle_hour, angle_minute) - min(angle_hour, angle_minute)

        return angle if angle <= 180 else 360 - angle


class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_minute = (360 / 60) * float(minutes)
        angle_hour = (360 / 12) * (float(hour % 12) + minutes / 60)
        angle = abs(angle_hour - angle_minute)

        return min(angle, 360 - angle)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.angleClock(1, 57)
        print(r)
        assert r == 76.5

        r = sol.angleClock(12, 30)
        print(r)
        assert r == 165.0

        r = sol.angleClock(3, 30)
        print(r)
        assert r == 75.0

        r = sol.angleClock(3, 15)
        print(r)
        assert r == 7.5

    unit_test(Solution())
    unit_test(Solution1())
