# The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
# number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"


# y is pos (which line) for NEXT char, forward is direction for NEXT move
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        forward = True
        res = [''] * numRows
        y = 0
        for ch in s:
            res[y] = res[y] + str(ch)
            if forward:
                y += 1
            else:
                y -= 1
            if y == 0 or y == numRows - 1:
                forward = not forward

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
