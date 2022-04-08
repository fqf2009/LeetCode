# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Constraints:
#   1 <= nums.length <= 105
#   0 <= nums[i] <= 105

# Binary Search with slight change. Each time visit & check two elements in the middle.
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return nums[0]

        i, j = (len(nums) - 1) // 2, (len(nums) + 1) // 2
        if nums[i] == nums[j]:
            i -= 1
            j += 1
        else:
            if i == 0:
                return nums[i]
            elif nums[i - 1] != nums[i]:
                return nums[i]
            else:
                i -= 2

            if j == len(nums) - 1:
                return nums[j]
            elif nums[j + 1] != nums[j]:
                return nums[j]
            else:
                j += 2

        res = self.singleNonDuplicate(nums[: i + 1])
        if res != -1:
            return res
        return self.singleNonDuplicate(nums[j:])


if __name__ == "__main__":
    obj = Solution()

    input = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    expected = 2
    output = obj.singleNonDuplicate(input)
    print(output)
    assert output == expected

    input = [3, 3, 7, 7, 10, 11, 11]
    expected = 10
    output = obj.singleNonDuplicate(input)
    print(output)
    assert output == expected

    input = [3, 3, 7, 7, 10, 10, 11, 11, 12, 12, 13]
    expected = 13
    output = obj.singleNonDuplicate(input)
    print(output)
    assert output == expected

    input = [1, 3, 3, 7, 7, 10, 10, 11, 11, 12, 12, 13, 13]
    expected = 1
    output = obj.singleNonDuplicate(input)
    print(output)
    assert output == expected
