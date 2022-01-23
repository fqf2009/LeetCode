# There are two types of persons:
#  - The good person: The person who always tells the truth.
#  - The bad person: The person who might tell the truth and might lie.
# You are given a 0-indexed 2D integer array statements of size n x n that represents 
# the statements made by n people about each other. More specifically, statements[i][j] 
# could be one of the following:

# 0 which represents a statement made by person i that person j is a bad person.
# 1 which represents a statement made by person i that person j is a good person.
# 2 represents that no statement is made by person i about person j.

# Additionally, no person ever makes a statement about themselves. Formally, we have that 
# statements[i][i] = 2 for all 0 <= i < n.

# Return the maximum number of people who can be good based on the statements made by the n people.

from typing import List


# Improvement:
#  - use an integer and its bits (1s, 0s) to represent the good and bad person.
#  - use bit Xor to test conflict, and no statement (2) situation should be masked away.
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n, res = len(statements), 0
        stmt = [0] * n
        mask = [0] * n
        for i in range(n):
            k = 1
            for j in range(n):
                if statements[i][j] == 1:
                    stmt[i] |= k
                elif statements[i][j] == 2:
                    mask[i] |= k
                k <<= 1
            mask[i] = ~mask[i] & (2**n - 1)

        for i in range(1, 2**n):
            k = 1
            good = 0
            for j in range(n):
                if i & k != 0:
                    if (i & mask[j]) ^ (stmt[j] & mask[j]) != 0:
                        break
                    good += 1
                k <<= 1
            else:
                res = max(res, good)

        return res


# Backtrack: O(2^n),  i.e. n^2 * 2^n
#  - use backtrack to simulate all conbination (2)
#  - test every good person's statements
class Solution1:
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

            success = True
            for j in range(n):
                if persons[j] == 1:
                    for k in range(n):
                        if statements[j][k] != 2 and statements[j][k] != persons[k]:
                            success = False
                            break
                if not success:
                    break

            if success:
                res = max(res, persons.count(1))

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumGood(statements = [[2,1,2],[1,2,2],[2,0,2]])
        print(r)
        assert(r == 2)

        r = sol.maximumGood(statements = [[2,0],[0,2]])
        print(r)
        assert(r == 1)

    unitTest(Solution())
    unitTest(Solution1())
