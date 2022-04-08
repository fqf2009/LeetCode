# You are given an integer num. You can swap two digits at most once to
# get the maximum valued number.
# Return the maximum valued number you can get.
# Constraints:
#   0 <= num <= 10^8


# Math + Greedy
# Analysis
# - scan through digits backwards, to calculate for every position,
#   max_value (digit) and pos_of_max_value of all digits from that pos
#   until the end of string. If there is tie, use the largest pos.
# - e.g. , e.g.  num       9  7  5  5  6  7  8  8  3
#                max_val   9  8  8  8  8  8  8  8  3
#                max_pos   0  7  7  7  7  7  7  7  8
# - then find first place: num[i] < max_val[i], here:
#           num[1] < max_val[1], i.e. 7 < 8;
# - so we swap num[1] with num[max_pos[1]], i.e. swap num[1] with num[7],
#   and we get: 9 8 5 5 6 7 8 7 3
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        max_val = [digits[-1]] * n
        max_pos = [n-1] * n
        for i in reversed(range(n-1)):
            if digits[i] > max_val[i+1]:
                max_val[i] = digits[i]
                max_pos[i] = i
            else:
                max_val[i] = max_val[i+1]
                max_pos[i] = max_pos[i+1]

        for i in range(n-1):
            if digits[i] < max_val[i]:
                digits[i], digits[max_pos[i]] = digits[max_pos[i]], digits[i]
                break   # only swap one time

        return int(''.join(digits))


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.maximumSwap(975567883)
        print(r)
        assert r ==985567873

        r = sol.maximumSwap(115)
        print(r)
        assert r == 511
        
        r = sol.maximumSwap(98368)
        print(r)
        assert r == 98863

        r = sol.maximumSwap(2736)
        print(r)
        assert r == 7236

        r = sol.maximumSwap(9973)
        print(r)
        assert r == 9973

    unit_test(Solution())
