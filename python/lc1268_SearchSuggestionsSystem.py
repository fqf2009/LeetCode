# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products
# after each character of searchWord is typed. Suggested products should
# have common prefix with searchWord. If there are more than three products
# with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of
# searchWord is typed.
# Constraints:
#   1 <= products.length <= 1000
#   1 <= products[i].length <= 3000
#   1 <= sum(products[i].length) <= 2 * 10^4
#   All the strings of products are unique.
#   products[i] consists of lowercase English letters.
#   1 <= searchWord.length <= 1000
#   searchWord consists of lowercase English letters.
from typing import List
import bisect

# Trie + DFS
# Time: O(n*L), where L is average length of product name.
# Space: O(N), N is nodes in trie. it depends on how frequent of common prefix.


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        suggestion = []
        res = []

        def getSuggestion(startNode, prefix):
            if '*' in startNode:
                suggestion.append(prefix)
                if len(suggestion) == 3:
                    return
            for ch in sorted(startNode.keys()): # sort over and over is a waste of time
                if ch != '*':
                    node = startNode[ch]
                    getSuggestion(node, prefix + ch)
                    if len(suggestion) == 3:
                        return

        for p in products:
            node = trie
            for ch in p:
                node = node.setdefault(ch, dict())
            node.setdefault('*', None)

        node = trie
        for i, ch in enumerate(searchWord):
            if ch in node:
                node = node[ch]
                suggestion.clear()
                getSuggestion(node, searchWord[:i+1])
                res.append(suggestion.copy())
            else:
                res.extend([[]] * (len(searchWord) - i))
                break

        return res


# Binary Search: T/S: O(n*log(n) + L*log(n)), O(1)
class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        leftPos = 0
        rightPos = bisect.bisect_right(products, searchWord)
        res = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            leftPos = bisect.bisect_left(products, prefix, leftPos, rightPos)
            suggestion = []
            for j in range(leftPos, leftPos + 3):
                if j < len(products) and products[j].startswith(prefix):
                    suggestion.append(products[j])
            res.append(suggestion)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], 'mouse')
        print(r)
        assert r == [["mobile", "moneypot", "monitor"],
                     ["mobile", "moneypot", "monitor"],
                     ["mouse", "mousepad"],
                     ["mouse", "mousepad"],
                     ["mouse", "mousepad"]]

        r = sol.suggestedProducts(["havana"], "havana")
        print(r)
        assert r == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]

        r = sol.suggestedProducts(["havana"], "tatiana")
        print(r)
        assert r == [[], [], [], [], [], [], []]

        r = sol.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bags")
        print(r)
        assert r == [["baggage", "bags", "banner"],
                     ["baggage", "bags", "banner"],
                     ["baggage", "bags"], ["bags"]]

    unitTest(Solution())
    unitTest(Solution1())
