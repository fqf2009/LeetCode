# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads 
# the same forward and backward. Alphanumeric characters include letters 
# and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Constraints:
#   1 <= s.length <= 2 * 10^5
#   s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            ch1 = s[i].lower()
            ch2 = s[j].lower()
            if not ch1.isalnum():
                i += 1
            elif not ch2.isalnum():
                j -= 1
            elif ch1 != ch2:
                return False
            else:
                i += 1
                j -= 1                

        return True


# Two Pointers
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            ch1 = s[i].lower()
            ch2 = s[j].lower()
            if not ch1.isalnum():
                i += 1
                continue
            if not ch2.isalnum():
                j -= 1
                continue
            if ch1 != ch2:
                return False
            i += 1
            j -= 1                

        return True


if __name__ == "__main__":
    def unit_test(sol):
        r = Solution().isPalindrome('A man, a plan, a canal: Panama')
        print(r)
        assert r == True

        r = Solution().isPalindrome('race a car')
        print(r)
        assert r == False

        r = Solution().isPalindrome(' ')
        print(r)
        assert r == True

    unit_test(Solution())
    unit_test(Solution1())
