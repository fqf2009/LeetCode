from typing import List, Optional
import bisect

# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. A subsequence is a sequence that can be derived 
# from an array by deleting some or no elements without changing the order 
# of the remaining elements. For example, [3,6,2,7] is a subsequence of 
# the array [0,3,1,6,2,2,7].

# use bisect lib to do binary search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        lis = 0  # point to the end of dp[]
        for n in nums[1:]:
            if n > dp[lis]:
                lis += 1
                dp[lis] = n
                continue
            p = bisect.bisect_left(dp, n, 0, lis)
            if n < dp[p]:
                dp[p] = n

        return lis + 1

# Time complexity: O(n*log(n)), Space complexity: O(n)
# for a LIS with length of m, dp[m-1] records minimum 
# ending value of this LIS, so that if future number
# is larger this value, then it represents another 
# (LIS + 1) is found. Use the binary search to find
# the proper place for this number among past LIS.
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        lis = 0  # point to the end of dp[]
        for n in nums[1:]:
            if n > dp[lis]:
                lis += 1
                dp[lis] = n
                continue
            left, right = 0, lis
            while left <= right:
                mid = (left + right) // 2
                if n == dp[mid]:
                    break
                if n > dp[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                dp[left] = min(dp[left], n)

        return lis + 1

# DP (Dynamic Porgramming)
# dp[i] records LIS with ending number of nums[i]
# Time complexity: O(n^2), Space complexity: O(n)
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums [i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    
    r = sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
    print(r)
    assert(r == 6)

    r = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(r)
    assert(r == 4)

    r = sol.lengthOfLIS([0,1,0,3,2,3])
    print(r)
    assert(r == 4)

    r = sol.lengthOfLIS([7,7,7,7,7,7,7])
    print(r)
    assert(r == 1)
