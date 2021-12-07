from collections import Counter

# Given a string s containing an out-of-order English representation of 
# digits 0-9, return the digits in ascending order.

# A Counter is a dict subclass for counting hashable objects. It is a collection where 
# elements are stored as dictionary keys and their counts are stored as dictionary 
# values. The Counter class is similar to bags or multisets in other languages.

class Solution:
    def originalDigits(self, s: str) -> str:
        digits = [  ('z', '0', 'zero'),
                    ('w', '2', 'two'),
                    ('u', '4', 'four'),
                    ('o', '1', 'one'),
                    ('f', '5', 'five'),
                    ('x', '6', 'six'),
                    ('r', '3', 'three'),
                    ('s', '7', 'seven'),
                    ('g', '8', 'eight'),
                    ('i', '9', 'nine') ]

        freq = Counter(s)
        res = ''
        for i in range(len(digits)):
            res += digits[i][1] * freq[digits[i][0]]
            freq = freq - Counter(digits[i][2] * freq[digits[i][0]])

        return ''.join(sorted(res))


if __name__ == "__main__":
    r = Solution().originalDigits('owoztneoer')
    print(r)
    assert(r == '012')

    r = Solution().originalDigits('fviefuro')
    print(r)
    assert(r == '45')
