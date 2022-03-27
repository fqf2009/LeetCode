# Given an integer array queries and a positive integer intLength, return 
# an array answer where answer[i] is either the queries[i]th smallest 
# positive palindrome of length intLength or -1 if no such palindrome exists.
# A palindrome is a number that reads the same backwards and forwards. 
# Palindromes cannot have leading zeros.
# Constraints:
#   1 <= queries.length <= 5 * 10^4
#   1 <= queries[i] <= 10^9
#   1 <= intLength <= 15
from typing import List


# Only need to count the first half of palindrome due to symmetric nature.
# - Note that only positive palindrome is needed, otherwise for length 1,
#   there are 10 palindromes (0 - 9).
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        leftLen = (intLength + 1) // 2
        rightLen = intLength - leftLen
        start = 10 ** (leftLen - 1)
        nPalindrome = start * 9
        res = [-1] * len(queries)
        for i, idx in enumerate(queries):
            if idx <= nPalindrome:
                leftPal = str(start + idx - 1)
                rightPal = leftPal[:rightLen][::-1]
                res[i] = int(leftPal + rightPal)

        return res
        

from typing import List
if __name__ == '__main__':
    def unitTest(sol):
        r = sol.kthPalindrome([2,201429812,8,520498110,492711727,
        339882032,462074369,9,7,6],1)
        print(r)
        assert r == [2,-1,8,-1,-1,-1,-1,9,7,6]

        r = sol.kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3)
        print(r)
        assert r == [101,111,121,131,141,999]

        r = sol.kthPalindrome(queries = [2,4,6], intLength = 4)
        print(r)
        assert r ==  [1111,1331,1551]

        r = sol.kthPalindrome(queries = [2,4,6,10], intLength = 1)
        print(r)
        assert r ==  [2,4,6,-1]

    unitTest(Solution())
