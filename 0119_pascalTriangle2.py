class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        nums = self.getRow(rowIndex - 1)
        res = [nums[0]]
        for i in range(len(nums) - 1):
            res.append(nums[i] + nums[i+1])
        res.append(nums[-1])
        return res


# test case
if __name__ == "__main__":
    rowIndex = 4
    expected = [1, 4, 6, 4, 1]
    r = Solution().getRow(rowIndex)
    print(r)
    assert(r == expected)

    rowIndex = 3
    expected = [1, 3, 3, 1]
    r = Solution().getRow(rowIndex)
    print(r)
    assert(r == expected)

    rowIndex = 0
    expected = [1]
    r = Solution().getRow(rowIndex)
    print(r)
    assert(r == expected)

    rowIndex = 1
    expected = [1, 1]
    r = Solution().getRow(rowIndex)
    print(r)
    assert(r == expected)
