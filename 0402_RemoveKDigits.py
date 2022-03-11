# Given string num representing a non-negative integer num, 
# and an integer k, return the smallest possible integer 
# after removing k digits from num.
# Constraints:
#   1 <= k <= num.length <= 10^5
#   num consists of only digits.
#   num does not have any leading zeros except for the zero itself.


# Stack (Monotonic Stack)
# - iterate over digits, if keep increasing or the same as previous,
#   push into stack, if descreasing, pop up from stack and remove it
# - be careful about cleanup:
#       - remaining digits not iterated
#       - iteration is done, but not enough digits get removed
#       - leading 0s
#       - for empty result, set to '0'
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        i =  0
        n = len(num)
        while i < n and k > 0:
            if len(stk) == 0 or num[i] >= stk[-1]:
                stk.append(num[i])
                i += 1
            else:
                stk.pop()
                k -= 1

        if i < n:
            stk.append(num[i:])
        elif k > 0:
            del stk[-k:]

        res = str.lstrip(''.join(stk), '0')
        if len(res) == 0:
            res = '0'

        return res

        
if __name__ == '__main__':
    def unitTest(sol):
        r = sol.removeKdigits(num = "1432219", k = 3)
        print(r)
        assert r == '1219'

        r = sol.removeKdigits(num = "10200", k = 1)
        print(r)
        assert r == '200'

        r = sol.removeKdigits(num = "10", k = 2)
        print(r)
        assert r == '0'

    unitTest(Solution())
