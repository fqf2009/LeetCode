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
# Since the answer may be very large, return it modulo 10^9 + 7.
#
# Constraints:
#   1 <= pressedKeys.length <= 10^5
#   pressedKeys only consists of digits from '2' - '9'.
from itertools import chain


# DP (fibonacci in disguise) - T/S: O(N), O(N)
# - memo or cache to reduce calculation
class Solution1:
    def countTexts(self, pressedKeys: str) -> int:
        n, res, modulo = len(pressedKeys), 1, 10**9+7
        dp = [[0] * (n+4) for _ in range(2)]
        dp[0][0], dp[1][0] = 1, 1
        hwm = [0, 0]        # high water mark of dp
        ch0 = pressedKeys[0]
        cnt = 1
        for ch in chain(pressedKeys[1:], '1'):
            if ch0 == ch:
                cnt += 1
            else:
                if ch0 in ('7', '9'):
                    steps = 4
                    idx = 1
                else:
                    steps = 3
                    idx = 0

                for i in range(hwm[idx], cnt):
                    for j in range(1, steps+1):
                        # % is important to avoid huge number and improve performance
                        dp[idx][i+j] = (dp[idx][i+j] + dp[idx][i]) % modulo
                res = res * dp[idx][cnt] % modulo
                hwm[idx] = max(hwm[idx], cnt)
                cnt = 1
                ch0 = ch

        return res


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
        r = sol.countTexts("344644887777599999")
        print(r)
        assert r == 960

        r = sol.countTexts("344644885")
        print(r)
        assert r == 8

        r = sol.countTexts("22233")
        print(r)
        assert r == 8

        r = sol.countTexts("222222222222222222222222222222222222")
        print(r)
        assert r == 82876089

        r = sol.countTexts("444444444444444444444444444444448888888888888888999999999999333333333333333366666666666666662222222222222222666666666666666633333333333333338888888888888888222222222222222244444444444444448888888888888222222222222222288888888888889999999999999999333333333444444664")
        print(r)
        assert r == 537551452

        r = sol.countTexts("88888888888888888888888888888999999999999999999999999999994444444444444444444444444444488888888888888888888888888888555555555555555555555555555556666666666666666666666666666666666666666666666666666666666222222222222222222222222222226666666666666666666666666666699999999999999999999999999999888888888888888888888888888885555555555555555555555555555577777777777777777777777777777444444444444444444444444444444444444444444444444444444444433333333333333333333333333333555555555555555555555555555556666666666666666666666666666644444444444444444444444444444999999999999999999999999999996666666666666666666666666666655555555555555555555555555555444444444444444444444444444448888888888888888888888888888855555555555555555555555555555555555555555555555555555555555555555555555555555555555999999999999999555555555555555555555555555554444444444444444444444444444444555")
        print(r)
        assert r == 886136986

    # unit_test(Solution())
    unit_test(Solution1())
