# Design a data structure that supports adding new words and finding
# if a string matches any previously added string.

# Implement the WordDictionary class:
#  - WordDictionary() Initializes the object.
#  - void addWord(word) Adds word to the data structure, it can be matched later.
#  - bool search(word) Returns true if there is any string in the data structure 
#    that matches word or false otherwise. word may contain dots '.' where dots 
#    can be matched with any letter.

# Use Trie, or prefix search tree
# https://en.wikipedia.org/wiki/Trie
# Insert, Search - time complexity O(1)
class WordDictionary:
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
                    self.branch[s[0]] = WordDictionary.Node()
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
        self.trie = WordDictionary.Node()

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
