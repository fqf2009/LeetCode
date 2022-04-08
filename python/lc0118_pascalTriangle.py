class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        res = self.generate(numRows - 1)
        nums0 = res[numRows - 2]
        nums1 = [nums0[0]]
        for i in range(len(nums0) - 1):
            nums1.append(nums0[i] + nums0[i+1])
        nums1.append(nums0[-1])
        res.append(nums1)
        return res


# test case
if __name__ == "__main__":
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    r = Solution().generate(numRows)
    print(r)
    assert(r == expected)

    numRows = 1
    expected = [[1]]
    r = Solution().generate(numRows)
    print(r)
    assert(r == expected)
