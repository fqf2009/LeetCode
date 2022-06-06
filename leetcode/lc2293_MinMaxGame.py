# You are given a 0-indexed integer array nums whose length is a power of 2.
# Apply the following algorithm on nums:
#  - Let n be the length of nums. If n == 1, end the process. Otherwise,
#    create a new 0-indexed integer array newNums of length n / 2.
#  - For every even index i where 0 <= i < n / 2, assign the value of
#    newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
#  - For every odd index i where 0 <= i < n / 2, assign the value of
#    newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
#  - Replace the array nums with newNums.
#  - Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm.
# Constraints:
#   1 <= nums.length <= 1024
#   1 <= nums[i] <= 10^9
#   nums.length is a power of 2.
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        N = nums
        while len(N) > 1:
            N = [min(N[2 * i], N[2 * i + 1]) if i % 2 == 0 else max(N[2 * i], N[2 * i + 1]) 
                    for i in range(len(N) // 2)]

        return N[0]


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minMaxGame([1, 3, 5, 2, 4, 8, 2, 2])
        print(r)
        assert r == 1

        r = sol.minMaxGame([3])
        print(r)
        assert r == 3

    unit_test(Solution())
