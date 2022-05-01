# You are given a string number representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number 
# such that the value of the resulting string in decimal form is maximized. The test cases 
# are generated such that digit occurs at least once in number.
# Constraints:
#   2 <= number.length <= 100
#   number consists of digits from '1' to '9'.
#   digit is a digit from '1' to '9'.
#   digit occurs at least once in number.


# One-liner
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return str(max(int(number[:i] + number[i+1:]) for i, ch in enumerate(number) if ch == digit))


class Solution1:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        for i, ch in enumerate(number):
            if ch == digit:
                res = max(res, int(number[:i] + number[i+1:]))

        return str(res)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.removeDigit("123", digit = "3")
        print(r)
        assert r == '12'

        r = sol.removeDigit("1231", digit = "1")
        print(r)
        assert r == '231'

        r = sol.removeDigit("551", digit = "5")
        print(r)
        assert r == '51'

    unit_test(Solution())
    unit_test(Solution1())
