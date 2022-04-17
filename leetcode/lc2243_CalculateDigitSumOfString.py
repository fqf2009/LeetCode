# You are given a string s consisting of digits and an integer k.
# A round can be completed if the length of s is greater than k. 
# In one round, do the following:
#  - Divide s into consecutive groups of size k such that the first k 
#    characters are in the first group, the next k characters are in 
#    the second group, and so on. Note that the size of the last 
#    group can be smaller than k.
#  - Replace each group of s with a string representing the sum of all 
#    its digits. For example, "346" is replaced with "13" 
#    because 3 + 4 + 6 = 13.
#  - Merge consecutive groups together to form a new string. If the 
#    length of the string is greater than k, repeat from step 1.
# Return s after all rounds have been completed.
# Constraints:
#   1 <= s.length <= 100
#   2 <= k <= 100
#   s consists of digits only.


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = []
            for i in range(0, (len(s) + k - 1) // k):
                total = sum(int(ch) for ch in s[i*k: i*k + k])
                res.append(str(total))
            s = ''.join(res)

        return s


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.digitSum(s = "11111222223", k = 3)
        print(r)
        assert r == '135'

        r = sol.digitSum(s = "111112", k = 3)
        print(r)
        assert r == '34'

        r = sol.digitSum(s = "1111121", k = 3)
        print(r)
        assert r == '341'

        r = sol.digitSum(s = "111", k = 3)
        print(r)
        assert r == '111'

        r = sol.digitSum(s = "00000000", k = 3)
        print(r)
        assert r == "000"

    unit_test(Solution())
