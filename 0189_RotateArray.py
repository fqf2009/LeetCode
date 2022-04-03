# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Do not return anything, modify nums in-place instead.
# Constraints:
#   1 <= nums.length <= 10^5
#   -2^31 <= nums[i] <= 2^31 - 1
#   0 <= k <= 10^5
from typing import List


# rotate 1 time, but each move will skip k items
# time O(n), space O(1)
# Analysis: (note i-th value use 1-based index)
# - if n % k == 0, e.g. n == 9, k == 3
#   save n9, move n6 -> n9, n3 -> n6, n9 -> n3
#   save n8, move n5 -> n8, n2 -> n5, n8 -> n2
#   save n7, ...
# - if n % k != 0, e.g. n == 9, k == 4
#   save n9, move n5 -> n9, n1 -> n5, n6-> n1, ...
#   when wrap around, e.g., nums[6] is nums[1 + 9 - 4]
# - if n*a == k*b and b < n, where a>0 and b>0 are minimum possible value,
#   e.g. n == 6, k == 4, b == 3 it means after 3 moves, it forms a cycle,
#   we need to move (n-1)th value, ...
#   so the first scenario (n % k == 0), is the special case of this.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        curPos = savePos = n - 1
        saveVal = nums[savePos]
        for i in range(n):
            nextPos = (curPos + n - k) % n
            if nextPos == savePos:
                nums[curPos] = saveVal
                savePos -= 1
                saveVal = nums[savePos]
                curPos = savePos
            else:
                nums[curPos] = nums[nextPos]
                curPos = nextPos


# rotate m = min(k%n, n-k%n) times : time O(n*m), space O(1)
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        if k <= n - k:   # rotate to the right
            for _ in range(k):
                v = nums[-1]
                nums[1:] = nums[:-1]
                nums[0] = v
        else:           # rotate to the left
            k = n - k
            for _ in range(k):
                v = nums[0]
                nums[:-1] = nums[1:]
                nums[-1] = v

# use buffer: time O(n), space O(m), where m = min(k%n, n-k%n)
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        if k <= n - k:  # rotate to the right
            buf = nums[-k:]
            nums[k:] = nums[0:-1-k+1]
            nums[:k] = buf
        else:           # rotate to the left
            k = n - k
            buf = nums[:k]
            nums[:-k] = nums[k:]
            nums[-k:] = buf


if __name__ == '__main__':
    def unitTest(sol):
        nums = [1, 2, 3, 4, 5, 6]
        sol.rotate(nums, k=4)
        print(nums)
        assert nums == [3, 4, 5, 6, 1, 2]

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sol.rotate(nums, k=3)
        print(nums)
        assert nums == [7, 8, 9, 1, 2, 3, 4, 5, 6]

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sol.rotate(nums, k=6)
        print(nums)
        assert nums == [4, 5, 6, 7, 8, 9, 1, 2, 3]

        nums = [1, 2, 3, 4, 5, 6, 7]
        sol.rotate(nums, k=3)
        print(nums)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

        nums = [1, 2, 3, 4, 5, 6, 7]
        sol.rotate(nums, k=3)
        print(nums)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

        nums = [1, 2, 3, 4, 5, 6, 7]
        sol.rotate(nums, k=6)
        print(nums)
        assert nums == [2, 3, 4, 5, 6, 7, 1]

        nums = [-1, -100, 3, 99]
        sol.rotate(nums, k=2)
        print(nums)
        assert nums == [3, 99, -1, -100]

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
