# Alice is texting Bob using her phone. The mapping of digits to letters
# is shown in the figure below.
# In order to add a letter, Alice has to press the key of the corresponding
# digit i times, where i is the position of the letter in the key.
#  - For example, to add the letter 's', Alice has to press '7' four times. 
#    Similarly, to add the letter 'k', Alice has to press '5' twice.
#  - Note that the digits '0' and '1' do not map to any letters, so Alice 
#    does not use them.
# However, due to an error in transmission, Bob did not receive Alice's 
# text message but received a string of pressed keys instead.
#  - For example, when Alice sent the message "bob", Bob received 
#    the string "2266622".
# Given a string pressedKeys representing the string received
# by Bob, return the total number of possible text messages
# Alice could have sent.
# Since the answer may be very large, return it modulo 109 + 7.
#
# Constraints:
#   1 <= pressedKeys.length <= 10^5
#   pressedKeys only consists of digits from '2' - '9'.
from itertools import chain


# DP (fibonacci in disguise) - T/S: O(N), O(N)
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        res = 1
        modulo = 10**9+7
        ch0 = pressedKeys[0]
        cnt = 1
        for ch in chain(pressedKeys[1:], '1'):
            if ch0 == ch:
                cnt += 1
            else:
                comb = [0] * (cnt + 4)
                comb[0] = 1
                steps = 4 if ch0 in ('7', '9') else 3
                for i in range(cnt):
                    for j in range(1, steps+1):
                        comb[i+j] += comb[i]
                res = res * comb[cnt] % modulo
                cnt = 1
                ch0 = ch

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.countTexts("22233")
        print(r)
        assert r == 8

        r = sol.countTexts("222222222222222222222222222222222222")
        print(r)
        assert r == 82876089 # 2082876103 

    unit_test(Solution())
