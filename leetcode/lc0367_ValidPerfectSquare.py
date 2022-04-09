# Given a positive integer num, write a function which returns True
# if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
# Constraints:
#   1 <= num <= 2^31 - 1


# Binary Search (Template 1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        i, j = 1, num // 2
        while i <= j:
            k = (i+j) // 2
            v = k*k
            if v == num:
                return True
            elif v < num:
                i = k + 1
            else:
                j = k - 1
            
        return False
        