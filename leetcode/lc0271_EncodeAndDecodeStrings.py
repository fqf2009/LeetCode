# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded
# back to the original list of strings.
# Constraints:
#   1 <= strs.length <= 200
#   0 <= strs[i].length <= 200
#   strs[i] contains any possible characters out of 256 valid ASCII characters.
from quopri import encodestring
from typing import List


# use CSV format, optionally quoted with '"'
# - seperator is ','
# - if a string has ',', quoted it with '"'
# - if a string has '"' or '\', use \" and \\ to express them.
class Codec:
    def encodeString(self, s: str) -> str:
        if len(s) == 0:
            return '""'
        elif '"' in s or "\\" in s or "," in s:
            return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
        else:
            return s

    def encode(self, strs: List[str]) -> str:
        return ",".join(self.encodeString(s) for s in strs)

    def decodeString(self, s: str) -> str:
        if len(s) == 0 or s[0] != '"':
            return s
        else:
            return s[1:-1].replace('\\"', '"').replace("\\\\", "\\")

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            r = l + 1
            if s[l] == '"':
                while r < len(s) and s[r] != '"':
                    if s[r] == "\\":
                        r += 2
                    else:
                        r += 1
                res.append(self.decodeString(s[l : r + 1]))
                r += 2  # skip '"' and ','
            else:
                while r < len(s) and s[r] != ",":
                    r += 1
                res.append(s[l:r])
                r += 1  # skip ','

            l = r

        return res


# encode string as: "4_bytes_int_length" + string
class Codec1:
    def encodeString(self, s: str) -> str:
        n = len(s)
        return "".join(chr(n >> (i * 8) & 0xFF) for i in range(4)) + s

    def decodeLength(self, s: str) -> int:
        return sum(ord(s[i]) * (256**i) for i in range(4))

    def encode(self, strs: List[str]) -> str:
        return "".join(self.encodeString(x) for x in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i, n = 0, len(s)
        while i < n:
            strLen = self.decodeLength(s[i : i + 4])
            i += 4
            res.append(s[i : i + strLen])
            i += strLen
        return res


if __name__ == "__main__":

    def unit_test(sol):
        input = ["Hello", "World"]
        output1 = sol.encode(input)
        print(output1)
        output2 = sol.decode(output1)
        print(output2)
        assert output2 == input

        input = ["He,llo", '"World\\']
        output1 = sol.encode(input)
        print(output1)
        output2 = sol.decode(output1)
        print(output2)
        assert output2 == input

        input = [""]
        output1 = sol.encode(input)
        print(output1)
        output2 = sol.decode(output1)
        print(output2)
        assert output2 == input

        input = ["", ""]
        output1 = sol.encode(input)
        print(output1)
        output2 = sol.decode(output1)
        print(output2)
        assert output2 == input

    unit_test(Codec())
    unit_test(Codec1())
