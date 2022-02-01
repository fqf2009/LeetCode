# The count-and-say sequence is a sequence of digit strings defined
# by the recursive formula:
#  - countAndSay(1) = "1"
#  - countAndSay(n) is the way you would "say" the digit string from 
#    countAndSay(n-1), which is then converted into a different digit string.
#  - To determine how you "say" a digit string, split it into the minimal number
#    of groups so that each group is a contiguous section all of the same character. 
#    Then for each group, say the number of characters, then say the character.
#  - To convert the saying into a digit string, replace the counts with a number 
#    and concatenate every saying.

# for example
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n-1):
            s = res
            res = ''
            ch0 = s[0]
            cnt = 1
            for ch1 in s[1:]:
                if ch1 == ch0:
                    cnt += 1
                else:
                    res = res + str(cnt) + ch0
                    ch0 = ch1
                    cnt = 1
            res = res + str(cnt) + ch0
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countAndSay(1)
        print(r)
        assert r == '1'

        r = sol.countAndSay(2)
        print(r)
        assert r == '11'

        r = sol.countAndSay(3)
        print(r)
        assert r == '21'

        r = sol.countAndSay(4)
        print(r)
        assert r == '1211'

        r = sol.countAndSay(5)
        print(r)
        assert r == '111221'

        r = sol.countAndSay(6)
        print(r)
        assert r == '312211'

        r = sol.countAndSay(7)
        print(r)
        assert r == '13112221'

        r = sol.countAndSay(30)
        print(r)

    unitTest(Solution())
