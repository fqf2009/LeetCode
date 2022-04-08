# Given a string num which represents an integer, return true if 
# num is a strobogrammatic number.
# A strobogrammatic number is a number that looks the same when 
# rotated 180 degrees (looked at upside down).
# Constraints:
#   1 <= num.length <= 50
#   num consists of only digits.
#   num does not contain any leading zeros except for zero itself.


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        for i in range((n+1) // 2):
            ch1, ch2 = num[i], num[n-1-i]
            if ch1+ch2 not in ('00', '11', '88', '69', '96'):
                return False

        return True


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.isStrobogrammatic("696")    # vs. "969"
        print(r)
        assert r == False

        r = sol.isStrobogrammatic("1801081")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("1801181")
        print(r)
        assert r == False

        r = sol.isStrobogrammatic("96096")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("88")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("69")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("008800")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("69")
        print(r)
        assert r == True

        r = sol.isStrobogrammatic("88")
        print(r)
        assert r == True

        r = (sol.isStrobogrammatic("2") or sol.isStrobogrammatic("3") or
             sol.isStrobogrammatic("4") or sol.isStrobogrammatic("5") or
             sol.isStrobogrammatic("6") or sol.isStrobogrammatic("7") or
             sol.isStrobogrammatic("9"))
        print(r)
        assert r == False

    unit_test(Solution())
