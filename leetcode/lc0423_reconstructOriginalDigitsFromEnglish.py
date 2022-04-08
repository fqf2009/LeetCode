# Given a string s containing an out-of-order English representation of 
# digits 0-9, return the digits in ascending order.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is one of the characters:
#       ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
#   s is guaranteed to be valid.
from collections import Counter


# Counter - T/S: O(n), O(n)
# - A Counter is a dict subclass for counting hashable objects. It is a collection  
#   where elements are stored as dictionary keys and their counts are stored as  
#   dictionary values. The Counter class is similar to bags or multisets in other
#   languages.
# - always choose an unique letter in the word of one remaining digit, but not in
#   the words of other remaining digits.
class Solution:
    def originalDigits(self, s: str) -> str:
        encoding = [ ('z', '0', 'zero'),
                     ('w', '2', 'two'),
                     ('u', '4', 'four'),
                     ('o', '1', 'one'),
                     ('f', '5', 'five'),
                     ('x', '6', 'six'),
                     ('r', '3', 'three'),
                     ('s', '7', 'seven'),
                     ('g', '8', 'eight'),
                     ('i', '9', 'nine') ]

        counter = Counter(s)
        res = []
        for ch, digit, word in encoding:
            res.extend([digit] * counter[ch])
            counter = counter - Counter(word * counter[ch])

        return ''.join(sorted(res))


if __name__ == "__main__":
    def unit_test(sol):
        r = sol.originalDigits('owoztneoer')
        print(r)
        assert r == '012'

        r = sol.originalDigits('fviefuro')
        print(r)
        assert r == '45'


    unit_test(Solution())
