# Convert a non-negative integer num to its English words representation.
# Example 1:
#   Input: num = 123
#   Output: "One Hundred Twenty Three"
# Example 2:
#   Input: num = 12345
#   Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#   Input: num = 1234567
#   Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Constraints:
#   0 <= num <= 2^31 - 1 (2147483647)

class Solution:
    def numberToWords(self, num: int) -> str:
        words20 = ['Zero', 'One', 'Two', 'Three', 'Four', 
                    'Five', 'Six', 'Seven', 'Eight', 'Nine',
                    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
                   ]
        wordsTens = ['Twenty', 'Thirty', 'Forty', 'Fifty',
                     'Sixty', 'Seventy', 'Eighty', 'Ninety']
        if num < 20:
            return words20[num]
        
        if num < 100:
            res = wordsTens[num//10 - 2] + (' ' + words20[num%10])
        elif num < 1000:
            res = words20[num//100] + ' Hundred ' + self.numberToWords(num%100)
        elif num < 1000000:
            res = self.numberToWords(num//1000) + ' Thousand ' + self.numberToWords(num%1000)
        elif num < 1000000000:
            res = self.numberToWords(num//1000000) + ' Million ' + self.numberToWords(num%1000000)
        else:
            res = self.numberToWords(num//1000000000) + ' Billion ' + self.numberToWords(num%1000000000)

        if res[-5:] == ' Zero':
            res = res[:-5]
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numberToWords(123)
        print(r)
        assert r == "One Hundred Twenty Three"

        r = sol.numberToWords(12345)
        print(r)
        assert r == "Twelve Thousand Three Hundred Forty Five"

        r = sol.numberToWords(1234567890)
        print(r)
        assert r == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty " \
                    "Seven Thousand Eight Hundred Ninety"

        r = sol.numberToWords(1234567891)
        print(r)
        assert r == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty " \
                    "Seven Thousand Eight Hundred Ninety One"

    unitTest(Solution())
