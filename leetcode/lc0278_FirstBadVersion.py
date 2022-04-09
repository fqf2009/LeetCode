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


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return version >= 10


# Binary Search Template 2
class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n + 1
        while i < j:
            k = (i + j) // 2
            if isBadVersion(k):
                j = k
            else:
                i = k + 1

        return i


# Binary Search
class Solution1:
    def firstBadVersion(self, n: int) -> int:
        i, j, res = 1, n, n+1
        while i <= j:
            k = (i + j) // 2
            if isBadVersion(k):
                res = k
                j = k - 1
            else:
                i = k + 1

        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from unittest.mock import patch
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            (100, 3, 3),
            (50, 39, 39),
            (50, 1, 1),
            (50, 100, 51),
            (500, 500, 500),
            (50, 0, 1),
        ])
        @patch('__main__.isBadVersion')
        def test_firstBadVersion(self, n, bad_version, expected, mock_obj):
            mock_obj.side_effect = lambda v: v >= bad_version

            sol = self.solution()       # type:ignore
            r = sol.firstBadVersion(n)
            self.assertEqual(r, expected)

    main()
