# You are given two strings start and target, both of length n. Each string
# consists only of the characters 'L', 'R', and '_' where:
#  - The characters 'L' and 'R' represent pieces, where a piece 'L' can
#    move to the left only if there is a blank space directly to its left,
#    and a piece 'R' can move to the right only if there is a blank space
#    directly to its right.
#  - The character '_' represents a blank space that can be occupied by
#    any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the
# pieces of the string start any number of times. Otherwise, return false.
# Constraints:
#   n == start.length == target.length
#   1 <= n <= 105
#   start and target consist of the characters 'L', 'R', and '_'.


# Two pointers
# - i, j pointing to pos in start and target strings
# - in each iteration (for next 'L' or 'R'):
#   scan through, and skip all '_' for both pointers
# - if the chars (from start and target) are different, fail;
#   otherwise, if the char is 'L', i should >= j, so it can move to left
#              if the char is 'R', i should <= j, so it can move to right
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j, n = 0, 0, len(start)
        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            ch1 = start[i] if i < n else '_'
            ch2 = target[j] if j < n else '_'
            if ch1 != ch2:
                return False
            if ch1 == 'L' and i < j:
                return False
            if ch1 == 'R' and i > j:
                return False
            i += 1
            j += 1

        return True


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.canChange("_L__R__R_", target = "L______RR")
        print(r)
        assert r == True

        r = sol.canChange("R_L_", target = "__LR")
        print(r)
        assert r == False

        r = sol.canChange("_R", target = "R_")
        print(r)
        assert r == False

    unit_test(Solution())
