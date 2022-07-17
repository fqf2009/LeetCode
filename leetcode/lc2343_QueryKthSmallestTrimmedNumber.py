# You are given a 0-indexed array of strings nums, where each string is of
# equal length and consists of only digits.
# You are also given a 0-indexed 2D integer array queries where
# queries[i] = [ki, trimi]. For each queries[i], you need to:
# - Trim each number in nums to its rightmost trimi digits.
# - Determine the index of the kith smallest trimmed number in nums. If two trimmed
#   numbers are equal, the number with the lower index is considered to be smaller.
# - Reset each number in nums to its original length.
# Return an array answer of the same length as queries, where answer[i] is the
# answer to the ith query.
# Note:
# - To trim to the rightmost x digits means to keep removing the leftmost digit,
#   until only x digits remain.
# - Strings in nums may contain leading zeros.
# Constraints:
#   1 <= nums.length <= 100
#   1 <= nums[i].length <= 100
#   nums[i] consists of only digits.
#   All nums[i].length are equal.
#   1 <= queries.length <= 100
#   queries[i].length == 2
#   1 <= ki <= nums.length
#   1 <= trimi <= nums[i].length
from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        sorted_nums = {}
        res = []
        for k, trim in queries:
            if trim not in sorted_nums:
                sorted_nums[trim] = sorted((x[-trim:], i) for i, x in enumerate(nums))
            res.append(sorted_nums[trim][k - 1][1])

        return res


class Solution1:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        return [sorted(zip(map(lambda x: x[-trim:], nums), range(len(nums))))[k - 1][1]
                for k, trim in queries]


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.smallestTrimmedNumbers(["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]])
        print(r)
        assert r == [2, 2, 1, 0]

        r = sol.smallestTrimmedNumbers(["24", "37", "96", "04"], [[2, 1], [2, 2]])
        print(r)
        assert r == [3, 0]

    unit_test(Solution())
    unit_test(Solution1())
