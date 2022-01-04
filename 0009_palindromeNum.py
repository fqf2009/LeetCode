# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revert = 0
        y = x
        while y > 0:
            y, r = divmod(y, 10)
            revert = revert * 10 + r

        return revert == x


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                return False
            
        return True


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.isPalindrome(121)
        print(r)
        assert(r == True)

        r = sol.isPalindrome(0)
        print(r)
        assert(r == True)

        r = sol.isPalindrome(-121)
        print(r)
        assert(r == False)

        r = sol.isPalindrome(10)
        print(r)
        assert(r == False)

    unitTest(Solution())
    unitTest(Solution1())