from typing import List
# Given an integer array nums, return the maximum result of 
# nums[i] XOR nums[j], where 0 <= i <= j < n.

# Bitwise Trie:
# https://en.wikipedia.org/wiki/Trie#Bitwise_tries
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
        # max length of binary string of nums[i]
        max_len = len(bin(max(nums))[2:])   # length-2 may lead to negtive length
        leadingZeros = '0' * max_len
        res = 0
        for val in nums:
            s = bin(val)[2:]
            s = leadingZeros[:max_len-len(s)] + s   # binary form of val, at fixed length

            t1 = t2 = trie  # t1 is trie to store s; t2 is check negation of s
            xor = 0
            for ch in s:
                t1 = t1.setdefault(ch, dict())  # store ch in trie
                op = str(1 - int(ch))
                xor *= 2
                if op in t2:
                    t2 = t2[op]
                    xor += 1
                else:           # now ch must in t2, because all path is in fixed length
                    t2 = t2[ch]
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
