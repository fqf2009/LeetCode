# You are given an array of strings ideas that represents a list of 
# names to be used in the process of naming a company. The process 
# of naming a company is as follows:
#  - Choose 2 distinct names from ideas, call them ideaA and ideaB.
#  - Swap the first letters of ideaA and ideaB with each other.
#  - If both of the new names are not found in the original ideas, 
#    then the name ideaA ideaB (the concatenation of ideaA and ideaB, 
#    separated by a space) is a valid company name.
#  - Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.
# Example 1:
# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
#   - ("coffee", "donuts"): The company name created is "doffee conuts".
#   - ("donuts", "coffee"): The company name created is "conuts doffee".
#   - ("donuts", "time"): The company name created is "tonuts dime".
#   - ("donuts", "toffee"): The company name created is "tonuts doffee".
#   - ("time", "donuts"): The company name created is "dime tonuts".
#   - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.
# The following are some examples of invalid selections:
#   - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
#   - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
#   - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
# Constraints:
#   2 <= ideas.length <= 5 * 10^4
#   1 <= ideas[i].length <= 10
#   ideas[i] consists of lowercase English letters.
#   All the strings in ideas are unique.
from collections import defaultdict
from typing import List


# O(n)
# Analysis:
# - assume idea = initial_char + postfix
# - if initial are the same, just skip, don't count
# - If two ideas ideas[i] and ideas[j] share a common postfix,
#   then ideas[i] can not pair with any idea starts with ideas[j][0]
#   and ideas[j] can not pair with any idea starts with ideas[i][0].
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(set)
        for idea in ideas:
            group[idea[0]].add(hash(idea[1:]))
        res = 0
        for a, seta in group.items():
            for b, setb in group.items():
                if a < b:
                    same = len(seta & setb)
                    res += (len(seta) - same) * (len(setb) - same)

        return res * 2


# Initial thought, too complex, still has error
class Solution1:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        initial = defaultdict(int)
        postfix = defaultdict(set)
        for company in ideas:
            initial[company[0]] += 1
            postfix[company[1:]].add(company[0])

        res = n * (n - 1)
        for v in initial.values():
            res -= v * (v - 1)
        for t, ini in postfix.items():
            m = len(ini)
            res -= m * (m - 1)
            lst = list(ini)
            for ch1, ch2 in zip(lst, lst[1:]):
                k1 = initial[ch1]
                k2 = initial[ch2]
                res -= k1 * (k1 - 1)
                res -= k2 * (k2 - 1)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.distinctNames(["r", "lycdkjdnoy", "wzlu", "wxkyjgwc", "qtaqnbi", "m", "x", "jhvdzr", "rquzz"])
        print(r)
        assert r == 58

        r = sol.distinctNames(["coffee", "donuts", "time", "toffee"])
        print(r)
        assert r == 6

        r = sol.distinctNames(["lack", "back"])
        print(r)
        assert r == 0

    unit_test(Solution())
