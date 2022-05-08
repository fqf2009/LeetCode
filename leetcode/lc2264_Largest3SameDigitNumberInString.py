# You are given a string num representing a large integer. An integer is good
# if it meets the following conditions:
#  - It is a substring of num with length 3.
#  - It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no 
# such integer exists.
# Note:
#  - A substring is a contiguous sequence of characters within a string.
#  - There may be leading zeroes in num or a good integer.
# Constraints:
#   3 <= num.length <= 1000
#   num only consists of digits.
from itertools import chain


# One-liner
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # [""] - chain's argument must be iterable
        return max(chain([""], (num[i: i+3] for i in range(len(num)-2)
                                if len(set(num[i: i+3])) == 1)))


class Solution1:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_val = -1
        for i in range(len(num)-2):
            ss = num[i: i+3]
            if len(set(ss)) == 1:
                if int(ss) > max_val:
                    max_val = int(ss)
                    res = ss
        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.largestGoodInteger("222")
        print(r)
        assert r == "222"

        r = sol.largestGoodInteger("6777133339")
        print(r)
        assert r == "777"

        r = sol.largestGoodInteger("2300019")
        print(r)
        assert r == "000"

        r = sol.largestGoodInteger("42352338")
        print(r)
        assert r == ""

    unit_test(Solution())
    unit_test(Solution1())
