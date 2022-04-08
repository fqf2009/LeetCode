from typing import List

# Given n cuboids where the dimensions of the i-th cuboid is 
#     cuboids[i] = [width(i), length(i), height(i)] (0-indexed). 
# Choose a subset of cuboids and place them on each other.
# You can place cuboid i on cuboid j if 
#   width(i) <= width(j) and length(i) <= length(j) and height(i) <= height(j) 
# You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.
# Return the maximum height of the stacked cuboids.


# DP (Dynamic Programing)
# - Rotate cuboid to make it [h, w, l] where h >= w >= l;
# - Sort cuboids in heights descending: [[h1, w1, l1], [h2, w2, l2], ...] where h1 >= h2
# - dp[i]: if i-th sorted cuboid is to be used, the height of the tower, so
#   dp[i] = max(dp[j]) + h(i), where: cuboid(i) can be put on top of cuboid(j)
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort(reverse=True)
        cuboids.sort(reverse=True)
        dp = [0] * len(cuboids)
        maxH = 0
        for i in range(len(cuboids)):
            precedingH = 0
            for j in reversed(range(i)):
                if cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                    precedingH = max(dp[j], precedingH)
                    if precedingH >= maxH:
                        break   
            dp[i] = precedingH + cuboids[i][0]
            maxH = max(maxH, dp[i])

        return maxH


if __name__ == '__main__':
    sol = Solution()

    r = sol.maxHeight(cuboids = [[36,46,41],[15,100,100],[75,91,59],[13,82,64]])
    print(r)
    assert(r == 182)

    r = sol.maxHeight(cuboids = [[50,45,20],[95,37,53],[45,23,12]])
    print(r)
    assert(r == 190)

    r = sol.maxHeight(cuboids = [[38,25,45],[76,35,3]])
    print(r)
    assert(r == 76)

    r = sol.maxHeight(cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
    print(r)
    assert(r == 102)
