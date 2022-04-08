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
#   1 <= bad <= n <= 2^31 - 1
import pytest


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
g_bad = -1
def isBadVersion(version: int) -> bool:
    return version >= g_bad


# Binary Search
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


if __name__ == "__main__":
    # @pytest.mark.parametrize('sol,n', [[Solution, 5], [Solution, 1], [Solution, 0]])
    def test_firstBadVersion(): # solution, n
        sol = Solution()
        n = 5
        globals()['g_bad'] = n
        r = sol.firstBadVersion(n)
        assert r == n

    pytest.main()
