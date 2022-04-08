# You are given a character array keys containing unique characters and a 
# string array values containing strings of length 2. You are also given 
# another string array dictionary that contains all permitted original 
# strings after decryption. You should implement a data structure that can 
# encrypt or decrypt a 0-indexed string.
# A string is encrypted with the following process:
# - For each character c in the string, we find the index i satisfying
#   keys[i] == c in keys.
# - Replace c with values[i] in the string.
# A string is decrypted with the following process:
# - For each substring s of length 2 occurring at an even index in the 
#   string, we find an i such that values[i] == s. If there are multiple
#   valid i, we choose any one of them. This means a string could have 
#   multiple possible strings it can decrypt to.
# - Replace s with keys[i] in the string.
# Implement the Encrypter class:
# - Encrypter(char[] keys, String[] values, String[] dictionary) 
#   Initializes the Encrypter class with keys, values, and dictionary.
# - String encrypt(String word1) Encrypts word1 with the encryption process 
#   described above and returns the encrypted string.
# - int decrypt(String word2) Returns the number of possible strings word2 
#   could decrypt to that also appear in dictionary.
#
# Constraints:
#   1 <= keys.length == values.length <= 26
#   values[i].length == 2
#   1 <= dictionary.length <= 100
#   1 <= dictionary[i].length <= 100
#   All keys[i] and dictionary[i] are unique.
#   1 <= word1.length <= 2000
#   1 <= word2.length <= 200
#   All word1[i] appear in keys.
#   word2.length is even.
#   keys, values[i], dictionary[i], word1, and word2 only contain lowercase English letters.
#   At most 200 calls will be made to encrypt and decrypt in total.
from typing import List
from collections import Counter

# HashMap - decrypt: O(1)
# - This brilliant solution comes from lee215:
# https://leetcode.com/problems/encrypt-and-decrypt-strings/discuss/1909025/JavaC%2B%2BPython-Two-Hashmaps-with-Explanation
class Encrypter1(object):

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {k: v for k,v in zip(keys, values)}
        self.decrypt = Counter(self.encrypt(w) for w in dictionary).__getitem__

    def encrypt(self, word1):
        return ''.join(self.enc[c] for c in word1)


# Trie
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encoding = {k: v for k, v in zip(keys, values)}
        self.decoding = {}
        for k, v in self.encoding.items():
            self.decoding.setdefault(v, list()).append(k)
        self.trie = {}
        for word in dictionary:
            branch = self.trie
            for ch in word:
                branch = branch.setdefault(ch, dict())
            branch['*'] = True      # mark a word

    def encrypt(self, word1: str) -> str:
        res = []
        for ch in word1:
            res.append(self.encoding[ch])
        return ''.join(res)

    def decrypt(self, word2: str) -> int:
        def dfs_decrypt(branch: dict, word: str) -> int:
            if len(word) == 0:
                return 1 if '*' in branch else 0
            res = 0
            if word[:2] in self.decoding:
                for ch in self.decoding[word[:2]]:
                    if ch in branch:
                        res += dfs_decrypt(branch[ch], word[2:])
            return res
        
        return dfs_decrypt(self.trie, word2)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

if __name__ == '__main__':
    def unitTest():
        inputs = [["Encrypter", "encrypt", "decrypt"],
                  [[['a', 'b', 'c', 'd'], 
                    ["ei", "zf", "ei", "am"], 
                    ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], 
                  ["abcd"], ["eizfeiam"]]]
        expected = [None,"eizfeiam", 2]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0]) # obj = Encrypter(keys, values, dictionary)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i]) # obj.encrypt(word1) or obj.decrypt(word2)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["Encrypter","decrypt","decrypt","decrypt","decrypt","decrypt","decrypt"],
                  [[["a","b","c","z"],
                    ["aa","bb","cc","zz"], 
                    ["aa","aaa","aaaa","aaaaa","aaaaaaa"]],
                  ["aaaa"],["aa"],["aaaa"],["aaaaaaaa"],["aaaaaaaaaaaaaa"],
                  ["aefagafvabfgshdthn"]]]
        expected = [None, 1, 0, 1, 1, 1, 0]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0]) # obj = Encrypter(keys, values, dictionary)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i]) # obj.encrypt(word1) or obj.decrypt(word2)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
