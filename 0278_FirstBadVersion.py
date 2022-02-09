# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the
# quality check. Since each version is developed based on the previous
# version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the
# first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.

# Constraints:
#   1 <= bad <= n <= 231 - 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
g_bad = -1
def isBadVersion(version: int) -> bool:
    return version >= g_bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j, res = 1, n, -1
        while i <= j:
            k = (i + j) // 2
            if isBadVersion(k):
                res = k
                j = k - 1
            else:
                i = k + 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        globals()['g_bad'] = 4
        r = sol.firstBadVersion(n=5)
        print(r)
        assert r == 4

        globals()['g_bad'] = 1
        r = sol.firstBadVersion(n=1)
        print(r)
        assert r == 1

    unitTest(Solution())