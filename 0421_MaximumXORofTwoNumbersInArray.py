from typing import List
# Given an integer array nums, return the maximum result of 
# nums[i] XOR nums[j], where 0 <= i <= j < n.

# Bitwise Trie:
#  - Find the max number M
#  - Build data structure Trie, implemented via a binary tree, with height
#    of (1 + log(M)), each branch represents 0 or 1, which are the prefix of
#    binary form of the numbers.
#  - The Trie is gradually built, by adding numbers one by one
#  - Each time when a number is begin added, compare its path with Trie,
#    at the same time traverse a virtual path in Trie, always choose opposite
#    branch direction to the number's branch at each level, unless there is
#    no options. Remember this opposite choice, the XOR can be calculated. 
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        M = max(nums)
        L = len(bin(M)[2:])
        leadingZeros = '0' * L
        res = 0
        for n in nums:
            s = bin(n)[2:]
            s = leadingZeros[:L-len(s)] + s
            t1 = v1 = trie
            xor = 0
            for ch in s:
                op = str(1 - int(ch))
                if ch not in t1:
                    t1[ch] = {}
                t1 = t1[ch]
                xor *= 2
                if op in v1:
                    v1 = v1[op]
                    xor += 1
                else:
                    v1 = v1[ch]
            res = max(res, xor)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8])
        print(r)
        assert(r == 28)

        r = sol.findMaximumXOR(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])
        print(r)
        assert(r == 127)

    unitTest(Solution())
