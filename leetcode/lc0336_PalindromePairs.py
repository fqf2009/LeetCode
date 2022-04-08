# Given a list of unique words, return all the pairs of the distinct
# indices (i, j) in the given list, so that the concatenation of the
# two words words[i] + words[j] is a palindrome.

# Constraints:
#   1 <= words.length <= 5000
#   0 <= words[i].length <= 300
#   words[i] consists of lower-case English letters.
from typing import List
from collections import defaultdict


# Hash-Talbe (Dict)
# LeetCode - Memory Limit Exceeded
# - 136 / 136 test cases passed, but took too much memory.
# Analysis:
# - e.g. "banana" + "nab"  is palindrome,
#        "banana" + "b"    is palindrome,
#        "abcd"   + "dcba" is palindrome,
#   the rule is:
#   (prefix + palindrome_suffix) + (other_word (reverse_of_prefix))
#        "ban"   + "ana"   + "nab"
#        "b"     + "anana" + "b"
#        "abcd"  + ""      + "dcba"
# - Another scenario is: "sisyl" + "analysis", i.e.,
#                        "sisyl" + ("ana" + "lysis")
#   the rule is:
#   (other_word (reverse_of_suffix)) + (palindrome_prefix + suffix)
# - Build two hash-tables (dict): for all prefix (with palindrome
#   suffix) and suffix (with palindrome prefix), and then test the
#   reverse each word, see if it is in either of the hash-tables.
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        prefix, suffix = defaultdict(set), defaultdict(set)
        for i, w in enumerate(words):
            n = len(w)
            for j in range(n+1):
                if w[j:] == w[j:][::-1]:
                    prefix[w[:j]].add(i)
                if w[0:n-j] == w[0:n-j][::-1]:
                    suffix[w[n-j:]].add(i)

        res = set()
        for i, w in enumerate(words):
            w1 = w[::-1]
            for j in prefix[w1]:
                if i != j:
                    res.add((j, i))
            for j in suffix[w1]:
                if i != j:
                    res.add((i, j))

        return [list(x) for x in res]


# Trie - T/S: O(n*k^2), O(n*k), where k is average length of words
# LeetCode - 134 / 136 test cases passed, then: Time Limit Exceeded
# - the test case is 1.2 MB of all the repeated "aaa..bbb..aaa...bbb",
#   so rediculous!
class Solution1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = {}
        PREFIX_SHIFT = 10**8

        def addWord(word: str, idx):
            branch = trie
            for ch in word:
                branch = branch.setdefault(ch, {})
            branch.setdefault('*', set()).add(idx)

        for i, w in enumerate(words):
            n = len(w)
            for j in range(n+1):
                if w[j:] == w[j:][::-1]:
                    addWord(w[:j], i + PREFIX_SHIFT)
                if w[0:n-j] == w[0:n-j][::-1]:
                    addWord(w[n-j:], i)

        res = set()
        for i, w in enumerate(words):
            w1 = w[::-1]
            branch = trie
            for ch in w1:
                if ch not in branch:
                    break
                branch = branch[ch]
            else:
                if '*' not in branch: continue
                for j in branch['*']:
                    if j >= PREFIX_SHIFT:
                        k = j - PREFIX_SHIFT
                        if k != i:
                            res.add((k, i))
                    elif i != j:
                        res.add((i, j))
            
        return [list(x) for x in res]


# Solution from LeetCode web site:
class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []

class Solution2:
    def palindromePairs(self, words):

        # Create the Trie and add the reverses of all the words.
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1] # We want to insert the reverse.
            current_level = trie
            for j, c in enumerate(word):
                # Check if remainder of word is a palindrome.
                if word[j:] == word[j:][::-1]:# Is the word the same as its reverse?
                    current_level.palindrome_suffixes.append(i)
                # Move down the trie.
                current_level = current_level.next[c]
            current_level.ending_word = i

        # Look up each word in the Trie and find palindrome pairs.
        solutions = []
        for i, word in enumerate(words):
            current_level = trie
            for j, c in enumerate(word):
                # Check for case 3.
                if current_level.ending_word != -1:
                    if word[j:] == word[j:][::-1]: # Is the word the same as its reverse?
                        solutions.append([i, current_level.ending_word])
                if c not in current_level.next:
                    break
                current_level = current_level.next[c]
            else: # Case 1 and 2 only come up if whole word was iterated.
                # Check for case 1.
                if current_level.ending_word != -1 and current_level.ending_word != i:
                    solutions.append([i, current_level.ending_word])
                # Check for case 2.
                for j in current_level.palindrome_suffixes:
                    solutions.append([i, j])
        return solutions


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
        print(r)
        assert sorted(r) == sorted([[0, 1], [1, 0], [3, 2], [2, 4]])

        r = sol.palindromePairs(["bat", "tab", "cat"])
        print(r)
        assert sorted(r) == sorted([[0, 1], [1, 0]])

        r = sol.palindromePairs(words=["a", ""])
        print(r)
        assert sorted(r) == sorted([[0, 1], [1, 0]])

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
