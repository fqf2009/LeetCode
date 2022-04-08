# There are two types of persons:
#  - The good person: The person who always tells the truth.
#  - The bad person: The person who might tell the truth and might lie.
# You are given a 0-indexed 2D integer array statements of size n x n 
# that represents the statements made by n people about each other. More
# specifically, statements[i][j] could be one of the following:
#   0 which represents a statement made by person i that person j is a bad person.
#   1 which represents a statement made by person i that person j is a good person.
#   2 represents that no statement is made by person i about person j.
# Additionally, no person ever makes a statement about themselves. Formally, 
# we have that statements[i][i] = 2 for all 0 <= i < n.

# Return the maximum number of people who can be good based on the 
# statements made by the n people.
# Constraints:
#   n == statements.length == statements[i].length
#   2 <= n <= 15
#   statements[i][j] is either 0, 1, or 2.
#   statements[i][i] == 2
from typing import List
from itertools import product


# Improvement: O(n*(2^n))
#  - use bit-mask (1s, 0s) in an int to represent the good (1) and bad (0) person.
#  - use bit Xor to test conflict.
#  - no statement (2) situation should be masked away.
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n, res = len(statements), 0
        stmt = [0] * n
        mask = [0] * n  # to mask away no-statement situation
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 1:
                    stmt[i] |= (1<<j)
                elif statements[i][j] == 2:
                    mask[i] |= (1<<j)
            mask[i] = ~mask[i] # & (2**n - 1)  # remove the 1 bit higher than n, not necessary

        for i in range(1, 2**n):    # generate bit-mask, no need to backtrack
            good = 0
            for j in range(n):      # iterate every person
                if i & (1<<j) != 0: # if this person is good
                    # check its statment against bit-mask
                    if (i & mask[j]) ^ (stmt[j] & mask[j]) != 0:
                        break       # conflict, loop to next i
                    good += 1
            else:
                res = max(res, good)

        return res


# Use Python bultin library to simulate backtracking
class Solution1:
    def maximumGood(self, statements: List[List[int]]) -> int:
        res, n = 0, len(statements)
        for persons in product((0, 1), repeat=n):
            good = 0
            conflict = False
            for i in range(n):
                if persons[i] == 1:
                    good += 1
                    for k in range(n):
                        if statements[i][k] != 2 and statements[i][k] != persons[k]:
                            conflict = True
                            break
                if conflict:
                    break
            else:
                res = max(res, good)

        return res


# Backtrack: O((n^2)*(2^n))
#  - use backtrack to simulate all conbination of good and bad person (2^n)
#  - test every good person's statements against it.
class Solution2:
    def maximumGood(self, statements: List[List[int]]) -> int:
        i, res, n = 0, 0, len(statements)
        persons = [2] * n
        while i >= 0:
            if persons[i] == 2:
                persons[i] = 1
            elif persons[i] == 1:
                persons[i] = 0
            else:
                persons[i] = 2
                i -= 1
                continue

            if i < n - 1:
                i += 1
                continue

            good = 0
            conflict = False
            for j in range(n):
                if persons[j] == 1:
                    good += 1
                    for k in range(n):
                        if statements[j][k] != 2 and statements[j][k] != persons[k]:
                            conflict = True
                            break
                if conflict:
                    break
            else:
                res = max(res, good)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumGood(statements = [[2,1,2],
                                          [1,2,2],
                                          [2,0,2]])
        print(r)
        assert(r == 2)

        r = sol.maximumGood(statements = [[2,0],[0,2]])
        print(r)
        assert(r == 1)

        r = sol.maximumGood(statements =[[2,2,2,2],
                                         [1,2,1,0],
                                         [0,2,2,2],
                                         [0,0,0,2]])
        print(r)
        assert(r == 1)


    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
