# You are given a string s and an integer repeatLimit. Construct 
# a new string repeatLimitedString using the characters of s such 
# that no letter appears more than repeatLimit times in a row. 
# You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# Constraints:
#   1 <= repeatLimit <= s.length <= 105
#   s consists of lowercase English letters.
from collections import Counter


# Two Pointers
# - pointer i, largest lexical char to repeat repeatLimit times at most.
# - pointer j, second largest char to repeat 1 time.
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        letters = [list(x) for x in sorted(freq.items(), reverse=True)]
        # print(letters)
        res = ''
        i, j, n = 0, 0, len(letters)
        while True:
            while i < n and letters[i][1] == 0:
                i += 1
            if i >= n: break
            if len(res) == 0 or res[-1] != letters[i][0]:
                repeat = min(letters[i][1], repeatLimit)
                res += letters[i][0] * repeat   # type:ignore
                letters[i][1] -= repeat         # type:ignore
                if letters[i][1] == 0:
                    i += 1
                    continue

            if j <= i:
                j = i + 1
            while j < n and letters[j][1] == 0:
                j += 1
            if j >= n: break
            res += letters[j][0]       # type:ignore
            letters[j][1] -= 1         # type:ignore

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.repeatLimitedString("cczazcc", repeatLimit = 3)
        print(r)
        assert r == "zzcccac"

        r = sol.repeatLimitedString(s = "aababab", repeatLimit = 2)
        print(r)
        assert r == "bbabaa"
        
    unitTest(Solution())
