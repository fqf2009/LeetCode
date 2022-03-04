# Design a search autocomplete system for a search engine. Users may input a
# sentence (at least one word and end with a special character '#').
# You are given a string array sentences and an integer array times both of
# length n where sentences[i] is a previously typed sentence and times[i] is
# the corresponding number of times the sentence was typed. For each input
# character except '#', return the top 3 historical hot sentences that have
# the same prefix as the part of the sentence already typed.
# Here are the specific rules:
#  - The hot degree for a sentence is defined as the number of times a user
#    typed the exactly same sentence before.
#  - The returned top 3 hot sentences should be sorted by hot degree (The
#    first is the hottest one). If several sentences have the same hot degree,
#    use ASCII-code order (smaller one appears first).
#  - If less than 3 hot sentences exist, return as many as you can.
#  - When the input is a special character, it means the sentence ends, and in
#    this case, you need to return an empty list.
# Implement the AutocompleteSystem class:
#  - AutocompleteSystem(String[] sentences, int[] times) Initializes the object
#    with the sentences and times arrays.
#  - List<String> input(char c) This indicates that the user typed character c.
#    - Returns an empty array [] if c == '#' and stores the inputted sentence in
#      the system.
#    - Returns the top 3 historical hot sentences that have the same prefix as
#      the part of the sentence already typed. If there are fewer than 3 matches,
#      return them all.
# Constraints:
#   n == sentences.length
#   n == times.length
#   1 <= n <= 100
#   1 <= sentences[i].length <= 100
#   1 <= times[i] <= 50
#   c is a lowercase English letter, a hash '#', or space ' '.
#   Each tested sentence will be a sequence of characters c that end with the character '#'.
#   Each tested sentence will have a length in the range [1, 200].
#   The words in each input sentence are separated by single spaces.
#   At most 5000 calls will be made to input.
from collections import defaultdict
from typing import List
import heapq


# Trie
# - for init, T/S: O(n*k), O(n*k), where k is average length of sentences.
# - for each input and suggestion, Time:
#   minimum: O(k),     - input length k is very long, only a few  or no suggestion
#   maximum: O(n*k/26) - if only input 1 char, but there are large amount of existing inputs
class suggestion:
    def __init__(self, freq: int, sentense: str):
        self.freq = freq
        self.sentence = sentense

    def __eq__(self, next):
        return self.freq == next.freq and self.sentence == next.sentence

    def __lt__(self, next):
        return self.freq < next.freq or (self.freq == next.freq and self.sentence > next.sentence)


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.freq = 0

    def addSentence(self, s: str, times: int):
        if len(s) > 0:
            self.children[s[0]].addSentence(s[1:], times)
        else:
            self.freq += times

    def collectSuggestion(self, inputs: str, prefix: str, suggestions: List):
        if len(inputs) > 0:
            if inputs[0] in self.children:
                self.children[inputs[0]].collectSuggestion(inputs[1:], prefix + inputs[0], suggestions)
            else:
                suggestions.clear()
        else:
            if self.freq > 0:
                heapq.heappush(suggestions, suggestion(self.freq, prefix))
                if len(suggestions) > 3:
                    heapq.heappop(suggestions)
            for ch, node in self.children.items():
                node.collectSuggestion('', prefix + ch, suggestions)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.inputs = ''
        for s, t in zip(sentences, times):
            self.root.addSentence(s, t)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.root.addSentence(self.inputs, 1)
            self.inputs = ''
            return []

        suggestions = []
        self.inputs += c
        self.root.collectSuggestion(self.inputs, '', suggestions)
        res = []
        while suggestions:
            res.append(heapq.heappop(suggestions).sentence)

        return res[::-1]


if __name__ == '__main__':
    def unitTest():
        inputs = [["AutocompleteSystem", "input", "input", "input", "input"],
                  [[["i love you", "island", "iroman", "i love leetcode"],
                    [5, 3, 2, 2]
                    ],
                   ["i"], [" "], ["a"], ["#"]
                   ]
                  ]
        expected = [None, ["i love you", "island", "i love leetcode"],
                    ["i love you", "i love leetcode"], [], []]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = AutocompleteSystem(sentences, times)
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.input(c)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["AutocompleteSystem", "input", "input", "input", "input", "input", "input",
                   "input", "input", "input", "input", "input", "input", "input", "input"],
                  [[["abc", "abbc", "a"], [3, 3, 3]],
                   ["b"], ["c"], ["#"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"], 
                   ["#"], ["a"], ["b"], ["c"], ["#"]
                  ]
                 ]
        expected = [None, [], [], [], ["bc"], ["bc"], [], ["a", "abbc", "abc"], ["abbc", "abc"],
                    ["abc"], [], ["abc", "a", "abbc"], ["abc", "abbc"], ["abc"], []]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
