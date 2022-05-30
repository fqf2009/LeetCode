# A sentence is a string of single-space separated words where each word 
# can contain digits, lowercase letters, and the dollar sign '$'. A word 
# represents a price if it is a non-negative real number preceded by a 
# dollar sign.
# For example, "$100", "$23", and "$6.75" represent prices while "100", 
# "$", and "2$3" do not.
# You are given a string sentence representing a sentence and an integer 
# discount. For each word representing a price, apply a discount of 
# discount% on the price and update the word in the sentence. All updated 
# prices should be represented with exactly two decimal places.
# Return a string representing the modified sentence.
# Constraints:
#   1 <= sentence.length <= 10^5
#   sentence consists of lowercase English letters, digits, ' ', and '$'.
#   sentence does not have leading or trailing spaces.
#   All words in sentence are separated by a single space.
#   All prices will be positive integers without leading zeros.
#   All prices will have at most 10 digits.
#   0 <= discount <= 100
import re


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
            res = sentence.split()
            for i, s1 in enumerate(res):
                if s1.count("$") == 1 and s1[0] == '$' and len(s1) > 1:
                    s2 = s1[1:]
                    if not any(ch.isalpha() for ch in s2):
                        price = int(s2) * (100 - discount) / 100
                        res[i] = f'${price:.2f}'

            return " ".join(res)


# Regular Expression
class Solution1:
    def discountPrices(self, sentence: str, discount: int) -> str:
            res = sentence.split()
            pattern = re.compile(r"\$([0-9]+)$")
            for i, s1 in enumerate(res):
                match = pattern.match(s1)
                if match != None:
                    s2 = match.group(1)
                    res[i] = f'${int(s2) * (100 - discount) / 100:.2f}'

            return " ".join(res)


if __name__ == '__main__':
    def unit_discountPrices(sol):
        r = sol.discountPrices("there are $1 $2 and 5$ candies in the shop", 50)
        print(r)
        assert r == "there are $0.50 $1.00 and 5$ candies in the shop"

        r = sol.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100)
        print(r)
        assert r == "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"

        r = sol.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 0)
        print(r)
        assert r == "1 2 $3.00 4 $5.00 $6.00 7 8$ $9.00 $10$"

    unit_discountPrices(Solution())
    unit_discountPrices(Solution1())
