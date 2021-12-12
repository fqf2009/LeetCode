class Solution:
    # LeetCode 168
    # Given an integer columnNumber, return its corresponding column
    # title as it appears in an Excel sheet.
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber
        res = []
        while c > 0:
            c, r = divmod(c - 1, 26)
            res.append(chr(ord('A') + r))
            
        return ''.join(reversed(res))

    # LeetCode 171
    # Given a string columnTitle that represents the column title as 
    # appear in an Excel sheet, return its corresponding column number.
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            res = res * 26 + ord(ch) - ord('A') + 1
        
        return res


if __name__ == "__main__":
    r = Solution().convertToTitle(1)
    print(r)
    assert(r == 'A')

    r = Solution().convertToTitle(28)
    print(r)
    assert(r == 'AB')

    r = Solution().convertToTitle(701)
    print(r)
    assert(r == 'ZY')

    r = Solution().convertToTitle(2147483647)
    print(r)
    assert(r == 'FXSHRXW')

    r = Solution().titleToNumber('A')
    print(r)
    assert(r == 1)

    r = Solution().titleToNumber('AB')
    print(r)
    assert(r == 28)

    r = Solution().titleToNumber('ZY')
    print(r)
    assert(r == 701)

    r = Solution().titleToNumber('FXSHRXW')
    print(r)
    assert(r == 2147483647)
