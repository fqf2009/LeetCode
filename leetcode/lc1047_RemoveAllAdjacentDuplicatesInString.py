# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal
# letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have
# been made. It can be proven that the answer is unique.
#  Constraints:
#   1 <= s.length <= 105
#   s consists of lowercase English letters.


# Stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.removeDuplicates("abbaca")
        print(r)
        assert r == "ca"

        r = sol.removeDuplicates("azxxzy")
        print(r)
        assert r == "ay"

    unit_test(Solution())
