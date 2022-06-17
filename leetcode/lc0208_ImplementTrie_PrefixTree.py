# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are various
# applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
#  - Trie() Initializes the trie object.
#  - void insert(String word) Inserts the string word into the trie.
#  - boolean search(String word) Returns true if the string word is in the
#    trie (i.e., was inserted before), and false otherwise.
#  - boolean startsWith(String prefix) Returns true if there is a previously
#    inserted string word that has the prefix prefix, and false otherwise.
# Constraints:
#   1 <= word.length, prefix.length <= 2000
#   word and prefix consist only of lowercase English letters.
#   At most 3 * 104 calls in total will be made to insert, search, and startsWith.
from typing import List, Optional


# Trie (Prefix Tree)
# - iteration instead of recursion
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        branch = self.root
        for ch in word:
            branch = branch.setdefault(ch, dict())
        branch.setdefault('*', 0)
        branch['*'] += 1

    def search(self, word: str) -> bool:
        branch = self.root
        for ch in word:
            if ch not in branch: return False
            branch = branch[ch]
        return '*' in branch

    def startsWith(self, prefix: str) -> bool:
        branch = self.root
        for ch in prefix:
            # if ch not in branch: return False
            # branch = branch[ch]
            branch = branch.get(ch)
            if not branch: return False
        return True


# Trie (Prefix Tree)
class Trie1:
    def __init__(self):
        self.branch = {}
        self.count = 0

    def insert(self, word: str) -> None:
        if word:
            self.branch.setdefault(word[0], Trie()).insert(word[1:])
        else:
            self.count += 1

    def search(self, word: str) -> bool:
        if not word: return self.count > 0
        return word[0] in self.branch and self.branch[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        return (not prefix or (prefix[0] in self.branch and
                                self.branch[prefix[0]].startsWith(prefix[1:])))


# Trie (Prefix Tree)
# - use list instead of dict
class Trie2:
    def __init__(self):
        self.branch: List[Optional[Trie]] = [None] * 26
        self.count = 0

    def insert(self, word: str) -> None:
        if word:
            i = ord(word[0]) - ord('a')
            if not self.branch[i]:
                self.branch[i] = Trie()
            self.branch[i].insert(word[1:]) #type:ignore
        else:
            self.count += 1

    def search(self, word: str) -> bool:
        if not word: return self.count > 0
        i = ord(word[0]) - ord('a')
        return self.branch[i] and self.branch[i].search(word[1:]) #type:ignore

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        i = ord(prefix[0]) - ord('a')
        return self.branch[i] and self.branch[i].startsWith(prefix[1:]) #type:ignore


if __name__ == '__main__':
    def unitTest():
        inputs = [["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                  [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]]
        expected = [None, None, True, False, True, None, True]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
