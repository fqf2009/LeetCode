# You are given the strings key and message, which represent a cipher key and a 
# secret message, respectively. The steps to decode message are as follows:
# Use the first appearance of all 26 lowercase English letters in key as the 
# order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one 
# instance of each letter in the alphabet), we have the partial substitution 
# table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.
# Constraints:
#   26 <= key.length <= 2000
#   key consists of lowercase English letters and ' '.
#   key contains every letter in the English alphabet ('a' to 'z') at least once.
#   1 <= message.length <= 2000
#   message consists of lowercase English letters and ' '.


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = [' '] * 26
        i = 0
        for ch in key:
            if ch != ' ':
                j = ord(ch) - ord('a')
                if cipher[j] == ' ':
                    cipher[j] = chr(ord('a') + i)
                    i += 1
                    if i == 26:
                        break
        
        res = []
        for ch in message:
            res.append(cipher[ord(ch) - ord('a')] if ch != ' ' else ch)

        return ''.join(res)


class Solution1:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {' ': ' '}
        i = 0
        for ch in key:
            if ch.isalpha() and ch not in decode:
                decode[ch] = chr(ord('a') + i)
                i += 1
                if i == 26: break

        return ''.join(decode[ch] for ch in message)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.decodeMessage("the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
        print(r)
        assert r == "this is a secret"

        r = sol.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
        print(r)
        assert r == "the five boxing wizards jump quickly"


    unit_test(Solution())
    unit_test(Solution1())
