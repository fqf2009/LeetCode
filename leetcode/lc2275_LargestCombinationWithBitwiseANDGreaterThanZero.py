# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
#  - For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
#  - Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the 
# bitwise AND of every combination of numbers of candidates. Each number
# in candidates may only be used once in each combination.
# Return the size of the largest combination of candidates with a bitwise 
# AND greater than 0.
# Constraints:
#   1 <= candidates.length <= 10^5
#   1 <= candidates[i] <= 10^7
from collections import defaultdict
from typing import List


# T/S: O(n*w), O(n), where w = avg_bit_len_of_numbers
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = defaultdict(int)
        for v in candidates:
            s = bin(v)[2:]
            for i, ch in enumerate(reversed(s)):
                if ch == '1':
                    res[i] += 1
        return max(res.values())
        

if __name__ == '__main__':
    def unit_test(sol):
        r = sol.largestCombination([16,17,71,62,12,24,14])
        print(r)
        assert r == 4

        r = sol.largestCombination([8,8])
        print(r)
        assert r == 2


    unit_test(Solution())
