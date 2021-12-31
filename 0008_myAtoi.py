# Implement the myAtoi(string s) function, which converts a string to a 32-bit 
# signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# - Read in and ignore any leading whitespace.
# - Check if the next character (if not already at the end of the string) is '-' or '+'. 
#   Read this character in if it is either. This determines if the final result is negative 
#   or positive respectively. Assume the result is positive if neither is present.
# - Read in next the characters until the next non-digit character or the end of the input 
#   is reached. The rest of the string is ignored.
# - Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were 
#   read, then the integer is 0. Change the sign as necessary (from step 2).
# - If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the 
#   integer so that it remains in the range. Specifically, integers less than -231 should be 
#   clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# - Only the space character ' ' is considered a whitespace character.
# - Do not ignore any characters other than the leading whitespace or the rest of the 
#   string after the digits.

# Just for logic control practice:
# - checkLeadingSpace: check many times until there is no leading space
# - checkLeadingSign:  check only once, after checking leading space
# - after previous check, break once there is a non-digit 
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        checkLeadingSpace = True
        checkLeadingSign = True
        sign = 1
        for ch in s:
            if checkLeadingSpace:
                if ch == ' ':
                    continue
                checkLeadingSpace = False
            
            if checkLeadingSign:
                checkLeadingSign = False
                if ch == '+':
                    continue
                if ch == '-':
                    sign = -1
                    continue
            
            if ch >= '0' and ch <= '9':
                res = res * 10 + ord(ch) - ord('0')
            else:
                break
        
        res = res * sign
        if res < -(2**31):
            return -(2**31)
        if res > 2**31 - 1:
            return 2**31 - 1
        return res


if __name__ == '__main__':
    sol = Solution()

    n = sol.myAtoi("00000-42a1234")
    print(n)
    assert(n == 0)

    n = sol.myAtoi('42')
    print(n)
    assert(n == 42)

    n = sol.myAtoi(' + 42')
    print(n)
    assert(n == 0)

    n = sol.myAtoi('   -42')
    print(n)
    assert(n == -42)

    n = sol.myAtoi('4193 with words')
    print(n)
    assert(n == 4193)

    n = sol.myAtoi('words and 987')
    print(n)
    assert(n == 0)

    n = sol.myAtoi(' +2147483648')
    print(n)
    assert(n == 2147483647)

    n = sol.myAtoi(' -2147483648')
    print(n)
    assert(n == -2147483648)
