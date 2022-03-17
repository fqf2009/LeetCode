# You are given an array of logs. Each log is a space-delimited string of words,
# where the first word is the identifier.
# There are two types of logs:
# - Letter-logs: All words (except the identifier) consist of lowercase English letters.
# - Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
# - The letter-logs come before all digit-logs.
# - The letter-logs are sorted lexicographically by their contents. If their contents
#   are the same, then sort them lexicographically by their identifiers.
# - The digit-logs maintain their relative ordering.
# Return the final order of the logs.
# Constraints:
#   1 <= logs.length <= 100
#   3 <= logs[i].length <= 100
#   All the tokens of logs[i] are separated by a single space.
#   logs[i] is guaranteed to have an identifier and at least one word after the identifier.
from typing import List


# Merge Sort - T/S: O(n*log(n)), O(n)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(s: str):
            pos = s.index(' ')
            if '0' <= s[pos + 1] <= '9':
                return ('~', '~')
            else:
                return (s[pos + 1:], s[:pos])
        
        def merge(L1: List[str], L2: List[str]) -> List[str]:
            n1, n2 = len(L1), len(L2)
            i = j = 0
            res = []
            while i < n1 and j < n2:
                if cmp(L1[i]) <= cmp(L2[j]):
                    res.append(L1[i])
                    i += 1
                else:
                    res.append(L2[j])
                    j += 1

            if i < n1:
                res.extend(L1[i:])
            if j < n2:
                res.extend(L2[j:])
            
            return res

        def mergeSort(L):
            n = len(L)
            if len(L) > 1:
                return merge(mergeSort(L[:n//2]), mergeSort(L[n//2:]))
            else:
                return L

        return mergeSort(logs)


# Sort: O(n*log(n))
class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(s: str):
            pos = s.index(' ')
            if '0' <= s[pos + 1] <= '9':
                return ('~', '~')
            else:
                return (s[pos + 1:], s[:pos])

        return sorted(logs, key=cmp)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                                 "let2 own kit dig", "let3 art zero"])
        print(r)
        assert r == ["let1 art can", "let3 art zero", "let2 own kit dig",
                     "dig1 8 1 5 1", "dig2 3 6"]

        r = sol.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                                 "ab1 off key dog", "a8 act zoo"])
        print(r)
        assert r == ["g1 act car", "a8 act zoo", "ab1 off key dog",
                     "a1 9 2 3 1", "zo4 4 7"]

        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                "ab1 off key dog", "a8 act zoo", "a2 act car"]
        r = sol.reorderLogFiles(logs)
        print(r)
        assert r == ["a2 act car", "g1 act car", "a8 act zoo",
                     "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

    unitTest(Solution())
    unitTest(Solution1())
