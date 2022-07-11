# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a
# sequence of moves to transform one string to the other.
# Constraints:
#   1 <= start.length <= 10^4
#   start.length == end.length
#   Both start and end will only consist of characters in 'L', 'R', and 'X'.


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        S = [(ch, i) for i, ch in enumerate(start) if ch in "LR"]
        E = [(ch, i) for i, ch in enumerate(end) if ch in "LR"]

        if len(S) != len(E):
            return False

        for (ch1, i), (ch2, j) in zip(S, E):
            if ch1 != ch2 or (ch1 == "L" and i < j) or (ch1 == "R" and i > j):
                return False

        return True


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.canTransform("RXXLRXRXL", "XRLXXRRLX")
        print(r)
        assert r == True

        r = sol.canTransform("X", "L")
        print(r)
        assert r == False

        r = sol.canTransform("XR", "RX")
        print(r)
        assert r == False

    unit_test(Solution())
