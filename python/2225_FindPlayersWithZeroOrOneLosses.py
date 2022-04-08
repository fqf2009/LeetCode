# You are given an integer array matches where 
# matches[i] = [winneri, loseri] indicates that the player 
# winneri defeated player loseri in a match.
#
# Return a list answer of size 2 where:
#  - answer[0] is a list of all players that have not lost any matches.
#  - answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
#  - You should only consider the players that have played at least one match.
#  - The testcases will be generated such that no two matches will have the same outcome.
# Constraints:
#   1 <= matches.length <= 10^5
#   matches[i].length == 2
#   1 <= winneri, loseri <= 10^5
#   winneri != loseri
#   All matches[i] are unique.
from typing import Counter, List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set(x[0] for x in matches)
        loser_counter = Counter(x[1] for x in matches)
        lose1 = [x for x, freq in loser_counter.items() if freq == 1]
        loser = set(loser_counter.keys())

        return [sorted(winner - loser), sorted(lose1)]


class Solution1:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lose_one = set()
        lose_many = set()
        for p1, p2 in matches:
            if p2 in winners:
                winners.remove(p2)
                lose_one.add(p2)
            elif p2 in lose_one:
                lose_one.remove(p2)
                lose_many.add(p2)
            elif p2 not in lose_many:
                lose_one.add(p2)
        
            if p1 not in lose_one and p1 not in lose_many:
                winners.add(p1)

        return [sorted(winners), sorted(lose_one)]


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],
                            [4,5],[4,8],[4,9],[10,4],[10,9]])
        print(r)
        assert r == [[1,2,10],[4,5,7,8]]

        r = sol.findWinners([[2,3],[1,3],[5,4],[6,4]])
        print(r)
        assert r == [[1,2,5,6],[]]

    unit_test(Solution())
    unit_test(Solution1())
