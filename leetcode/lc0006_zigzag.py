# The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
# number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given 
# a number of rows.
#
# Constraints:
#   1 <= s.length <= 1000
#   s consists of English letters (lower-case and upper-case), ',' and '.'.
#   1 <= numRows <= 1000

# flow control
# - y is pos (which line) for NEXT char
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = [''] * numRows
        y, direction = 0, 1
        for ch in s:
            res[y] += str(ch)
            y += direction
            if y == 0 or y == numRows - 1:
                direction *= -1

        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()

    r = sol.convert('PAYPALISHIRING', 3)
    print(r) 
    assert(r == 'PAHNAPLSIIGYIR')

    r = sol.convert('PAYPALISHIRING', 4)
    print(r)
    assert(r == 'PINALSIGYAHRPI')

    r = sol.convert('A', 1)
    print(r)
    assert(r == 'A')
    
    r = sol.convert('AB', 1)
    print(r)
    assert(r == 'AB')
