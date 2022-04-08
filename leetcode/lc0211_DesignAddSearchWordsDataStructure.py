# Design a data structure that supports adding new words and finding
# if a string matches any previously added string.

# Implement the WordDictionary class:
#  - WordDictionary() Initializes the object.
#  - void addWord(word) Adds word to the data structure, it can be matched later.
#  - bool search(word) Returns true if there is any string in the data structure 
#    that matches word or false otherwise. word may contain dots '.' where dots 
#    can be matched with any letter.


# Trie (Prefix Tree)
# - Simplify code, no need to use two classes
# - '*' in dict to indicate word exists, also save word count
# - to reduce recursion depth, only '.' use recursion, non-wildcard use iteration
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        branch = self.root
        for ch in word:
            branch = branch.setdefault(ch, {})
        branch.setdefault('*', 0)
        branch['*'] += 1

    def search(self, word: str) -> bool:
        def exists(branch: dict, word: str) -> bool:
            for i, ch in enumerate(word):
                if ch == '.':
                    return any(exists(branch[ch1], word[i+1:]) for ch1 in branch.keys() if ch1 != '*')
                else:
                    if ch not in branch: return False
                branch = branch[ch]
            return '*' in branch and branch['*'] > 0

        return exists(self.root, word)


# Use Trie, or prefix search tree
# https://en.wikipedia.org/wiki/Trie
# Insert, Search - time complexity O(1)
class WordDictionary1:
    class Node:
        def __init__(self) -> None:
            self.branch = {}
            # count > 0, it is a word node, otherwise it is prefix node
            self.count = 0

        def add(self, s: str) -> None:
            if len(s) == 0:
                self.count += 1
            else:
                if s[0] not in self.branch:
                    self.branch[s[0]] = WordDictionary1.Node()
                self.branch[s[0]].add(s[1:])

        def search(self, word: str) -> bool:
            if len(word) == 0:
                return self.count > 0
            elif word[0] == '.':
                for node in self.branch.values():
                    if node.search(word[1:]):
                        return True
                return False
            else:
                if word[0] in self.branch:
                    return self.branch[word[0]].search(word[1:])
                else:
                    return False

    def __init__(self):
        self.trie = WordDictionary1.Node()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)
            

if __name__ == '__main__':
    def unitTest(wd):
        inputs = [["addWord", "addWord", "addWord", "search", "search", "search", "search"],
                  [["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]]

        expected = [None, None, None, False, True, True, True]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(wd, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest(WordDictionary())
    unitTest(WordDictionary1())
